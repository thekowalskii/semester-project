import { useContext } from 'react'

import ClearButton from '../ClearButton/ClearButton'

import { OrderContext } from '../../../context/OrderContext'

import './OrderPayment.css'


function OrderPayment() {
	const { selectedPayment, setSelectedPayment } = useContext(OrderContext)

	function changePayment(event) {
		setSelectedPayment(event.target.value)
	}

	function clear() {
		setSelectedPayment(null)
	}

	return (
		<div className='order-form-item'>
			<h2>Payment</h2>
			<div className='order-radio'>
				<label htmlFor='payment-card'>Card payment</label>
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
				<label htmlFor='payment-delivery'>Cash on delivery</label>
				<input
					type='radio'
					id='payment-delivery'
					name='payment'
					value='payment-delivery'
					checked={selectedPayment === 'payment-delivery'}
					onChange={changePayment}
				/>
			</div>
			<ClearButton clearFunction={clear} label='Clear payment methods' />
		</div>
	)
}


export default OrderPayment
