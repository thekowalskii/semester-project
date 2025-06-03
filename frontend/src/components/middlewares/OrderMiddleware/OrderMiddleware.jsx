import { Outlet } from "react-router-dom";
import { OrderContextProvider } from "../../../context/OrderContext";


export default function OrderMiddleware() {
    
    return (
        <>
            <OrderContextProvider>
                <Outlet />
            </OrderContextProvider>
        </>
    )
}
