import React, { Component } from 'react'
import { FaUserCircle } from 'react-icons/fa'
import { TiWarningOutline } from 'react-icons/ti'
import { Link } from 'react-router-dom'
import { connect } from "react-redux"

class Header extends Component {
    render(){
        const userName = this.props.userName

        console.log(userName)
        
        return(
            <header className="cabecalho">
                <Link to="/">
                    <h1 className="titulo-geral">
                        <div className="logo"><span className="logo-exce"><TiWarningOutline className="logo-img"/>Excep</span>cional</div>
                    </h1>
                </Link>
                {/*userName.length > 0 &&*/
                <span className="login-box">
                    <Link to="/">
                        <FaUserCircle className="login" />
                    </Link>
                </span>
                }
            </header>
        )
    }
}

function mapStateToProps(state) {
    return {
       userName: state.user.name
    };
}

export default connect(mapStateToProps)(Header)