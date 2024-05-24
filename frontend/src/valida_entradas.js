
export const valida_entradas = (x, y) => {
    if (!x || !y) {
        return 'Valor inválido! Por favor, complete todos os campos do formulário';

    }
    
    try {
        x = parseInt(x);
        y = parseInt(y);
        if (isNaN(x) || isNaN(y) || x <= 0 || y <= 0) {
            return 'Valor inválido! Por favor, digite 2 números inteiros positivos';
        }
        if (x >= y) {
            return 'Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial';
        }
        return null;
    } catch (error) {
        return 'Valor inválido! Por favor, digite 2 números inteiros positivos';
    }
};
