import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Cookies from 'js-cookie'

import api from '../api'

import AuthenticateForm from './components/Authenticate'


function checkToken() {
  let token = Cookies.get('access_token')

  return token
}


function App() {
  const [token, setToken] = useState(checkToken())

  return (
    <>
      <h1>Hello</h1>
    </>
  )
}


export default App
