from fastapi import Depends

from backend.models import User
from backend.api.dependencies.db import Session_dp


async def get_cart_by_email(session: Session_dp, email: str):
    '''
    This function gets and returns user\'s cart in database by email
    '''

    user = await User.get(session=session, field=User.email, value=email)
    return user.cart


user_email_dp = Depends(get_cart_by_email)
