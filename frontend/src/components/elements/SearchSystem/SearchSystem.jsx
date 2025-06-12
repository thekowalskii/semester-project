import { useEffect, useContext } from 'react'

import SearchArea from '../SearchArea/SearchArea'

import { BaseContext } from '../../../context/BaseContext'

import './SearchSystem.css'


function SearchSystem({
	itemName,
	itemId,
	label,
	data,
	value,
	setValue,
	valueName,
	filterFunction,
}) {
	// const [  ] = useState([])
	// const [ searchItem, setSearchItem ] = useState('')
	const {
		searchItem,
		setSearchItem,
		searchFilteredElements,
		setSearchFilteredElements,
	} = useContext(BaseContext)

	const changeSearchItem = event => {
		setSearchItem(event.target.value)
	}

	useEffect(() => {
		if (!searchItem) {
			return
		}
		setSearchFilteredElements(filterFunction(data))
	}, [searchItem])

	return (
		<div className='search'>
			<div className='search-selected-item'>
				{value ? value : `No ${itemName} selected`}
			</div>
			<label htmlFor={`search-item-${itemId}`}>{label}</label>
			<input
				type='text'
				id={`search-item-${itemId}`}
				placeholder={`Specify the ${itemName}`}
				value={searchItem}
				onChange={changeSearchItem}
			/>
			<SearchArea
				data={searchItem ? searchFilteredElements : []}
				valueName={valueName}
			/>
		</div>
	)
}


export default SearchSystem
