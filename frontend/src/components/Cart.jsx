import { useState, useEffect } from "react";

import api from "../api";
import Cookies from 'js-cookie';

import CartItem from "./CartItem";


function checkCart() {
    let cart = Cookies.get('cart_id')

    return cart
}


function Cart() {
    const [loading, setLoading] = useState(true)
    const [cartInfo, setCartInfo] = useState()
    const [cartId, setCartId] = useState(checkCart())


    useEffect(() => {
        const createCart = async () => {
            await api.post('/carts/create')
                .then((response) => {
                    Cookies.set('cart_id', response.data)
                })
            location.reload()
        }

        if (Cookies.get('cart_id') == undefined) {
            createCart()
        }

        const getRes = async () => {
            const data = await api.get(
                `/carts/cart_info?cart_id=${cartId}`)
                
            .then((response) => {
                console.log(response.data)
                setCartInfo(response.data)
            })
            .catch((error) => {
                // createCart()
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

            <main className="products-container">
                {cartInfo.items.length == 0 ? <h2>Your Cart Is Empty</h2> : <></>}

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
