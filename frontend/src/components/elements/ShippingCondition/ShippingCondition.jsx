import { useContext, useEffect } from "react"

import { OrderContext } from "../../../context/OrderContext"
import { BaseContext } from '../../../context/BaseContext'

import SearchSystem from "../SearchSystem/SearchSystem"

import './ShippingCondition.css'


function ShippingCondition({ id, dataDepartment, dataCourier, valueName, filter }) {

    const {
			selectedShippingConditions,
			setSelectedShippingConditions,
			shippingLocality,
			setShippingLocality,
		} = useContext(OrderContext)
	const { setSearchItem, setSearchFilteredElements } = useContext(BaseContext)

    const changeShippingConditions = function (event) {
        setSelectedShippingConditions(event.target.value)
    }

	useEffect(() => {
		setShippingLocality('')
		setSearchItem('')
		setSearchFilteredElements([])
	}, [selectedShippingConditions])

	return (
		<div>
			<div className='shipping'>
				<div className='shipping-radio'>
					<label htmlFor={`${id}-department`}>Department</label>
					<input
						type='radio'
						id={`${id}-department`}
						name={`${id}-shipping-conditions`}
						value={`${id}-department`}
						checked={selectedShippingConditions === `${id}-department`}
						onChange={changeShippingConditions}
					/>
				</div>
				<div className='shipping-radio'>
					<label htmlFor={`${id}-courier`}>Courier</label>
					<input
						type='radio'
						id={`${id}-courier`}
						name={`${id}-shipping-conditions`}
						value={`${id}-courier`}
						checked={selectedShippingConditions === `${id}-courier`}
						onChange={changeShippingConditions}
					/>
				</div>
			</div>
			{selectedShippingConditions === `${id}-department` ? (
				<SearchSystem
					itemName='locality'
					itemId={`${id}-department`}
					label='Locality'
					data={dataDepartment}
					value={shippingLocality}
					setValue={setShippingLocality}
					valueName={valueName}
					filterFunction={filter}
				/>
			) : selectedShippingConditions === `${id}-courier` ? (
				<SearchSystem
					itemName='locality'
					itemId={`${id}-department`}
					label='Locality'
					data={dataCourier}
					value={shippingLocality}
					setValue={setShippingLocality}
					valueName={valueName}
					filterFunction={filter}
				/>
			) : null}
		</div>
	)
}


export default ShippingCondition
