import { useContext, useEffect } from 'react'
import { OrderContext } from '../../../context/OrderContext'


export default function OrderClearButton() {

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
			<button className='clear-button' onClick={clear}>
				Clear all
			</button>
		</>
	)
}
