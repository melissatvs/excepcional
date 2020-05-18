import React from 'react'
import '../../styles/forms.css'
import { Link } from 'react-router-dom'

function Login() {

    return(
        <main>
            <h2 className="titulo-pagina">Acesso ao Monitor</h2>
            <form className="register">
                <input className="campo-texto" type="text" placeholder="e-mail"></input>
                <input className="campo-texto" type="text" placeholder="senha"></input>
                <Link to="/monitor"><button className="botao">Entrar</button>
                </Link>
            </form>
        </main>
    )    
}

export default Login