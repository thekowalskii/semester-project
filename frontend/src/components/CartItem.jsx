import { useEffect } from "react"


function CartItem({ item }) {

    return (
        <div className='product-container' key={item.title + '_pc'}>

            <div className="info" key={item.product_title + '_info'}>
                <h3 key={item.product_title + '_t'}>{item.product_title}</h3>
                <h3 key={item.product_title + '_p'}>Price: {item.product_price}₴</h3>
                <h3 key={item.product_title + '_q'}>Quantity: {item.quantity}</h3>
                <p key={item.product_title + '_d'}>
                    {item.description}
                    <br key={item.title + '_d_br'}/>
                    {item.available}
                </p>
            </div>
        </div>
    )
}


export default CartItem
