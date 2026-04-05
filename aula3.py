n1 = int (input ('de primeiro numero:  '))
n2 = int (input ('de segundo numero:  '))



## posso colocar dessas duas formas
##s = n1+n2
##print('A noma é {}'.format(n1+n2))
##print('A noma é {}'.format(s))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print ('A soma é {}, multiplicação é {} e a divisão é {:.3f}'.format(s, m, d))
print ('Divisão inteira é {} e a Potência é {}'.format(di,e))