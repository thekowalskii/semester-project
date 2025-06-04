import { useContext, useEffect } from 'react'
import { OrderContext } from '../../../context/OrderContext'


function UkrShipping() {

    const { selectedShippingConditions, changeShippingConditions } = useContext(OrderContext)

	return (
		<div>
			<h3>Shipping conditions</h3>
			<div className='shipping-radio'>
				<label for='ukr-department'>Department</label>
				<input
					type='radio'
					id='ukr-department'
					name='ukr-shipping-conditions'
					value='ukr-department'
					checked={selectedShippingConditions === 'ukr-department'}
					onChange={changeShippingConditions}
				/>
			</div>
			<div className='shipping-radio'>
				<label for='ukr-courier'>Courier</label>
				<input
					type='radio'
					id='ukr-courier'
					name='ukr-shipping-conditions'
					value='ukr-courier'
					checked={selectedShippingConditions === 'ukr-courier'}
					onChange={changeShippingConditions}
				/>
			</div>
			<div className='shipping-radio'>
				<label for='ukr-parcel-locker'>Parcel locker</label>
				<input
					type='radio'
					id='ukr-parcel-locker'
					name='ukr-shipping-conditions'
					value='ukr-parcel-locker'
					checked={selectedShippingConditions === 'ukr-parcel-locker'}
					onChange={changeShippingConditions}
				/>
			</div>
		</div>
	)
}


export default UkrShipping
