import React, { Component } from 'react'

class GridRow extends Component {

    state = {
        selecionado: false
    }

    toggleCheck = () => {
        this.setState({
            selecionado: !this.state.selecionado
        })
    }

    componentDidUpdate(prevProps) {
        if (this.props.selecionado !== prevProps.selecionado) {
            this.setState({
                selecionado: this.props.selecionado
            })
        }
    }

    render() {
        const { id, nivel, data, hora, origem, mensagem, ocorrencias, 
            linha, linhasPorPagina, pagina } = this.props
        
        return (
            <>
                {Math.ceil((linha+1) / linhasPorPagina) === pagina &&
                    <tr key={id} className={"gr-" + nivel.toLowerCase()}>
                        <td className="t-min">
                            <input
                                name="check"
                                type="checkbox"
                                checked={this.state.selecionado}
                                onChange={this.toggleCheck}>
                            </input>
                        </td>
                        <td className="t1">{nivel}</td>
                        <td className="t1">{data}</td>
                        <td className="t1">{hora}</td>
                        <td className="t1">{origem}</td>
                        <td className="t-max">{mensagem}</td>
                        <td className="t1">{ocorrencias}</td>
                    </tr>
                }
            </>
        )
    }
}

export default GridRow