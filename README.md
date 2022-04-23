# lista_reproduccion
Lista de Reproducción de Música
Con el paso de los años, usted y su grupo de amigos han adquirido la costumbre de reproducir música cada vez que se reunen.
 A pesar de que tienen gustos similares cuando se trata de sus artistas preferidos, es muy difícil estar de acuerdo al 
elegir cuál de las canciones de un artista les gustaría escuchar a continuación. Para esto, usted decide aplicar los 
conocimientos que ha adquirido en su curso de programación para crear un programa que tenga listas de reproducción por 
artista y que permita al grupo simplemente decidir cuál artista les gustaría escuchar. Este programa generará comandos 
que usted puede luego ingresar en cualquiera de las plataformas de streaming que tengan a su alcance.





añadir: primero que nada, su programa debería permitir añadir canciones nuevas. Para esto, el usuario puede agregar 
el título de una canción de un artista determinado. Una vez recibe el comando añadir, el programa recibe, en las dos 
líneas siguientes, el nombre de la canción y el nombre de artista y lo agrega a la lista de reproducción.
reproducir: una vez usted y sus amigos han añadido las canciones que más les gusta, deberían poder "reproducir" la 
siguiente canción. Después de ingresar el comando reproducir, en la siguiente línea se ingresa el nombre de un artista, 
el programa deberá escribir en pantalla la siguiente canción a reproducirse. Para simplificar las cosas, las canciones 
se reproducirán en el orden en el que fueron añadidas, reproduciendo primero las canciones más antiguas y eliminando las 
canciones conforme se van reproduciendo. El texto que reporta este comando tiene 3 formas:

- Si el artista tiene canciones en cola, deberá escribir el texto: Reproduciendo <canción> de <artista>., con el título de la canción y el nombre del artista correspondientes
- Si ya se reprodujeron todas las canciones de un artista, deberá escribir el texto: No quedan canciones en cola.
- Si el artista ingresado nunca ha tenido canciones registradas, deberá escribir el mensaje El artista no tiene canciones registradas.
detener: como el artista recibe un número indeterminado de canciones, se tiene que definir una forma de terminar su ejecución. Cuando el programa recibe el comando detener, el programa deberá escribir el mensaje Terminando sesión. ¡Hasta pronto! y terminar su ejecución.

En caso de que el comando ingresado esté mal escrito o sea desconocido por el programa, se deberá informar al usuario 
con el mensaje Comando no reconocido. Intente de nuevo:
