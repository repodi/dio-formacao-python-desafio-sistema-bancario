# Sistema bancário em Python

Desafio DIO da Formação Python Developer que tem por objetivo a construção de um sistema bancário utilizando os conceitos iniciais da linguagem Python.

## Objetivo

Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato. 

## Narrativa do escopo 

O banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão devemos implementar apenas 3 operações: depósito, saque e extrato. 


### Operação de depósito

Deve ser possível depositar valores positivos para a conta bancária. 

O sistema possui apenas um usuário. Então não é necessário identificar a agência e conta. 

Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato. 

### Operação de saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 

Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. 

Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato. 

### Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. 

No fim da listam deve ser exibido o saldo atual da coanta. 

Se o extrato estiver em branco, exibir a mensagem: 

*Não foram realizadas movimentações*

