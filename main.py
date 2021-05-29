import funciones_listas as fn 



sw = "si"
while(sw == "si"):
  print("Digite la opcion que desea usar:")
  op = input("""   1 -> Si desea usar el suma_acumulativa
   2 -> Si desea usar el traductor_pig_latin
   3 -> Si desea usar el identificador_frutas
   4 -> Si desea usar el son_palindromos\n""")
  
  if(op == "1"):
    lista_numeros = input("Digite la lista de numeros separdas por , :\n").split(",")
    #lista_numeros = [1,2,3,4,5,6]
    fn.suma_acumulativa(lista_numeros)
  elif(op == "2"):
    lista_palabras = input("Digite la lista de palabras separdas por , :\n").split(",")
    #lista_palabras = ['out','and','word','father']
    fn.traductor_pig_latin(lista_palabras)
  elif(op == "3"):
    lista_frutas = input("Digite la lista de frutas separdas por , :\n").split(",")
    #ista_frutas = ['pera','manzana','limon','toronja','melon']
    fn.identificador_frutas(lista_frutas)
  elif(op == "4"):
    palabra1 = input("Digite la primera palabra:\n")
    palabra2 = input("Digite la segunda palabra:\n")
    #palabra = "Anula la luz azul a la luna"
    fn.son_palindromos(palabra1, palabra2)

  sw = input("Desea seguir con el programa: si/no\n")

#





