import { useEffect, useState } from 'react';

import api from '../../api'


function Product({ img_title }) {
    const url = 'http://127.0.0.1:8000/paintings/get_photo?title=' + img_title

    const [imageUrl, setImageUrl] = useState('');
    const [productInfo, setProductInfo] = useState();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchImage = async () => {
            try {
                const response = await fetch('http://127.0.0.1:8000/paintings/get_photo?title=' + img_title)
                setImageUrl(response.url)
            } catch (error) {
                console.error('Error fetching image:', error)
            }
        }

        const fetchData = async () => {
            const data = await api.get('http://127.0.0.1:8000/paintings/get_one?title=' + img_title)
                .then((response) => {
                    setProductInfo(response)
                    setLoading(false)
                })
        }

        fetchImage();
        fetchData();
    }, []);

    if (loading) return <div style={{ textAlign: 'center' }}>Loading...</div>;

    return (
        <div className='product-container'>
            <div className="image" key={img_title} style={
                {
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${imageUrl})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }
            }></div>
            
            <div className="info">
                <h3 key={img_title + '_t'}>{productInfo.data.title}</h3>
                <h3 key={img_title + '_p'}>Price: {productInfo.data.price}₴</h3>
                <p key={img_title + '_d'}>
                    {productInfo.data.description}
                    <br key={img_title + '_d_br'}/>
                    {productInfo.data.available}
                </p>
            </div>
        </div>
    )
}

export default Product
