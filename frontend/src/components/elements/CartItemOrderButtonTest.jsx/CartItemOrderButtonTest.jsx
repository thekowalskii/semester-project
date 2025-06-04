import { useNavigate } from "react-router-dom"


function CartItemOrderButtonTest() {
    const navigate = useNavigate()

    const handleOrder = () => {
        navigate('/cart/order/test-item')
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
