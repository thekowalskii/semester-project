import { useContext, useEffect } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import { OrderContext } from "../../../context/OrderContext"
import api from '../../../api'


export default function OrderItem() {

    const navigate = useNavigate()
    const { itemId } = useParams()
    const { image, title, price, setTitle, setImage, } = useContext(OrderContext)

    useEffect(() => {
        const fetchItem = async () => {
            try {
                let response = await api.get(`${category}/${itemId}`)
                let itemData = response.data
                setTitle(itemData.title)
                setPrice(itemData.price)
            } catch (error) {
                // navigate('/item-does-not-exists')
            }
        }
        const fetchItemImage = async () => {
            try {
                let response = await api.get(`${category}/get_one?title=${title}`, {
                    responseType: 'blob'
                })
                const url = URL.createObjectURL(response.data);
                setImage(url)
            } catch (error) {
                setImage("data:image/jpeg;base64,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")
            }
        }
        fetchItem()
        fetchItemImage()
    }, [])

    return (
			<div className='order-item'>
				<img src={image} alt="Image item"/>
                <h2>{title}</h2>
                <h2>Price: {price}</h2>
			</div>
		)
}
