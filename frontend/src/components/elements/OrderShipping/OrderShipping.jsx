import { useContext, useEffect } from 'react'
import { OrderContext } from '../../../context/OrderContext'
import NovaShipping from '../NovaShipping/NovaShipping'
import MeestShipping from '../MeestShipping/MeestShipping'
import UkrShipping from '../UkrShipping/UkrShipping'


export default function OrderShipping() {

    const { selectedShipping, setSelectedShipping, setSelectedShippingConditions } = useContext(OrderContext)

    function changeShipping(event) {
        setSelectedShippingConditions(null)
        setSelectedShipping(event.target.value)
    }

	function clear() {
		setSelectedShippingConditions(null)
		setSelectedShipping(null)
	}

	return (
		<div className='order-form-item'>
			<h2>Shipping</h2>
			<div className='order-radio'>
				<label for='nova'>Nova poshta</label>
				<input
					type='radio'
					id='nova'
					name='shipping'
					value='nova'
					checked={selectedShipping === 'nova'}
					onChange={changeShipping}
				/>
				{selectedShipping === 'nova' && <NovaShipping />}
			</div>
			<div className='order-radio'>
				<label for='ukr'>UKR poshta</label>
				<input
					type='radio'
					id='ukr'
					name='shipping'
					value='ukr'
					checked={selectedShipping === 'ukr'}
					onChange={changeShipping}
				/>
				{selectedShipping === 'ukr' && <UkrShipping />}
			</div>
			<div className='order-radio'>
				<label for='meest'>Meest poshta</label>
				<input
					type='radio'
					id='meest'
					name='shipping'
					value='meest'
					checked={selectedShipping === 'meest'}
					onChange={changeShipping}
				/>
				{selectedShipping === 'meest' && <MeestShipping />}
			</div>
			<button 
			className='clear-button'
			onClick={clear}>
			Clear shipping options</button>
		</div>
	)
}
