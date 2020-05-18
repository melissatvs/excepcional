import React from 'react'
import { FaUserCircle } from 'react-icons/fa'
import { TiWarningOutline } from 'react-icons/ti'
import { Link } from 'react-router-dom'

function Header() {
    return(
        <header className="cabecalho">
            <Link to="/">
                <h1 className="titulo-geral">
                    <span className="logo-exce"><TiWarningOutline className="logo-img"/>Exce</span>pcional
                </h1>
            </Link>            
            <span className="login-box">
                <Link to="/">
                    <FaUserCircle className="login" />
                </Link>
            </span>
            
        </header>
    )
}

export default Header