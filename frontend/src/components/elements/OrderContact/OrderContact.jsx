import { useContext, useEffect } from 'react'
import { OrderContext } from "../../../context/OrderContext"


export default function OrderContact() {

    const { phoneNumber, setPhoneNumber, firstName, setFirstName, lastName, setLastName,
        firstNameError, setFirstNameError, lastNameError, setLastNameError, phoneNumberError, setPhoneNumberError
     } = useContext(OrderContext)

    const changePhoneNumber = (event) => {
        setPhoneNumber(() => event.target.value)
    }
    const changeFirstName = (event) => {
        setFirstName(() => event.target.value)
    }
    const changeLastName = (event) => {
        setLastName (() => event.target.value)
    }

    useEffect(() => {
        const regexPattern = /^(\+?\d{1,3}[- ]?)?(\(?\d{2,4}\)?[- ]?)?\d{3,4}[- ]?\d{4}$/
        let isValidNumber = regexPattern.test(phoneNumber)
        if (!isValidNumber) {
            setPhoneNumberError('Invalid phone number')
        } else {
            setPhoneNumberError('')
        }
    }, [phoneNumber])

    useEffect(() => {
        const regexPatter = /^\p{L}+$/u
        let isValidFirstName = regexPatter.test(firstName)
        if (!isValidFirstName || firstName.length < 1 || firstName.length > 30) {
            setFirstNameError('Invalid first name')
        } else {
            setFirstNameError('')
        }
        }, [firstName])

    useEffect(() => {
        const regexPatter = /^\p{L}+$/u
        let isValidLastName = regexPatter.test(lastName)
        if (!isValidLastName || lastName.length < 1 || lastName.length > 30) {
                    setLastNameError('Invalid last name')
                } else {
                    setLastNameError('')
                }
    }, [lastName])

    return (
            <div className='order-form-item'>
                <h2>Contact data</h2>
                <div>
                    <div className='order-input'>
                        <input
                            id='phone-number'
                            onChange={changePhoneNumber}
                            value={phoneNumber}
                            placeholder='Enter your phone number'
                            className='order-input-field'
                        />
                        <p className='error-field'>{phoneNumberError}</p>
                    </div>
                    <div className='order-input'>
                        <label for='phone-number'>Phone number</label>

                        <label for='first-name'>First name</label>
                        <input
                            id='first-name'
                            onChange={changeFirstName}
                            value={firstName}
                            placeholder='Enter your first name'
                            className='order-input-field'
                        />
                        <p className='error-field'>{firstNameError}</p>
                    </div>
                    <div className='order-input'>
                        <label for='last-name'>Last name</label>
                        <input
                            id='last-name'
                            onChange={changeLastName}
                            value={lastName}
                            placeholder='Enter your last name'
                            className='order-input-field'
                        />
                        <p className='error-field'>{lastNameError}</p>
                    </div>
                </div>
            </div>
        )

}
