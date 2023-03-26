#solicitar salário
salario_base = float(input('Digite seu salário: R$'))
#solicitar gratificação
gratificacao = float(input('Digite o valor da gratificação que você vai receber: R$'))
#calcular salário + gratificação
salario_bruto = salario_base + gratificacao
#entrega resultado na tela
print('--------------------------Salário--------------------------')
print('Salário total-------------: R$ {:.2f}'.format(salario_bruto))