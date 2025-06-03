import OrderContact from "../OrderContact/OrderContact"
import OrderShipping from "../OrderShipping/OrderShipping"


export default function OrderForm() {


    return (
			<div className='order-form'>
                <OrderContact />
                <OrderShipping />
			</div>
		)

}
