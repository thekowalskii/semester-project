import { useNavigate } from "react-router-dom"


function CartItemOrderButtonTest() {
    const navigate = useNavigate()

    const handleOrder = () => {
        navigate('/cart/order/7bafc400-8e46-4925-9f33-1b2e11c6002a?category=paintings')
    }

	return (
		<>
			<button className='card-order-button' onClick={() => handleOrder()}>
                Order pisun
            </button>
		</>
	)
}

export default CartItemOrderButtonTest
