import React, { Component } from 'react'
import TableGrid from '../../components/grid'
import { BsSearch } from 'react-icons/bs'

class Monitor extends Component {

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
                
                <TableGrid />
            </main>
        );
    }
      
}

export default Monitor