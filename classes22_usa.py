# - Sintaxe:
# from nome_arquivo_sem_extensao import NomeClasse1, NomeClasse2, NomeClasse3
from classes22 import Conta, PessoaFisica, PessoaJuridica
if __name__ == '__main__':
    c1 = Conta('Alice', 1000.00) # Chama o construtor da classe Conta
    print("Endereço do objeto:", c1)
    print('- Superclasse:\nNome:', c1.get_nome())  # Métodos da superclasse
    print('Saldo:', c1.get_saldo())
    c1.set_nome('Emily')
    print('Nome alterado:', c1.get_nome())

    pf1 = PessoaFisica('Ana', 3000.0, 'f')  # Objeto da subclasse
    print("Endereço do objeto:", pf1)
    print('- Pessoa Física 1:\nNome:', pf1.get_nome())  # Método na superclasse
    print("Saldo:", pf1.get_saldo())
    pf2 = PessoaFisica('Ailton', 7000.0)    # Objeto da subclasse
    print("Endereço do objeto:", pf2)
    print('- Pessoa Física 2:\nNome:', pf2.get_nome())  # Método na superclasse

    pj1 = PessoaJuridica('Café ABC', 15000.0, 'MEI') # Objeto (instância)
    print(pj1)
    print('- Pessoa Jurídica:\nNome:', pj1.get_nome())  # Método da superclasse
    print("Saldo:", pj1.get_saldo())
    print(pj1)
    pj2 = PessoaJuridica('Padaria', 35000.0) # Objeto (instância)

    pf1.deposito(11)                                       # Depósito
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())   # Verifica alteração
    pj1.deposito(22)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo()) # Verifica alteração
    pf1.retirada(10)                                       # Retirada sem RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())   # Verifica alteração
    pj1.retirada(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo()) # Verifica alteração
    pf1.retirada_rn(10)                                    # Retirada com RN
    print("- Pessoa Física 1:\nSaldo:", pf1.get_saldo())   # Verifica alteração
    pj1.retirada_rn(21)
    print("- Pessoa Jurídica 1:\nSaldo:", pj1.get_saldo()) # Verifica alteração
    pj1.retirada_rn(20000.0)                               # Retirada, msg erro
    print('Saldo: ', pj1.get_saldo())                      # Verifica alteração
    print("- Pessoa Física 1, antes:\nSaldo:", pf1.get_saldo())
