import React from 'react'
import '../../styles/forms.css'

function RegisterUser() {

    return(
        <main>
            <h2 className="titulo-pagina">Cadastro de Usuário</h2>
            <form className="register">
                <input className="campo-texto" type="text" placeholder="e-mail"></input>
                <input className="campo-texto" type="text" placeholder="senha"></input>
                <input className="campo-texto" type="text" placeholder="confirme a senha"></input>
                <button className="botao">Cadastrar</button>                
            </form>
        </main>
    )    
}

export default RegisterUser