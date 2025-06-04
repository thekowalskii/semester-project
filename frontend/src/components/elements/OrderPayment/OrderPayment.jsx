import { useContext, useEffect } from 'react'
import { OrderContext } from "../../../context/OrderContext"


export default function OrderPayment() {

    const { selectedPayment, setSelectedPayment } = useContext(OrderContext)

    function changePayment(event) {
        setSelectedPayment(event.target.value)
    }

    return (
			<div className='order-form-item'>
				<h2>Payment</h2>
				<div className='order-radio'>
					<label for='payment-card'>Card payment</label>
					<input
						type='radio'
						id='payment-card'
						name='payment'
						value='payment-card'
						checked={selectedPayment === 'payment-card'}
						onChange={changePayment}
					/>
				</div>
				<div className='order-radio'>
					<label for='payment-delivery'>Cash on delivery</label>
					<input
						type='radio'
						id='payment-delivery'
						name='payment'
						value='payment-delivery'
						checked={selectedPayment === 'payment-delivery'}
						onChange={changePayment}
					/>
				</div>
			</div>
		)
}
