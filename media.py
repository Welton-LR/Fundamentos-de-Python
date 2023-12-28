nota1 = float(input("Digite o nome de Portugês!---------"))
nota2 = float(input("Digite o nome de Matemática!---------"))
nota3 = float(input("Digite o nome de História!---------"))
nota4 = float(input("Digite o nome de Geografia!---------"))
media = (nota1 + nota2 + nota3 + nota4) /4
print(media)

if media>=7:
    print("Aprovado!")
elif media <6:
    print("Reprovado!")      
else:
    print("Em Recuperação!")    