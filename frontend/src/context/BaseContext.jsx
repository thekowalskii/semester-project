import { createContext, useState, useEffect } from 'react'

import api from '../api'


const BaseContext = createContext()


const BaseContextProvider = ({ children }) => {
    const [ isNovaCached, setIsNovaCached ] = useState(false)
	const [ searchItem, setSearchItem ] = useState(null)
	const [ searchFilteredElements, setSearchFilteredElements ] = useState([])

	useEffect(() => {
		const cacheLocalitiesNova = async () => {
			try {
				const response = await api.post('/nova/cache/localities/all')
				setIsNovaCached(true)
			} catch (error) {
				setIsNovaCached(true)
			}
		}
		const isNovaCachedRequest = async () => {
			try {
				const response = await api.get('/nova/get/cache/localities')
				const data = response.data
				if (data.isCached) {
					setIsNovaCached(true)
				} else {
					cacheLocalitiesNova()
				}
			} catch (error) {console.log(error)}
		}
		if (!isNovaCached) {
			isNovaCachedRequest()
		}
	}, [])

	return (
		<BaseContext.Provider
			value={{
				isNovaCached,
				searchItem,
				setSearchItem,
				searchFilteredElements,
				setSearchFilteredElements
			}}
		>
			{children}
		</BaseContext.Provider>
	)
}


export { BaseContext, BaseContextProvider };
