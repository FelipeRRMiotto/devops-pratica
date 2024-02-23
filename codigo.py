#Declarando variaveis de lista e opção
lista = []
opcao = 's'

#Menu principal, continua rodando enquanto o usuario digitar s
while opcao == 's':
    #obtendo dados
    nome = input('Digite o nome do aluno: ')
    n1 = input('\nDigite a primeira nota do aluno: ')
    n2 = input('\nDigite a segunda nota do aluno: ')

    #calculando a media
    media = (int(n1)+int(n2))/2

    #adicionando os dados em uma lista representando um aluno e colocando essa lista dentro da lista de alunos
    lista.append([nome, n1, n2, media])
    opcao = input('\n\nDeseja inserir outro aluno? s/n: ')

#mostrando todos os alunos individualmente
print('\n\nAluno | N1 | N2 | Media ')
for i in lista:
    print(i[0],' | ',i[1],' | ',i[2],' | ',i[3])