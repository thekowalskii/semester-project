import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Cookies from 'js-cookie';

import SignIn from "./SignInForm";
import api from "../../api";


function Header() {
    const logout = async () => {
        Cookies.remove('access_token')
        api.post('/logout')

        location.reload()
    }

    return (
        <>
        <header style={{backgroundColor: '#ffe0b2', flexShrink: 0}} className="block-el">
            <h2>ArtStudia</h2>

            <nav>
                <Link to='/signin' className="nav-link">Sign In</Link>
                <Link onClick={() => {logout()}} className="nav-link" style={{ color: '#9a1111' }}>Log Out</Link>

                {/* <a onClick={() => logout()}>Log Out</a>
                <a href='/signin'>Sign In</a> */}
            </nav>
        </header>
        </>
    )
}


export default Header
