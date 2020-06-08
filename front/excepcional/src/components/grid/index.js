import React, { Component } from 'react'
import { connect } from "react-redux"
import axios from "axios"
import { MdFirstPage, MdChevronLeft, MdChevronRight, MdLastPage } from 'react-icons/md'
import GridRow from '../../components/grid/gr-row'

class TableGrid extends Component {

    state = {
        selecionado: false,
        linhasPorPagina: 10,
        qtdPaginas: 0,
        pagina: 1
    }

    componentDidMount = async() => {
        await axios.get("http://localhost:3000/erros")
            .then(resposta => {
                this.props.dispatch({
                    type: "GET_ERROS",
                    payload: resposta.data
                    })
                })

        this.setState({
            qtdPaginas: Math.ceil(this.props.erros.length / this.state.linhasPorPagina)
        })
    }

    calcularPaginas = () => {
        this.setState({
            qtdRegistros: this.props.erros.length(),
            qtdPaginas: Math.ceil(this.props.erros.length() / this.qtdRegistros)
        })
    }

    marcarTodos = () => {
        const novoSelecionado = !this.state.selecionado
        

        this.setState({
            selecionado: novoSelecionado
        })

        this.props.erros.map(erro => (
            erro.selecionado = novoSelecionado
        ))
    }

    irParaPrimeiraPagina = () => {
        this.setState({
            pagina: 1
        })
    }

    irParaPaginaAnterior = () => {
        if (this.state.pagina > 1) {
            this.setState({
                pagina: this.state.pagina -1
            })
        }
    }

    irParaProximaPagina = () => {
        if (this.state.pagina !== this.state.qtdPaginas) {
            this.setState({
                pagina: this.state.pagina +1
            })
        }
    }

    irParaUltimaPagina = () => {
        this.setState({
            pagina: this.state.qtdPaginas
        })
    }

    render() {
        const erros = this.props.erros

        return(
            <table className="grade">
                <thead>
                    <tr>
                        <th className="t-min"><input type="checkbox" onChange={this.marcarTodos}></input></th>
                        <th className="t1">Nível</th>
                        <th className="t1">Data</th>
                        <th className="t1">Hora</th>
                        <th className="t1">Origem</th>
                        <th className="t-max">Mensagem</th>
                        <th className="t1">Ocorrências</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.qtdPaginas > 0 &&
                    erros.map((erro, i) => (
                        <GridRow
                            key={erro.id}
                            linha={i}
                            linhasPorPagina={this.state.linhasPorPagina}
                            pagina={this.state.pagina}
                            selecionado={erro.selecionado}
                            id={erro.id}
                            nivel={erro.nivel}
                            data={erro.data}
                            hora={erro.hora}
                            origem={erro.origem}
                            mensagem={erro.mensagem}
                            ocorrencias={erro.ocorrencias}
                        />
                    ))}
                </tbody>
                <tfoot>
                    <tr>
                        <td colSpan="7" className="gr-paginacao">
                            <div className="gr-botoes">
                                <MdFirstPage className="gr-botao" onClick={this.irParaPrimeiraPagina} />
                                <MdChevronLeft className="gr-botao" onClick={this.irParaPaginaAnterior} />
                                <span className="gr-page"> {this.state.pagina} / {this.state.qtdPaginas} </span>
                                <MdChevronRight className="gr-botao" onClick={this.irParaProximaPagina} />
                                <MdLastPage className="gr-botao" onClick={this.irParaUltimaPagina} />
                            </div>
                        </td>
                    </tr>
                </tfoot>
            </table>
        );
    }
      
}

function mapStateToProps(state) {
    return {
       erros: state.erros
    };
}

export default connect(mapStateToProps)(TableGrid)