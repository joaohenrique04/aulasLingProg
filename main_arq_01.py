def solicita_info():
    nome = input('Digite o nome >> [0 encerra] ')

    if nome == '0':
        print("Volte sempre!")
        exit()

    idade = input('Digite a idade >> ')
    sexo = input('Digite o sexo >> [M/F] ').upper()
    telefone = input('Digite o telefone >> ')

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
    leitura = open('oii.txt', 'r', encoding='utf-8')
    nomes = leitura.read()
    leitura.close()

    lista = nomes.split(';')

    for x in lista:
        print(x)


def main():
    limpa()
    while True:
        nomes = solicita_info()
        escreve_nomes(nomes+'\n')

main()