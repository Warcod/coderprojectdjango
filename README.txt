Bienvenidos a la entrega parcial de mi proyecto en Django

Enlisto los pasos para probar la web:

1- Levantar el servidor y entrar al la url principal (/' ')
    Esto levanta la view home() , donde podemos encontrar el inicio de nuestra web, el menú lateral para navegarla y los botones para acceder a las funciones.

2- Luego acceder a alguna de las tres categorías Series, Peliculas o Canciones. Pueden hacerlo tanto por el menú lateral o por los botones en el boddy del HTML.

3- Una vez en alguna de estas secciones, estaremos parados en perfil/<nombreDeLaSección>. Supongamos que es Canciones.

4- Estaremos parados sobre pefil/songs lo cual levantará la vista songs() y te dejará hacer 3 cosas:

    4.1 Ver todas las canciones en la BBDD.
    4.2 Agregar una nueva canción.
    4.3 Buscar una nueva canción.

5- Agrega una canción haciendo clic en "agregar canción". Esto te llevará a perfil/form-song/ y allí verás un form de django que te pedirá los datos para agregar una nueva canción a la lista. Complétalo y pulsa agregar.

6- Una vez agregada, vuelve a ver las canciones con el boton "ver todas las canciones". Allí debería aparecer la canción recientemente agregada.

7- Ahora busca una canción. Haciendo clic en "Buscar una canción". 

8- Esto te llevará a /perfil/search-song y ahí verás un form para buscar por título. Busca el titulo que quieras encontrar. Si no existe la canción, no aparecerá nada, y podrás hacer otra búsqueda con el botón buscar.

9- Vuelve al home con el menú lateral.

Y eso es todo :)