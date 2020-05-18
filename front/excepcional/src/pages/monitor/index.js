import React, { Component } from 'react'
import '../../styles/forms.css'
import { Link } from 'react-router-dom'
import { BsSearch } from 'react-icons/bs'

class Monitor extends Component {

    state = { checked: false }

    myChangeHandler = (event) => {
        this.setState({
            checked: !this.state.checked      
        })
    }

    render() {
        return(
            <main>
                <h2 className="titulo-pagina">Monitor</h2>
                <section className="filtros">
                    <label for="ambiente">Ambiente:</label>
                    <select id="ambiente">
                        <option value="producao">Produção</option>
                        <option value="homolog">Homologação</option>
                        <option value="dev">Desenvolvimento</option>
                    </select>
                    <label for="ordenacao">Ordenar por:</label>
                    <select id="ordenacao">
                        <option value="nivel">Nível</option>
                        <option value="ocorrencias">Ocorrências</option>
                    </select>
                    <label for="ordenacao">Buscar por:</label>
                    <select id="busca">
                        <option value="nivel">Nível</option>
                        <option value="mensagem">Mensagem</option>
                        <option value="origem">Origem</option>
                    </select>
                    <input type="text"></input>
                    <BsSearch />
                </section>
                <table className="grade">
                    <tr className="grade-linha">
                        <th><input type="checkbox" onChange={this.myChangeHandler}></input></th>
                        <th>Nível</th>
                        <th>Data</th>
                        <th>Hora</th>
                        <th>Origem</th>
                        <th>Mensagem</th>
                        <th>Ocorrências</th>
                    </tr>
                    <tr className="grade-linha">
                        <td><input type="checkbox" checked={this.state.checked}></input></td>
                        <td>Erro</td>
                        <td>01/02/2022</td>
                        <td>11:59:03</td>
                        <td>192.168.0.1</td>
                        <td>Access Violation</td>
                        <td>100</td>
                    </tr>
                    <tr className="grade-linha">
                        <td><input type="checkbox" checked={this.state.checked}></input></td>
                        <td>Erro</td>
                        <td>01/02/2022</td>
                        <td>11:59:03</td>
                        <td>192.168.0.1</td>
                        <td>Access Violation</td>
                        <td>100</td>
                    </tr>
                    <tr className="grade-linha">
                        <td><input type="checkbox" checked={this.state.checked}></input></td>
                        <td>Erro</td>
                        <td>01/02/2022</td>
                        <td>11:59:03</td>
                        <td>192.168.0.1</td>
                        <td>Access Violation</td>
                        <td>100</td>
                    </tr>
                    <tr className="grade-linha">
                        <td><input type="checkbox" checked={this.state.checked}></input></td>
                        <td>Erro</td>
                        <td>01/02/2022</td>
                        <td>11:59:03</td>
                        <td>192.168.0.1</td>
                        <td>Access Violation</td>
                        <td>100</td>
                    </tr>
                </table>
            </main>
        )  
    }
      
}

export default Monitor