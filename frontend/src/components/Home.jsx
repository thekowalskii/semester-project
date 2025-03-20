import { useEffect, useState } from "react"

import Cookies from 'js-cookie'

import api from "../../api"

import Header from "./Header"
import Product from "./Product"
import Painting from "./Painting"
import Perfume from "./Perfume"


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
    const [perfumes, setPerfumes] = useState([])
    const [products, setProducts] = useState([])

    const [loading, setLoading] = useState(false)
    const [token, setToken] = useState(checkToken())
    const [email, setEmail] = useState(checkEmail())
    const [cart, setCart] = useState(checkCart())


    useEffect(() => {
        const getPaintings = async () => {
            const data = await api.get('/paintings/get_all')
                .then((response) => {
                    setPaintings(response.data)
                })
            setLoading(false);
        };

        const getPerfumes = async () => {
            const data = await api.get('/perfumes/get_all')
                .then((response) => {
                    setPerfumes(response.data)
                })
            setLoading(false);
        };

        const getProducts = async () => {
            const data = await api.get('/products/get_all')
                .then((response) => {
                    setProducts(response.data)
                })
            setLoading(false);
        };

        getPaintings();
        getPerfumes();
        getProducts();
    }, []);

    if (loading) return <div>Loading...</div>;

    return (
        <>
            <Header />


            <main>
                <h2>Paintings</h2>
                <section>
                    {paintings.length == 0 ? <h6>No paintings provided</h6> :  paintings.map((element, index) => (
                        <>
                            <Painting item={element} key={index}/>
                        </>
                    ))}
                </section>

                <h2>Perfumes</h2>
                <section>
                    {perfumes.length == 0 ? <h1>No perfumes provided</h1> : perfumes.map((element, index) => (
                        <>
                            <Perfume item={element} key={index}/>
                        </>
                    ))}
                </section>

                <h2>Products</h2>
                <section>
                    {products.length == 0 ? <h1>No products provided</h1> : products.map((element, index) => (
                        <>
                            <Product item={element} key={index}/>
                        </>
                    ))}
                </section>
            </main>
        </>
    )
}


export default Home
