import { useEffect, useState } from "react"
import Cookies from 'js-cookie'

// import API_KEY from '../config'
import api from "../api"
import Header from "./Header"
import Product from "./Product"
import Painting from "./Painting"
import Perfume from "./Perfume"
import ProductModal from "./ProductModal"

import CartItemTest from '../components/elements/CartItemTest/CartItemTest'


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
    const [selectedProduct, setSelectedProduct] = useState(null);
    const [selectedProductType, setSelectedProductType] = useState(null);
    const [availableScroll, setAvailableScroll] = useState(true);
    const [selectedProductImageUrl, setSelectedProductImageUrl] = useState(null);

    const [paintings, setPaintings] = useState([])
    const [perfumes, setPerfumes] = useState([])
    const [products, setProducts] = useState([])

    const [loading, setLoading] = useState(false)
    const [token, setToken] = useState(checkToken())
    const [email, setEmail] = useState(checkEmail())
    const [cart, setCart] = useState(checkCart())

    // the function below is used to do three actions at one moment: 
    // 1. set selected product
    // 2. set its type (painting/perfume/product)
    // 3. allow/prohibit page scrolling
    //
    // all this is used when user open/close the modal window with 
    // a product information
    //
    // this approach is more confortable, since we need to call it
    // in our components, it it wouldn't be that comfortable to do
    // all this in each place we need to

    function setSelectedProduct_(product, type, allowScroll, imgUrl){
        setSelectedProduct(product);
        setSelectedProductType(type);
        setAvailableScroll(allowScroll);
        setSelectedProductImageUrl(imgUrl);

        if (allowScroll === false) {
            // prohibit to scroll the page (the modal window is closed)
            document.body.style.overflow = 'hidden'
        } else {
            // allow to scroll the page (the modal window is opened)
            document.body.style.overflow = 'auto'
        }
    }

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
                    {paintings.length == 0 ? <h3>No paintings provided</h3> :  paintings.map((element, index) => (
                        <>
                            <Painting item={element} onClick={setSelectedProduct_} key={index}/>
                        </>
                    ))}
                </section>

                <h2>Perfumes</h2>
                <section>
                    {perfumes.length == 0 ? <h3>No perfumes provided</h3> : perfumes.map((element, index) => (
                        <>
                            <Perfume item={element} onClick={setSelectedProduct_} key={index}/>
                        </>
                    ))}
                </section>

                <h2>Products</h2>
                <section>
                    {products.length == 0 ? <h3>No products provided</h3> : products.map((element, index) => (
                        <>
                            <Product item={element} onClick={setSelectedProduct_} key={index}/>
                        </>
                    ))}
                </section>

                <ProductModal 
                    product={selectedProduct} 
                    onClose={() => {
                        setSelectedProduct_(null, null, true);
                    }}
                    type={selectedProductType} 
                    imgUrl={selectedProductImageUrl} />
            </main>

            
            <CartItemTest />

        </>
    )
}


export default Home
