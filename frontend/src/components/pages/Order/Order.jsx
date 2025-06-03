import { useParams } from "react-router-dom"
import OrderForm from "../../elements/OrderForm/OrderForm";
import OrderItem from "../../elements/OrderItem/OrderItem";


export default function Order() {
    const { item_id } = useParams();

    return (
        <>
          <h1>Order</h1>
          <div className="order">
            <OrderForm />
            <OrderItem />
          </div>
        </>
    )
}
