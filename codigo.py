lista = []
opcao = 's'

while opcao == 's':
    nome = input('Digite o nome do aluno: ')
    n1 = input('\nDigite a primeira nota do aluno: ')
    n2 = input('\nDigite a segunda nota do aluno: ')
    media = (int(n1)+int(n2))/2
    lista.append([nome, n1, n2, media])
    opcao = input('\n\nDeseja inserir outro aluno? s/n: ')

print('\n\nAluno | N1 | N2 | Media ')
for i in lista:
    print(i[0],' | ',i[1],' | ',i[2],' | ',i[3])