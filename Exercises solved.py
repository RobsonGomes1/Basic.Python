# Exercícios básicos aritméticos

# Quest 1: Crie um programa que leia dois números e mostre a soma entre eles.

z = int(input("Valor do primeiro número a ser somado: "))  #Valores a serem somados
y = int(input("Valor do primeiro número a ser somado: "))
soma = z + y #Var para Armazenar  o resultado da soma
print(" Valor: {} \n Valor 2: {} \n Soma: {} <<<".format(z, y, soma)) #Apresentação do resultado

print("\nPróximo exercício\n")

# Faça um programa que leia algo pelo teclado
# mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

X = (input("Digite qualquer valor ou caractere: "))
print("Informações sobre a variavel X: \n")
print("Contém alfanumérico: ", X.isalnum())
print("Contém alfanumérico: ", X.isalpha())



print("\nPróximo exercício")

# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n1 = int(input("Diga o numero para ser realizado o Antecessor/ Sucessor: "))
ant = (n1 - 1) #Antecessor (Variável)
su = (n1 + 1)  # Sucessor (Variável)
print("Valor:{} \n Antecessor:{}\nSucessor:{}".format(n1, ant, su))  # Apresentação

print("Proximo exercício")

#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

Numero1 = int(input("Valor a ser chamado: "))
dobro = (Numero1*2)
triplo = (Numero1*3)
raiz = Numero1**(1/2)
print("Valor inserido: {}\nDobro:{}\nTriplo:{}\nRaiz quadrada: {:.1f}\n".format(Numero1,dobro,triplo,raiz))

#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
print("\nCALCULANDO MÉDIA\n")
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1 + nota2)/2
print("Media é: {:.1f}".format(media))
if media > 6: #Se nota for maior que 6, apresenta como aprovado
    print("Aluno aprovado")
elif media == 6: #Elif segunda condição ... Se nota for igualmente a 6
    print("Fazer recuperação")
else: #Senão... Caso nota for menor que média 6, aluno será reprovado
  print("Reprovado")
