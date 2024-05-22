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
            setError('Please enter valid positive integers where x < y.');
            return;
        }

        try {
            const response = await axios.get('http://localhost:8000/api/calcula-mmc-intervalo/', {
                params: { x: xNum, y: yNum }
            });
            setResult(response.data.result);
        } catch (err) {
            setError('An error occurred while fetching the result.');
        }
    };

    return (
        <div className="App">
            <form onSubmit={handleSubmit}>
                <label>
                    x:
                    <input type="number" value={x} onChange={(e) => setX(e.target.value)} />
                </label>
                <label>
                    y:
                    <input type="number" value={y} onChange={(e) => setY(e.target.value)} />
                </label>
                <button type="submit">Calculate</button>
            </form>
            {error && <p className="error">{error}</p>}
            {result && <p className="result">MMC: {result}</p>}
        </div>
    );
}

export default App;