import { useContext } from 'react'

import NovaShipping from '../NovaShipping/NovaShipping'
import MeestShipping from '../MeestShipping/MeestShipping'
import UkrShipping from '../UkrShipping/UkrShipping'
import Shipping from '../Shipping/Shipping'
import ClearButton from '../ClearButton/ClearButton'

import { OrderContext } from '../../../context/OrderContext'

import './OrderShipping.css'


function OrderShipping() {

    const {
			selectedShipping,
			setSelectedShipping,
			setSelectedShippingConditions,
			setNovaCourier,
			setNovaDepartment
		} = useContext(OrderContext)

	function clear() {
		setSelectedShippingConditions(null)
		setSelectedShipping(null)
	}

	return (
		<div className='order-form-item'>
			<h2>Shipping</h2>
			<div className='order-shipping'>
				<Shipping
					id='nova'
					label='Nova Post'
					shippingElement=<NovaShipping />
				/>
				<Shipping id='ukr' label='Ukr Post' shippingElement=<UkrShipping /> />
				<Shipping
					id='meest'
					label='Meest Ukraine Post'
					shippingElement=<MeestShipping />
				/>
			</div>
			<ClearButton clearFunction={clear} label='Clear shipping options' />
		</div>
	)
}


export default OrderShipping
