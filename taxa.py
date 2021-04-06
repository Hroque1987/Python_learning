#Input dados
salario=input('Salario Bruto:')
sub=input('Subsidio de almoço diario:')
days=input('Dias trabalhados mes:')
ss=input('Taxa de segurança social:')
int('ss')
if ss>11
    print('Taxa em Portugal 11%')
    ss=11
#Calculos
ss=float(ss)/100 #conversão para percentagem
liq=float(salario)-(float(salario)*float(ss))
sub=float(days)*float(sub)
print('Salario liquido:',liq)
print('Subsidio alimentação:',sub)
print('Salario Total:',liq+sub)
