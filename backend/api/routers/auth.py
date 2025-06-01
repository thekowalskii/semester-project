import time

from fastapi import APIRouter, Request, Response, Depends, HTTPException, status, Query

from backend.api.dependencies.db import Session_dp
from backend.schemas.user import UserSchema, UserSigninForm, UserResponseSchema
from backend.models.user import User
from backend.utils import password_manager
from backend.services import token_manager


auth_r = APIRouter(tags=['auth'], prefix='/auth')


@auth_r.post('/signup')
async def signup(request: Request, response: Response, session: Session_dp, form_data: UserSchema):

    user = await User.get(session=session, field=User.email, value=form_data.email)

    if user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='User with such email already exist'
        )

    # Creating new User is database (PG)
    user = await User.create(session=session, user=form_data)

    # Creating JWT token to add in cookies

    token = token_manager.encode_token(user=user)
    request.session['access_token'] = token

    print(user.role)

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

    user = UserResponseSchema.model_validate(user)

    token = token_manager.encode_token(user=user)
    request.session['access_token'] = token

    res = {
        'token': token,
        'email': user.email,
        'cart': user.cart
    }

    return res


@auth_r.post('/logout')
async def logout(request: Request):
    try:
        del request.session['access_token']
    except Exception as _:
        return 'You are not signed in'

    return 'Loged Out'

