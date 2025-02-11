// import { send } from "vite";
import api from "../../api";

import Cookies from 'js-cookie';


function SignIn() {
    const sendData = async (email, password) => {
        const data = {
            email: email,
            password: password
        }

        await api.post('/signin', data)
            .then((response) => {
                let token = response.data
                Cookies.set('access_token', token)
                location.reload()
            })

            .catch((error) => {
                let statusSpan = document.getElementById('status-span')
                let errorText = error.response.data.detail
                statusSpan.innerHTML = errorText
                console.log(errorText)
            })
    }

    return (
        <>
        <div style={{backgroundColor: '#ffe0b2'}} className="signin-form">
            <h2>Sign In</h2>

            <input type="email" id="email" placeholder="Enter your Email" required />
            <label htmlFor="Email">Email</label><br />

            <input type="password" id="password" required placeholder="Enter your password"/>
            <label htmlFor="password">Password</label>

            <span id="status-span" style={{ color: 'red' }}></span>

            <button onClick={() => sendData(
                email=document.getElementById('email').value,
                password=document.getElementById('password').value
            )}>Sign In</button>
        </div>
        </>
    )
}


export default SignIn
