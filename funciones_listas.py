""" Modulo Listas
    Funciones para practicas con listas
    Daniel Valencia Cordero
    Mayo 10-2021 """
# Definición de Funciones

def suma_acumulativa(lista_numeros):
  suma = []
  suma.append(lista_numeros[0])
  for i in range(0,len(lista_numeros)-1):
    suma.append(lista_numeros[i]+lista_numeros[i+1])
  print("La suma acumulada es:"+str(suma))

def traductor_pig_latin(lista_palabras):
  tradu = []
  vocales = ["a","e","i","o","u"]
  consonante = ["p", "q", "b", "t", "d", "c", "h", "j", "k", "g", "f", "v", "s", "z","m","n", "ñ", "l", "x", "r", "w", "e", "y"]
  for i in lista_palabras:
    if( vocales.count(i[0])==1 ):
      tradu.append(i+"yay")
    elif( consonante.count(i[0])==1 ):
      tradu.append(i[1:]+i[0]+"yay")
  print("Las palabras traducidas son: "+str(tradu))

def identificador_frutas(lista_frutas):
  frutas =[]
  for i in lista_frutas:
    if( i.count("a")>= 1 ):
      frutas.append(i)
  print("Las frutas que contiene la vitamina A so: "+str(frutas))

def son_palindromos(frase_uno, frase_dos):
  frase_uno = frase_uno.replace(" ","").lower()
  frase_dos = frase_dos.replace(" ","") .lower()
  tem =""
  for i in range(len(frase_dos)-1,-1,-1):
    tem = tem + frase_dos[i]
  if(tem == frase_uno):
    print("Las palabras evaluadas son palindromes")
  else:
    print("Las palabras evaluadas no son palindromes")
