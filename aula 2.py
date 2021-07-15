a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
soma= a + b
subtracao= a - b
multiplicacao= a * b
divisao = a/b
resto=a%b
potencia=a**b
Resultado=('Soma: {}. '
      '\nSubtração: {}.'
      ' \nMultiplicação: {}. '
      '\nResto: {}. '
      '\nDivisão: {}.'
      '\nPotência: {}. '.format(soma,subtracao, multiplicacao, resto, divisao, potencia))
print(Resultado)

