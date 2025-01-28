import time

from fastapi import APIRouter, Request, Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from backend.api.dependencies.db import Session_dp
from backend.schemas.user import UserSchema, UserSigninForm
from backend.models.user import User
from backend.utils import token_manager, password_manager


auth_r = APIRouter(tags=['auth'])

registrate_schema = OAuth2PasswordBearer(tokenUrl='registrate')
authenticate_schema = OAuth2PasswordBearer(tokenUrl='authenticate')


@auth_r.post('/signup')
async def signup(request: Request, response: Response, session: Session_dp, form_data: UserSchema = Depends()):

    user = await User.get(session=session, field=User.email, value=form_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email already exist'
        )

    # Creating new User is database (PG)
    user = await User.create(session=session, user=form_data)

    # Creating JWT token to add in cookies
    jwt_payload = {
        'scope': user.role,
        'email': user.email,
        "exp": time.time() + 10
    }

    token = token_manager.encode_token(payload=jwt_payload)
    request.session['access_token'] = token


    return token


@auth_r.post('/signin')
async def signin(request: Request, response: Response, session: Session_dp, form_data: UserSigninForm):
    user = await User.get(session=session, field=User.email, value=form_data.email)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email does not exist'
        )

    password_manager.verify_password(form_data.password, user.password)
    
    # Creating JWT token to add in cookies
    jwt_payload = {
        'scope': user.role,
        'email': user.email,
        "exp": time.time() + 10
    }

    token = token_manager.encode_token(payload=jwt_payload)
    request.session['access_token'] = token

    response.headers['Access-Token'] = token

    return token


@auth_r.post('/logout')
async def logout(request: Request):
    del request.session['access_token']

    return 'Loged Out'
    


# @auth_r.get('/all_users')
# async def get_all_users(request: Request, response: Response, session: Session_dp):
#     print(f'GET ALL USERS cookies: {await request.body()}')


#     users = await User.all(session=session)

#     response.set_cookie(
#         'access_token', 'some_jwt_token',
#         samesite='none', httponly=False, secure=True
#     )

#     response.headers

#     return users


# @auth_r.post('/some_post')
# async def some_post(request: Request, response: Response):
#     print(f'SOME POST cookies: {await request.body()}')

#     response.set_cookie(
#         'access_token', 'some_jwt_token',
#         samesite='none', httponly=False
#     )

#     response.headers

#     return 'Ok'


# @auth_r.get('/check_token')
# async def check_token(request: Request):
#     token = request.session.get('access_token')

#     return token


# git commit -m "Added authentication" -m "Here i have added such endpoints as /signup, /signin and
#  /logout. It will probably modifide in future. "
