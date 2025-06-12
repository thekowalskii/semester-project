// import { useParams } from "react-router-dom"

import OrderForm from "../../elements/OrderForm/OrderForm";
import OrderItem from "../../elements/OrderItem/OrderItem";

import './Order.css'


function Order() {
    // const { item_id } = useParams();

    function handleSubmit(event) {
		event.preventDefault()

    }

    return (
			<>
				<h1>Order</h1>
				<form className='order' onSubmit={handleSubmit}>
						<OrderForm />
						<OrderItem />
				</form>
			</>
		)
}


export default Order
