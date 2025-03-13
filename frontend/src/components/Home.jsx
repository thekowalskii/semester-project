import { useEffect, useState } from "react"

import Cookies from 'js-cookie'

import Header from "./Header"
import Product from "./Product"
import api from "../../api"


function checkToken() {
  let token = Cookies.get('access_token')

  return token
}

function checkEmail() {
    let email = Cookies.get('email')
  
    return email
  }

function checkCart() {
    let cart = Cookies.get('cart')

    return cart
}


function Home() {
    const [paintings, setPaintings] = useState([])
    const [loading, setLoading] = useState(true)
    const [token, setToken] = useState(checkToken())
    const [email, setEmail] = useState(checkEmail())
    const [cart, setCart] = useState(checkCart())


    useEffect(() => {
        const getRes = async () => {
            const data = await api.get('/paintings/get_all')
                .then((response) => {
                    setPaintings(response)
                })
            setLoading(false);
        };
    
        getRes();
    }, []);
    if (loading) return <div>Loading...</div>;

    return (
        <>
            <Header />

            <main className="products-container">
                {paintings.data.map((element, index) => (
                    <>
                        <Product item={element} key={index}/>
                    </>
                ))}
            </main>
        </>
    )
}


export default Home
