import { useEffect, useState } from 'react';

import api from '../../api'


function Product({ item }) {
    const url = 'http://127.0.0.1:8000/paintings/get_one?title=' + item.title_wos

    return (
        <div className='product-container' key={item.title + '_pc'}>
            <div className="image" key={item.title + '_image'} style={
                {
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${url})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }
            }></div>
            
            <div className="info" key={item.title + '_info'}>
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

export default Product
