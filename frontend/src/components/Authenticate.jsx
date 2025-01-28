// import { send } from "vite";
import api from "../../api";

import Cookies from 'js-cookie';


function AuthenticateForm() {
    const sendData = async (email, password) => {
        const data = {
            email: email,
            password: password
        }

        console.log(data)

        await api.post('/signin', data)
            .then((response) => {
                let token = response.data
                Cookies.set('access_token', token)
            })
            .catch((error) => {
                console.log('Email or password is incorrect')
            }) 
    }

    return (
        <>
        <div>
            <input type="email" id="email" placeholder="Enter your Email" required />
            <label htmlFor="Email">Email</label><br />

            <input type="password" id="password" required placeholder="Enter your password"/>
            <label htmlFor="password">Password</label>

            <button onClick={() => sendData(
                email=document.getElementById('email').value,
                password=document.getElementById('password').value
            )}>Authenticate</button>
        </div>
        </>
    )
}


export default AuthenticateForm
