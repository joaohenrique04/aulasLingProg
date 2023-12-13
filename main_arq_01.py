# Muito a melhorar, principalmente refatorando e tratando erros, porém o tempo atual nao permite 
# e estou entregando essa parcial funcional com todos os requisitos

def solicita_info():
    nome = input('Digite o nome >> [0 encerra] ')

    if nome == '0':
        print("Volte sempre!")
        le_nomes()
        exit()

    idade = input('Digite a idade >> ')
    sexo = 'x'
    while sexo != 'M' and sexo != 'F':
        sexo = input('Digite o sexo >> [M/F] ').upper()
    telefone = input('Digite o telefone >> ')
    print('')

    texto = str(nome)+'|'+str(idade)+'|'+str(sexo)+'|'+str(telefone)

    return texto

def limpa():
    arq = open('oii.txt', 'w', encoding='utf-8')
    arq.write('')
    arq.close()    

def escreve_nomes(nomes):
    sobr = open('oii.txt', 'a', encoding='utf-8')
    sobr.write(nomes)
    sobr.close()

def le_nomes():

    tipoBusca = 0
    while tipoBusca not in ('1', '2', '3'):
        print("Que tipo de busca você quer realizar? ")
        print('1 - Listar Tudo')
        print('2 - Por Gênero')
        print('3 - Por Nome')
        tipoBusca = input()

    leitura = open('oii.txt', 'r', encoding='utf-8')
    nomes = leitura.read()
    leitura.close()

    pessoas = nomes.split('\n')
    pessoas.pop(-1)

    if tipoBusca == '2':
        sexo = 'A'
        while sexo not in ('M', 'F'):
            sexo = input("Qual sexo vc deseja pesquisar? [M/F]").upper()
        pessoas = busca_usuario_pelo_sexo(sexo)
    elif tipoBusca == '3':
        nome = input("Qual nome vc deseja pesquisar? ")
        pessoas = busca_usuario_pelo_nome(nome)

    for x in pessoas:
        dados = x.split('|')
        
        sexo = str(dados[2])
        print(busca_usuario_pelo_sexo)
        sexo = sexo.replace('M', 'Masculino')
        sexo = sexo.replace('F', 'Feminino')
        print(sexo)

        print('Nome: '      + str(dados[0]))
        print('Idade: '     + str(dados[1]))
        print('Sexo: '      + sexo)
        print('Telefone: '  + str(dados[3]))
        

        print('')

def busca_usuario_pelo_sexo(sexo):
    leitura = open('oii.txt', 'r', encoding='utf-8')
    nomes = leitura.read()
    leitura.close()

    pessoas = nomes.split('\n')
    pessoas.pop(-1)

    resultado = []

    for x in pessoas:
        dados = x.split('|')
        if dados[2] == sexo: 
            resultado.append(dados[0]+'|'+dados[1]+'|'+dados[2]+'|'+dados[3])
            
    return resultado

def busca_usuario_pelo_nome(nome_procurado):
    leitura = open('oii.txt', 'r', encoding='utf-8')
    nomes = leitura.read()
    leitura.close()

    pessoas = nomes.split('\n')
    pessoas.pop(-1)

    resultado = []

    for x in pessoas:
        dados = x.split('|')
        if nome_procurado.upper() in dados[0].upper():
            resultado.append(dados[0]+'|'+dados[1]+'|'+dados[2]+'|'+dados[3])

    return resultado


def main():
    limpa()
    while True:
        nomes = solicita_info()
        escreve_nomes(nomes+'\n')
main()
