#EXERCÍCIO 27
morango_kg = float(input("Digite a quantidade de morangos em kg: "))
maca_kg = float(input("Digite a quantidade de maças em kg: "))
#MORANGOS
preco_menor_mor = morango * 2.50
preco_maior_mor = morango * 2.20
#MAÇÃ
preco_menor_mac = maca * 1.80
preco_maior_mac = maca * 1.50
#CÁLCULO DO MORANGO
if morango >= 5:
    preco_total_mor = preco_menor_mor
else:
    preco_total_mor = preco_maior_mor
#CÁLCULO DA MAÇÃ
if maca >= 5:
    preco_total_mac = preco_menor_mac
else:
    preco_total_mac = preco_maior_mac
preco_total_das_frutas = preco_total_mor + preco_total_mac
#CÁLCULO TOTAL DAS FRUTAS
if preco_total_das_frutas >= 25 or (morango_kg + maca_kg) >= 8:
    print("Valor final: ", (preco_total_mor - (preco_total_mac * 0.1)))
else:
    print("Valor final: ", preco_total_das_frutas)



