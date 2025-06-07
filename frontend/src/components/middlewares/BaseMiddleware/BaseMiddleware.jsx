import { Outlet } from 'react-router-dom'
import Footer from '../../elements/Footer/Footer'
import Header from '../../Header'
import { BaseContextProvider } from '../../../context/BaseContext'


function BaseMiddleware() {
    
    return (
        <BaseContextProvider>
            <Header />
            <Outlet />
            <Footer />
        </BaseContextProvider>
    )
}


export default BaseMiddleware
