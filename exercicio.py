a = 80000
b = 200000

cont = 0

while a < b:
    a *=  1.03 
    b *= 1.015  
    cont += 1
print(f'o ano que a cidade A passará a cidade B é {cont}')