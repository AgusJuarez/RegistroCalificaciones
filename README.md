CURSO DE PYTHON

Introducción:
El programa es una herramienta para el registro de alumnos y sus calificaciones en diferentes materias. Permite agregar alumnos, asignar calificaciones, mostrar el promedio de calificaciones realizando cálculo y visualización de promedios. Esta información se guarda en un archivo CSV.

Descripción del programa:

Está escrito en Python, utiliza la biblioteca pandas para la manipulación de datos y matplotlib para la visualización de gráficos. A continuación, se describen las principales características y funciones del programa:

Clase Registro Calificaciones:
- Esta clase gestiona todas las operaciones relacionadas con el registro de calificaciones.
Incluye métodos para agregar alumnos, asignar calificaciones, mostrar promedios y visualizar tablas y gráficos de calificaciones.
Los datos se almacenan en un DataFrame de pandas, con columnas para el nombre del alumno, materia y la calificación.

Métodos principales:
- agregar_alumno(nombre_alumno): Este método estaba diseñado para agregar un nuevo alumno al registro, pero no está implementado en el programa final.
- asignar_calificacion(nombre_alumno, materia, calificación): Asigna una calificación a un alumno en una materia específica.
- mostrar_promedio(nombre_alumno): Calcula y muestra el promedio de calificaciones de un alumno en todas las materias.
- mostrar_promedio2(nombre_alumno): Este método muestra el promedio de calificaciones de un alumno para cada materia individualmente.
- guardar_registro(): Guarda el registro actual en un archivo CSV.
- visualizar_registro(): Visualiza el promedio de calificaciones por materia en forma de gráfico de barras.
mostrar_tabla() y mostrar_tabla2(): Muestran tablas con las calificaciones de los alumnos, con la segunda versión mostrando los valores de manera más legible.

Interfaz de usuario:

El programa ofrece un menú de opciones para que el usuario interactúe con las funciones por consola.
El usuario puede agregar calificaciones, mostrar tablas y gráficos, guardar el registro y calcular promedios.

Funcionamiento del Programa

El programa se ejecuta en un bucle donde el usuario elige una opción del menú. Dependiendo de la opción seleccionada, el programa realiza las operaciones correspondientes utilizando los métodos de la clase RegistroCalificaciones.
Posibles Mejoras
Mejorar la interfaz de usuario proporcionando mensajes más informativos y manejo de errores más robusto.
Añadir funcionalidades adicionales, como la capacidad de eliminar calificaciones o generar informes detallados.
