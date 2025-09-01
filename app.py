# -*- coding: utf-8 -*-
# Este script demonstra funcoes basicas de Python


def saudacao(nome):
    return f"Ola, {nome}!"

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

if __name__ == "__main__":
    nomes = ["Alice", "Bob", "Charlie"]
    for nome in nomes:
        saudacao(nome)
    
    resultado = somar(5, 3)
    print(f"A soma de 5 e 3 é {resultado}")

    resultado_subtracao = subtrair(10, 4)
    print(f"A subtracao de 10 e 4 é {resultado_subtracao}")