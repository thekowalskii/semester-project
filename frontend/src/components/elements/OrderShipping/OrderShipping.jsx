import { useContext, useEffect } from 'react'
import { OrderContext } from '../../../context/OrderContext'


export default function OrderShipping() {

    const { selectedShipping, setSelectedShipping } = useContext(OrderContext)

    function changeShipping(event) {
        setSelectedShipping(event.target.value)
    }

	return (
		<div className='order-form-item'>
			<div className='order-radio'>
				<label for='nova'>Nova poshta</label>
				<input
					type='radio'
					id='nova'
					name='nova'
					value='nova'
					checked={selectedShipping === 'nova'}
					onChange={changeShipping}
				/>
			</div>
			<div className='order-radio'>
				<label for='ukr'>UKR poshta</label>
				<input
					type='radio'
					id='ukr'
					name='ukr'
					value='ukr'
					checked={selectedShipping === 'ukr'}
					onChange={changeShipping}
				/>
			</div>
			<div className='order-radio'>
				<label for='meest'>Meest poshta</label>
				<input
					type='radio'
					id='meest'
					name='meest'
					value='meest'
					checked={selectedShipping === 'meest'}
					onChange={changeShipping}
				/>
			</div>
		</div>
	)
}
