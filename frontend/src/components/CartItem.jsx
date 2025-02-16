function CartItem({ item }) {
    const url = 'http://127.0.0.1:8000/paintings/get_one?title=' + item.product_title

    return (
        <div className='product-container' key={item.title + '_pc'}>
            <div className="image" key={item.title + '_image'} style={
                {
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${url})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }
            }></div>
            
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
