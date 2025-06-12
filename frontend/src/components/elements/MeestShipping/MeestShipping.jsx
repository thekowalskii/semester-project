import { useContext, useEffect } from 'react'

import ShippingCondition from '../ShippingCondition/ShippingCondition'

import { OrderContext } from '../../../context/OrderContext'

import './MeestShipping.css'


function MeestShipping() {

    const { selectedShippingConditions } = useContext(OrderContext)

	return (
		<>
			<ShippingCondition
				id='meest'
			/>
		</>
	)
}


export default MeestShipping
