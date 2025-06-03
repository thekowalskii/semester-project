import { useContext } from 'react'
import { OrderContext } from "../../../context/OrderContext"


export default function OrderItem() {

    const { image, title, price } = useContext(OrderContext)

    return (
			<div className='order-item'>
				<img src={image} alt="Image item"/>
                <h2>{title}</h2>
                <h2>Price: {price}</h2>
			</div>
		)
}
