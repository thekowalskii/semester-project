import OrderContact from "../OrderContact/OrderContact"
import OrderShipping from "../OrderShipping/OrderShipping"
import OrderPayment from '../../elements/OrderPayment/OrderPayment'


export default function OrderForm() {


    return (
			<div className='order-form'>
                <OrderContact />
                <OrderShipping />
                <OrderPayment />
			</div>
		)

}
