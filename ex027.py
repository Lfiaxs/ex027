nome = str(input('Digite seu nome completo: ')).strip()
d = nome.split()
print('Muito prazer em te conhecer!')
print('O primeiro nome é {}.'.format(d[0]))
print('O último nome é {}.'.format(d[len(d)-1]))
