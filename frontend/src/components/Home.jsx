import { useEffect, useState } from 'react'

import api from '../../api'
import Header from "./Header"
import Product from "./Product"
import { data } from 'react-router-dom'


const getPhotoTitles = async () => {
    return await api.get('/paintings/get_all')
        .then((response) => {return response})
}


function Home() {
    const [paintings, setPaintings] = useState([])
    const [loading, setLoading] = useState(true)

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
                {paintings.data.map((title, index) => (
                    <>
                        <Product img_title={title} key={index}/>
                    </>
                ))}

            </main>
        </>
    )
}


export default Home
