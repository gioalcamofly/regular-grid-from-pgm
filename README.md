Regular grid a partir de imagen PGM
============================

This script has been developed to be used as part of a robot navigation stack. It takes a pgm image representing a map as input, crop it and generates a regular grid as CSpace. This regular grid is represented as a matrix.

Este script ha sido desarrollado para ser usado como parte de la pila de navegación de un robot. Toma una imagen PGM representando un mapa como entrada, y tras tratarla debidamente genera un espacio tipo Regular Grid. Este espacio, utilizado a modo de grafo, será usado para realizar la búsqueda del mejor camino desde un punto A a un punto B por medio del algoritmo A*.



Archivos
---------------------

 - *main.py*: Archivo con el código principal. Lee la imagen almacenada en la carpeta 'resources' y tras tratarla haciendo uso de funciones auxiliares y obtener el regular grid correspondiente, traza el camino de un punto A a un punto B utilizando el algoritmo A*. Finalmente muestra la imagen con el camino a seguir dibujado.
 
 - *image_utils.py*: Archivo con funciones relativas al tratamiento de la imagen. Hace uso de la librería OpenCV y permite obtener la imagen original recortada junto a su regular grid correspondiente. Así, en primer lugar aplica un umbral a la imagen, dejando en negro los píxeles ocupados y en blanco los píxeles libres. A continuación, realiza un recorte de la imagen, para dejar únicamente el espacio donde se encuentra realmente el mapa (ya que por defecto se puede encontrar mucho espacio en negro alrededor). Además, este recorte no es completamente exacto, ya que se deja un pequeño espacio de más para que todos los límites del mapa sean negros y, por tanto, representen espacios ocupados (límites). Finalmente, se crea un regular grid, el cual no es más que una matriz, en la que cada celda representa un espacio de NxN de píxeles de la imagen(siendo N el valor almacenado en la variable GRID_SIZE), y cada valor informa si dicho espacio esta ocupado (1) o no (0).
 
 - *node.py*: Incluye la clase Node, la cual es utilizada por el algoritmo A* para recorrer el Regular Grid como si se tratase de un grafo.
 
 - *astar.py*: Incluye el algoritmo A*. A partir de un Regular Grid y unas coordenadas de inicio y final, devuelve el camino a seguir para llegar de un punto a otro.
 
 
 Funcionamiento
 --------------------
 
 - Funcionamiento por defecto: Ejecutar `python main.py`
 
 - Nuevas coordenadas: Alterar variables `start` y `end` en *main.py*.
 
 - Nueva imagen: Almacenar nueva imagen de formato .pgm en el directorio *resources* con el nombre *housemap.pgm*.
 
 - Cambiar tamaño del Regular Grid: Alterar variable `GRID_SIZE` en *image_utils.py*.
 
 
 Notas
 ------------
 
 Como futura mejora, queda pendiente permitir los cambios descritos en la sección anterior desde la línea de comandos, de forma que no sea necesario modificar el código para conseguir el comportamiento deseado.
 
 
