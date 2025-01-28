from fastapi import Depends, Request, HTTPException, status

from backend.services import token_manager


def admin_scope(request: Request):
    '''
    This function checks users's access token. User can use the route ONLY in that case, if scope is `admin`.

    Return `scope`.
    '''

    access_token = request.session.get('access_token')

    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='You are not authorized'
        )

    payload = token_manager.decode_token(access_token)

    scope = payload.get('scope')

    if scope != 'admin':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have permision to use this route.'
        )

    return scope

admin_scope_dp = Depends(admin_scope)
