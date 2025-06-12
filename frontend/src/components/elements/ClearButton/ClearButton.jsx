import './ClearButton.css'


function ClearButton({ clearFunction, label }) {

    return (
		<>
			<button className='clear-button' onClick={clearFunction}>
				{label}
			</button>
		</>
	)
}


export default ClearButton
