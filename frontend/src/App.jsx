import { useState } from 'react'
import './App.css'

import Cookies from 'js-cookie'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'

import Header from './components/Header'
import SignIn from './components/SignInForm';
import Home from './components/Home';
import Cart from './components/Cart';
import Order from './components/pages/Order/Order';
import OrderMiddleware from './components/middlewares/OrderMiddleware/OrderMiddleware';
import Error404 from './components/pages/Error404/Error404';
import BaseMiddleware from './components/middlewares/BaseMiddleware/BaseMiddleware'


function checkToken() {
  let token = Cookies.get('access_token')

  return token
}


function checkCart() {
    let cart = Cookies.get('cart')

    return cart
}


function App() {
  const [cart, setCart] = useState(checkCart())

	return (
		<>
			<Router>
				<Routes>
					<Route path='/' element={<BaseMiddleware />}>
						<Route path='' element={<Home />}></Route>
						<Route path='signin' element={<SignIn />}></Route>
						<Route path='cart' element={<Cart cart={cart} />}></Route>
						<Route path='' element={<OrderMiddleware />}>
							<Route path='cart/order/:itemId' element={<Order />} />
						</Route>
						<Route path='*' element={<Error404 />} />
					</Route>
				</Routes>
			</Router>
		</>
	)
}


export default App
