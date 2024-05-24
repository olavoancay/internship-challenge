import { valida_entradas } from './valida_entradas';

describe('Teste de validação de entradas', () => {
  test('Campos em branco', () => {
    expect(valida_entradas('', '')).toBe('Valor inválido! Por favor, complete todos os campos do formulário');
  });

  test('X campo em branco', () => {
    expect(valida_entradas('', '10')).toBe('Valor inválido! Por favor, complete todos os campos do formulário');
  });

  test('Y campo em branco', () => {
    expect(valida_entradas('10', '')).toBe('Valor inválido! Por favor, complete todos os campos do formulário');
  });

  test('X não inteiro', () => {
    expect(valida_entradas('abc', '10')).toBe('Valor inválido! Por favor, digite 2 números inteiros positivos');
  });

  test('Y não inteiro', () => {
    expect(valida_entradas('10', 'abc')).toBe('Valor inválido! Por favor, digite 2 números inteiros positivos');
  });

  test('X negativo', () => {
    expect(valida_entradas('-1', '10')).toBe('Valor inválido! Por favor, digite 2 números inteiros positivos');
  });

  test('Y negativo', () => {
    expect(valida_entradas('10', '-1')).toBe('Valor inválido! Por favor, digite 2 números inteiros positivos');
  });

  test('Y menor que X', () => {
    expect(valida_entradas('10', '5')).toBe('Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial');
  });

  test('X igual a Y', () => {
    expect(valida_entradas('10', '10')).toBe('Valor inválido! O valor final do intervalo deve ser maior do que o valor inicial');
  });

  test('Sucesso', () => {
    expect(valida_entradas('1', '4')).toBe(null);
  });
});
