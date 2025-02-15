import { useEffect, useState } from "react"

import Header from "./Header"
import Product from "./Product"
import api from "../../api"


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
                {paintings.data.map((element, index) => (
                    <>
                        <Product img_obj={element} key={index}/>
                    </>
                ))}
            </main>
        </>
    )
}


export default Home
