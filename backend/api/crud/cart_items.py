import uuid

from fastapi import HTTPException, status

from backend.api.dependencies.db import Session_dp
from backend.models import Cart, Painting, CartItem


async def add_item(
        session: Session_dp,
        cart_id: uuid.UUID,
        product_id: uuid.UUID,
        quantity: int = 1
):   
    cart = await Cart.get(session=session, field=Cart.id, value=cart_id)
    product = await Painting.get(session=session, field=Painting.id, value=product_id)

    if quantity > product.available:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Sorry! We don\'t have so much products in our storage. Available amount: {product.available}'
        )

    for item in cart.cart_items:
        if str(item.product_id) == product_id:
            if (item.quantity + quantity) > product.available:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f'Sorry! We don\'t have so much products in our storage.'
                )
            
            item.quantity += quantity
            cart.update_total_price()
            await session.commit()

            return 201

    # Create new cart_item

    cart_item = await CartItem.create(
        session=session,
        product_id=product_id,
        quantity=quantity,
        cart=cart,
    )

    cart.update_total_price()
    await session.commit()

    return 201


async def remove_item(
        session: Session_dp,
        cart_id: uuid.UUID,
        product_id: uuid.UUID
):
    cart = await Cart.get(session=session, field=Cart.id, value=cart_id)
    product = await Painting.get(session=session, field=Painting.id, value=product_id)
    cart_item = await CartItem.get(session=session, field=CartItem.product_id, value=product_id)

    for item in cart.cart_items:
        if str(item.product_id) == product_id:
            cart.update_total_price()

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            elif cart_item.quantity == 1:
                await session.delete(cart_item)

            await session.commit()

    cart.update_total_price()
    await session.commit()

    return 203
