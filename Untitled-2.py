#Desenvolvendo a primeiroa versao 
def saudacao () -> str:
    print("Olá , seja bem vindo")
saudacao() 

def saudacao_nome(nome):
    return "Olá é um prazer te conhecer " + nome
resultado = saudacao_nome("rafael") 
print(resultado)