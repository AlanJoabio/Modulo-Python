"""
Operadores Aritméticos
"""

a = 10;
b = 3;

soma                 = a + b; # Somar
subtracao            = a - b; # Subtração
multiplicacao        = a * b; # Multiplicação
divisao              = a / b; # Divisão (float)
resto_da_divisao     = a % b; # Resto da divisão (int) e não float.
resto_descartado     = a // b; #Divisão após descartado a parte fracionária
raiz_quadrada        = pow(2,4); #Raiz quadrada
exponenciacao        = a ** b; #Potência

print("Soma:", soma,"\n");
print("Subtração:", subtracao,"\n");
print("Multiplicação:", multiplicacao,"\n");
print("Divisão:", divisao,"\n");
print("Resto da divisão", resto_da_divisao,"\n");
print("Resto Descartado: ", resto_descartado,"\n");
print("Raíz Quadrada de 8 é igual à:", raiz_quadrada,"\n");
print("Exponenciação do número 'A' elevada ao número 'B':", exponenciacao,"\n");
            
