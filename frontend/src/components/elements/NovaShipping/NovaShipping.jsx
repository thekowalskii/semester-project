import { useContext, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'

import ShippingCondition from '../ShippingCondition/ShippingCondition'

import { OrderContext } from '../../../context/OrderContext'
import { BaseContext } from '../../../context/BaseContext'

import api from '../../../api'

import './NovaShipping.css'


function NovaShipping() {
	const navigate = useNavigate()
    const { setNovaDepartment, setNovaCourier, novaDepartment, novaCourier } = useContext(OrderContext)
	const { searchItem, setSearchItem } = useContext(BaseContext)

	function filter(data) {
		// const cleanData = data.filter((element => element.department === true))
		const cleanData = data.filter(element => element.title.toLowerCase().startsWith(searchItem.toLowerCase()))
		return cleanData
	}

	// function filterCourier(data) {
	// 	// const cleanData = data.filter(element => element.courier === true)
	// 	const cleanData = data.filter(element => element.courier === true)
	// 	return cleanData
	// }

	useEffect(() => {
		const fetchData = async () => {
			const url = '/nova/get/localities/'
			try {
				let response1 = await api.get(`${url}department`)
				let response2 = await api.get(`${url}courier`)
				setNovaDepartment(response1.data)
				setNovaCourier(response2.data)
				// return true
			} catch (error) {
				// return false
				// console.log(error)
				navigate('/')
			}
		}

		fetchData()

		// let id

		// const fetching = async () => {
		// 	const response = fetchData()
		// 	if (!response) {
		// 		id = setInterval(async () => {
		// 			const result = await fetchData()
		// 			if (!result) {
		// 				clearInterval(id)
		// 			}
		// 		})
		// 	}
		// }

		// fetching()

		// return () => {
		// 	clearInterval(id)
		// }
	}, [])

    return (
			<>
				<ShippingCondition
					id='nova'
					dataDepartment={novaDepartment}
					dataCourier={novaCourier}
					valueName='fullTitle'
					filter={filter}
				/>
			</>
		)
}


export default NovaShipping


{
	/* <div className='shipping-radio'>
	<label for='nova-parcel-locker'>Parcel locker</label>
	<input
		type='radio'
		id='nova-parcel-locker'
		name='nova-shipping-conditions'
		value='nova-parcel-locker'
		checked={selectedShippingConditions === 'nova-parcel-locker'}
		onChange={changeShippingConditions}
	/>
</div> */
}
