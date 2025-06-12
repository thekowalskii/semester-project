import { useContext } from "react"

import { OrderContext } from "../../../context/OrderContext"

import './Shipping.css'


function Shipping({ id, label, shippingElement }) {
    
    const {
            selectedShipping,
            setSelectedShipping,
            setSelectedShippingConditions
        } = useContext(OrderContext)

    function changeShipping(event) {
        setSelectedShippingConditions(null)
        setSelectedShipping(event.target.value)
    }

    return (
			<div className={`order-radio`}>
				<label htmlFor={id}>{label}</label>
				<input
					type='radio'
					id={id}
					name='shipping'
					value={id}
					checked={selectedShipping === id}
					onChange={changeShipping}
				/>
				{selectedShipping === id && shippingElement}
			</div>
		)

}


export default Shipping
