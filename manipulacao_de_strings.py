string = "Hello, World!"

print(len(string)) #13
print(type(string)) #<class 'str'>
print(string  + " Concatenei")

# Replace -> Substitui uma string por outra
print(string.replace("World", "Mundo")) #Hello, Mundo!

# startsWith -> Verifica se a string começa com um determinado valor
print(string.startswith("Hello")) #True

# endsWith -> Verifica se a string termina com um determinado valor
print(string.endswith("!")) #True

# count -> Conta quantas vezes um determinado valor aparece na string
print(string.count("l")) #3

# capitalize -> Coloca a primeira letra da string em maiúsculo
nome = "gabs"
print(nome.capitalize()) #Gabs

# isdigit -> Verifica se a string é um número, se tiver ao menos uma letra ele retorna false
numero = "123"
print(numero.isdigit()) #True

# isalnum -> Verifica se a string é alfanumérica, se tiver ao menos um caractere especial ele retorna false
alphanumeric = "123abc"
print(alphanumeric.isalnum()) #True

# upper -> Coloca toda a string em maiúsculo
print(string.upper()) #HELLO, WORLD!

# lower -> Coloca toda a string em minúsculo
print(string.lower()) #hello, world!

# find -> Encontra a posição de um determinado valor na string
print(string.find("World")) #7

# strip -> Remove espaços em branco no início e no final da string
endereco = "   Rua das Flores, 123   "
print(endereco.strip()) #"Rua das Flores, 123"

# split -> Divide a string em substrings se encontrar instâncias do separador
endereco = "Rua das Flores, 123"
print(endereco.split(" ")) #['Rua das Flores', ' 123']

