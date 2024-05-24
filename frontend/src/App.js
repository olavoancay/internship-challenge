import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [x, setX] = useState('');
    const [y, setY] = useState('');
    const [result, setResult] = useState(null);
    const [error, setError] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setResult(null);

        const xNum = parseInt(x);
        const yNum = parseInt(y);

        if (isNaN(xNum) || isNaN(yNum) || xNum <= 0 || yNum <= 0 || xNum >= yNum) {
            setError('Por favor, insira inteiros positivos válidos onde x < y.');
            return;
        }

        try {
            const response = await axios.get('http://localhost:8000/api/calcula-mmc-intervalo/', {
                params: { x: xNum, y: yNum }
            });
            setResult(response.data.result);
        } catch (err) {
            setError('Ocorreu um erro ao buscar o resultado.');
        }
    };

    return (
        <div className="App">
            <div className="form-container">
                <h1>Bem-vindo!</h1>
                <p>
                    Este formulário calcula o menor número divisível por todos os números contidos em um intervalo definido por um valor inicial e um valor final.
                </p>
                <p>
                    <strong>Regras:</strong><br /><br />
                   - Os 2 valores devem ser números inteiros positivos<br />
                   - O valor inicial deve ser diferente do valor final<br />
                   - O valor final deve ser maior do que o valor inicial
                </p>
                <div id='formulario'>
                <form onSubmit={handleSubmit}>
                    <label>
                        Valor Inicial:
                        <input type="number" value={x} onChange={(e) => setX(e.target.value)} />
                    </label>
                    <label>
                        Valor Final: 
                        <input type="number" value={y} onChange={(e) => setY(e.target.value)} />
                    </label>
                    <button type="submit" >Calcular</button>
                </form>
                </div>
                {error && <p className="error">{error}</p>}
                {result && <p className="result">MMC: {result}</p>}
            </div>
        </div>
    );
}

export default App;
