import { useEffect, useState } from 'react';

import api from '../api'
import detailsAnimation from './detailsAnimation';


function Painting({ item }) {
    const [imageUrl, setImageUrl] = useState("");

    const img_url = 'http://127.0.0.1:8000/paintings/get_one?title=' + item.title_wos

    useEffect(() => {
        api.get(img_url, {
            responseType: 'blob'
        })
        .then(response => {
            const url = URL.createObjectURL(response.data);
            setImageUrl(url);
        })
        .catch(error => console.error('Error fetching image:', error));
    }, []);

    return (
        <div className='product-container' key={item.title + '_pc'} onClick={() => {detailsAnimation(item); }} >
            {/* <div className='image' key={item.title + '_image'} style={
                {
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${img_url})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }
            }></div> */}

            <img src={imageUrl} alt=""  className='image' style={{
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${img_url})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }} />
            
            <div className='info' key={item.title + '_info'}>
                <h3 key={item.title + '_t'}>{item.title}</h3>
                <h3 key={item.title + '_p'}>Price: {item.price}₴</h3>
                <p key={item.title + '_d'}>
                    {item.description}
                    <br key={item.title + '_d_br'}/>
                    {item.available}
                </p>
            </div>
        </div>
    )
}

export default Painting