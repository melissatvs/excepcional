import React from 'react'
import { Link } from 'react-router-dom'

function Home() {
    return(
        <main>
            <section className="apresentacao">
                <p>Tenha controle das exceções <span className="apresentacao-palavras">da sua aplicação</span>
                </p>          
            </section>
            <form className="acesso">
                <section className="botoes">
                <Link to="/register-user">
                    <button className="botao">Criar Conta</button>
                </Link>
                <Link to="/login">
                    <button className="botao">Login</button>
                </Link>
                </section>
            </form>
        </main>
    )    
}

export default Home