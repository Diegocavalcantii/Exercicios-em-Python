n1=float(input('Digite a 1 nota: '))
n2=float(input('Digite a 2 nota: '))
m=(n1+n2)/2
print(f'A sua média foi: {m:.1f}')
if m >= 6.0:
    print(f'Parabéns!')
else:
    print('Sua média foi ruim')