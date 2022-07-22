from ast import If
from operator import ifloordiv


nome=input("informe nome do aluno")
nota1=float(input("informe nota1 do aluno"))
nota2=float(input("informe nota2 do aluno"))
faltas=int(input("informe quantas faltas do aluno"))
media = (nota1 + nota2) /2 
if    media>=7 and faltas<3:
      print (nome +"foi aprovado")
else:
      print(nome +"foi reprovado")
     
