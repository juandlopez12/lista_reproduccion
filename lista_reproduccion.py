canciones={}

while True:
  comando= input()
  if comando=="añadir":
  
    cancion=input()
    artista=input()
    
    
    if artista not in canciones:
      canciones[artista]=list() #quiere decir que... en el diccionario canciones, la clave [artista] pasada por input tiene un valor de lista vacia
    if artista in canciones:
      canciones[artista].append(cancion) #quiere decir que... cancion pasado por input se agrega al valor

  elif comando=="reproducir":
    artista=input()
    if artista in canciones:
      if len(canciones[artista]) >0:
        cancion=canciones[artista].pop(0)
        print(f"Reproduciendo {cancion} de {artista}")
      else:
        print(f"No quedan canciones en la cola.")
    else:
      print(f"El artista no tiene canciones registradas.")

  elif comando=="detener":
    print(f"Terminando sesión. ¡Hasta pronto!")
    break
  
  else: 
    print(f"Comando no reconocido. Intente de nuevo:")
    
    

