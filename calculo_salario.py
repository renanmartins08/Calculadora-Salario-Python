#solicitar salário
salario_base = float(input('Digite seu salário: R$'))
#calcular vale-transporte/ vai ser levado em considadeção o desconto de 6% do salario-base
vale_transporte = salario_base * 0.06
#calcular inss
if salario_base <= 1302.00:
   inss = salario_base * 0.075
elif salario_base <= 2571.29:
     inss = salario_base * 0.09
elif salario_base <= 3856.94:
      inss = salario_base * 0.12
elif salario_base <=7507.49:
      inss = salario_base * 0.14
else:
   pass
   
#entrega resultado na tela
if salario_base <=7507.49:
    salario_bruto = salario_base - inss - vale_transporte
    print('--------------------------Salário--------------------------')
    print('seu inss é:------------- {:.2f}'.format(inss))
    print('Vale Transporte:------------- {:.2f}'.format(vale_transporte))
    print('Salário total-------------: R$ {:.2f}'.format(salario_bruto))
else:
     salario_base =7507.49
     print('Valor não se enquadro na tabela do inss, o valor maximo é : R$7507.49!')
   