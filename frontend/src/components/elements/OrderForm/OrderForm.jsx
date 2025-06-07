import OrderContact from "../OrderContact/OrderContact"
import OrderShipping from "../OrderShipping/OrderShipping"
import OrderPayment from '../../elements/OrderPayment/OrderPayment'
import OrderClearButton from "../OrderClearButton/OrderClearButton"



export default function OrderForm() {


    return (
			<div className='order-form'>
                <OrderContact />
                <OrderShipping />

                <OrderPayment />
                <OrderClearButton />
			</div>
		)

}
