import './SearchArea.css'


function SearchArea({ data, valueName }) {

    return (
        <div className="search-area">
            <ul>
                {/* <li>{data.length}</li> */}
                {data.length > 0 ? data.map((item, index) => (
                    <li className="search-suggest" key={item.id}>{item[valueName]}</li>
                )) :
                <li key='#'>No results found</li>}
            </ul>
        </div>
    ) 
}


export default SearchArea
