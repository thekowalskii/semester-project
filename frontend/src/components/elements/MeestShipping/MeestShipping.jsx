import { useContext, useEffect } from 'react'
import { OrderContext } from '../../../context/OrderContext'


function MeestShipping() {

    const { selectedShippingConditions, changeShippingConditions } = useContext(OrderContext)

	return (
		<div>
			<h3>Shipping conditions</h3>
			<div className='shipping-radio'>
				<label for='meest-department'>Department</label>
				<input
					type='radio'
					id='meest-department'
					name='meest-shipping-conditions'
					value='meest-department'
					checked={selectedShippingConditions === 'meest-department'}
					onChange={changeShippingConditions}
				/>
			</div>
			<div className='shipping-radio'>
				<label for='meest-courier'>Courier</label>
				<input
					type='radio'
					id='meest-courier'
					name='meest-shipping-conditions'
					value='meest-courier'
					checked={selectedShippingConditions === 'meest-courier'}
					onChange={changeShippingConditions}
				/>
			</div>
			<div className='shipping-radio'>
				<label for='meest-parcel-locker'>Parcel locker</label>
				<input
					type='radio'
					id='meest-parcel-locker'
					name='meest-shipping-conditions'
					value='meest-parcel-locker'
					checked={selectedShippingConditions === 'meest-parcel-locker'}
					onChange={changeShippingConditions}
				/>
			</div>
		</div>
	)
}


export default MeestShipping

