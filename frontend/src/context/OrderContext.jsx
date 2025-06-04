import { createContext, useState } from 'react'

export const OrderContext = createContext()

export const OrderContextProvider = ({ children }) => {
    const [ image, setImage ] = useState(null)
    const [ title, setTitle ] = useState('Title')
    const [ price, setPrice ] = useState('Price')
    const [ phoneNumber, setPhoneNumber ] = useState('')
    const [ firstName, setFirstName ] = useState('')
    const [ lastName, setLastName ] = useState('')
    const [ firstNameError, setFirstNameError ] = useState("Invalid first name")
    const [ lastNameError, setLastNameError ] = useState("Invalid last name")
    const [ phoneNumberError, setPhoneNumberError ] = useState("Invalid phone number")
    const [ selectedShipping, setSelectedShipping ] = useState(null)
    const [ selectedShippingConditions, setSelectedShippingConditions ] = useState(null)
	const [ selectedPayment, setSelectedPayment ] = useState(null)

    const changeShippingConditions = function(event) {
        setSelectedShippingConditions(event.target.value)
    }

	return (
		<OrderContext.Provider
			value={{
				image,
				title,
				price,
				phoneNumber,
				setPhoneNumber,
				firstName,
				setFirstName,
				lastName,
				setLastName,
				firstNameError,
				setFirstNameError,
				lastNameError,
				setLastNameError,
				phoneNumberError,
				setPhoneNumberError,
				selectedShipping,
				setSelectedShipping,
				selectedShippingConditions,
				changeShippingConditions,
				setSelectedShippingConditions,
				setSelectedPayment,
				selectedPayment,
				setImage,
				setPrice,
				setTitle
			}}
		>
			{children}
		</OrderContext.Provider>
	)
}
