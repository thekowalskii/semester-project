import { Outlet } from "react-router-dom";

import { OrderContextProvider } from "../../../context/OrderContext";


function OrderMiddleware() {
    
    return (
        <>
            <OrderContextProvider>
                <Outlet />
            </OrderContextProvider>
        </>
    )
}


export default OrderMiddleware
