import { useContext, useEffect, useState } from 'react'
import { OrderContext } from '../../../context/OrderContext'


function NovaShipping() {

    const { selectedShippingConditions, changeShippingConditions } = useContext(OrderContext)

	const [ localities, setLocalities ] = useState([])

	useEffect(() => {

	}, [])
    
    return (
			<div>
				<h3>Shipping conditions</h3>
				<div className='shipping-radio'>
					<label for='nova-department'>Department</label>
					<input
						type='radio'
						id='nova-department'
						name='nova-shipping-conditions'
						value='nova-department'
						checked={selectedShippingConditions === 'nova-department'}
						onChange={changeShippingConditions}
					/>
				</div>
				<div className='shipping-radio'>
					<label for='nova-courier'>Courier</label>
					<input
						type='radio'
						id='nova-courier'
						name='nova-shipping-conditions'
						value='nova-courier'
						checked={selectedShippingConditions === 'nova-courier'}
						onChange={changeShippingConditions}
					/>
				</div>
				<div className='shipping-radio'>
					<label for='nova-parcel-locker'>Parcel locker</label>
					<input
						type='radio'
						id='nova-parcel-locker'
						name='nova-shipping-conditions'
						value='nova-parcel-locker'
						checked={selectedShippingConditions === 'nova-parcel-locker'}
						onChange={changeShippingConditions}
					/>
				</div>
			</div>
		)
}


export default NovaShipping
