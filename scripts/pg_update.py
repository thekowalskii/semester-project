from backend.models import Cart
from backend.config import ADMIN_PASSWORD


def pg_clear():
   if input('Enter admin pas: ') != ADMIN_PASSWORD:
        print('Incorrect password')
        return
   
   # update total_prices

