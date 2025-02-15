import { useEffect, useState } from 'react';

import api from '../../api'


function Product({ img_obj }) {
    const url = 'http://127.0.0.1:8000/paintings/get_one?title=' + img_obj.title

    return (
        <div className='product-container' key={img_obj.title + '_pc'}>
            <div className="image" key={img_obj.title + '_image'} style={
                {
                    width: '100%',
                    height: '200px',
                    backgroundImage: `url(${url})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    backgroundRepeat: 'no-repeat'
                }
            }></div>
            
            <div className="info" key={img_obj.title + '_info'}>
                <h3 key={img_obj.title + '_t'}>{img_obj.title}</h3>
                <h3 key={img_obj.title + '_p'}>Price: {img_obj.price}₴</h3>
                <p key={img_obj.title + '_d'}>
                    {img_obj.description}
                    <br key={img_obj.title + '_d_br'}/>
                    {img_obj.available}
                </p>
            </div>
        </div>
    )
}

export default Product
