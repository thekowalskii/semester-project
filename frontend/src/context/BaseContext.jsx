import { createContext, useState } from 'react'

export const BaseContext = createContext()

export const BaseContextProvider = ({ children }) => {
    const [ isCached, setIsCached ] = useState(false)

	return (
		<BaseContext.Provider
			value={
                isCached
            }
		>
			{children}
		</BaseContext.Provider>
	)
}
