import time
import uuid

from fastapi import APIRouter, Request, Response, Depends, HTTPException, status, Form

from backend.api.dependencies.db import Session_dp
from backend.schemas.user import UserSchema, UserSigninForm
from backend.models.user import Cart
from backend.api.crud.cart_items import add_item, remove_item
from backend.api.dependencies.carts import user_email_dp


carts_r = APIRouter(tags=['carts'], prefix='/carts')


@carts_r.post('/create')
async def create_cart(session: Session_dp):
    cart = await Cart.create(session=session)

    return cart.id


@carts_r.post('/add_product')
async def add_product(session: Session_dp,
                      cart_id: uuid.UUID = Form(...),
                      product_id = Form(...),
                      quantity: int = Form(...)
):
    res = await add_item(
        session=session, 
        cart_id=cart_id, 
        product_id=product_id, 
        quantity=quantity
    )

    return res


@carts_r.get('/cart_info')
async def get_cart_info(session: Session_dp, cart_id ):
    if cart_id == 'undefined':
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You do not have a cart'
        )

    cart = await Cart.get(session=session, field=Cart.id, value=cart_id)

    if not cart:
        return 'Such cart does not exist'

    info = {
        'total_price': cart.total_price,
        'created_at': cart.created_at,
        'status': cart.status,
        'items': [p for p in cart.cart_items],
    }

    return info


@carts_r.delete('/remove_product')
async def add_product(session: Session_dp,
                      cart_id: uuid.UUID = Form(...),
                      product_id = Form(...)
):
    res = await remove_item(
        session=session, 
        cart_id=cart_id, 
        product_id=product_id
    )

    return res
