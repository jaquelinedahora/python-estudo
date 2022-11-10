from calendar import isleap

ano = int(input("digite o ano: "))

if isleap(ano):
    print("é bissexto")
else:
    print("não é bissexto")