import { useState, useEffect } from "react";

import api from "../../api";
import Cookies from 'js-cookie';

import CartItem from "./CartItem";


function checkEmail() {
    let email = Cookies.get('email')

    return email
}


function Cart({ cart }) {
    const [loading, setLoading] = useState(true)
    const [cartInfo, setCartInfo] = useState()


    useEffect(() => {
        const getRes = async () => {
            const data = await api.get(
                `/carts/cart_info?cart_id=${cart}`)
                
            .then((response) => {
                console.log(response.data)
                setCartInfo(response.data)
            })
            setLoading(false);
        };
    
        getRes();
    }, []);
    if (loading) return <div>Loading...</div>;


    return (
        <>
            <h1>My Cart</h1>

            <h2>Total Price: {cartInfo.total_price}₴</h2>

            {/* <p>{ Cart['total_price'] }</p> */}

            <main className="products-container">
                {cartInfo.items.map((element, index) => (
                    <>
                        <CartItem item={element} />
                    </>
                ))}
            </main>
        </>
    )
}


export default Cart
