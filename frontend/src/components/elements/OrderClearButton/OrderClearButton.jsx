import { useContext } from 'react'

import ClearButton from '../ClearButton/ClearButton'

import { OrderContext } from '../../../context/OrderContext'

import './OrderClearButton.css'


function OrderClearButton() {

    const {
			setPhoneNumber,
			setFirstName,
			setLastName,
			setSelectedShippingConditions,
			setSelectedShipping,
			setSelectedPayment,
		} = useContext(OrderContext)

    function clear() {
        setPhoneNumber('')
        setFirstName('')
        setLastName('')

        setSelectedShippingConditions(null)
        setSelectedShipping(null)

        setSelectedPayment(null)
    }

	return (
		<>
			<ClearButton clearFunction={clear} label='Clear all options' />
		</>
	)
}


export default OrderClearButton
