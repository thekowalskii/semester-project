import { useContext } from 'react'

import ShippingCondition from '../ShippingCondition/ShippingCondition'

import { OrderContext } from '../../../context/OrderContext'

import './UkrShipping.css'


function UkrShipping() {

    const { selectedShippingConditions, changeShippingConditions } = useContext(OrderContext)

	return (
		<>
			<ShippingCondition
				id='ukr'
			/>
		</>
	)
}


export default UkrShipping
