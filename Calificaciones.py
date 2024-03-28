
#Registro de alumnos y calificaciones
#Crea un programa para registrar alumnos y sus calificaciones en diferentes materias. 
# El programa debe permitir agregar alumnos, asignar calificaciones, mostrar el promedio de calificaciones
# y guardar esta información en un archivo.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Clase del programa
class RegistroCalificaciones:
    
    def __init__(self):
        try:
            
            # Define el diccionario de tipos de datos para cada columna
            dtype_dict = {
                'Alumno': str,
                'Materia': str,
                'calificacion': int
            }
            
            self.archivo_csv = 'calificaciones.csv'
            self.registro = pd.read_csv(self.archivo_csv, dtype=dtype_dict)
            print("Se cargaron datos de archivo existente.")
        except:
            self.registro = pd.DataFrame(columns=['Alumno', 'Materia', 'Calificación'])
            print("No existe archivo con calificaciones. Se crea archivo.")
              
    def esta_calificacion_no_registrada(self, nombre_alumno, materia):
        materia_registrada = self.registro.loc[(self.registro['Alumno'].str.upper() == nombre_alumno.upper()) & (self.registro['Materia'].str.upper() == materia.upper())].empty
        return materia_registrada
        
    def asignar_calificacion(self, nombre_alumno, materia, calificacion):
        if (self.esta_calificacion_no_registrada(nombre_alumno, materia)):
            nueva_fila = {'Alumno': nombre_alumno, 'Materia': materia, 'Calificación': calificacion}
            self.registro = self.registro._append(nueva_fila, ignore_index=True)
            self.guardar_registro()
        else:
            print("Este alumno ya tiene calificacion en la materia.")

    def mostrar_promedio(self, nombre_alumno):
        try:
            promedios = []
            for materia in self.registro['Materia'].unique():
                calificaciones = self.registro.loc[(self.registro['Alumno'] == nombre_alumno) & (self.registro['Materia'] == materia), 'Calificación']
                if not calificaciones.empty:
                    promedio = calificaciones.mean()
                    promedios.append(promedio)

            if promedios:
                promedio_total = sum(promedios) / len(promedios)
                print("Promedio de calificaciones para", nombre_alumno, "en todas las materias:", promedio_total)
            else:
                print("No hay calificaciones registradas para", nombre_alumno)
        except:
            print("Error al mostrar el promedio del Alumno: " + nombre_alumno)
    
    
    def guardar_registro(self):
        try:
            self.registro.to_csv(self.archivo_csv, index=False)
            print("Archivo guardado exitosamente.")
        except:
            print("Error en guardar el archivo.")
            
            
    def visualizar_registro(self):
        try:
            self.registro.set_index('Alumno', inplace=True)
            self.registro['Calificación'] = pd.to_numeric(self.registro['Calificación'], errors='coerce')
            self.registro.groupby('Materia')['Calificación'].mean().plot(kind='bar')
            plt.title('Promedio de calificaciones por materia')
            plt.ylabel('Promedio')
            plt.xlabel('Materia')
            plt.show()
        except:
            print("Error al crear la imagen")
            
    def mostrar_modelo_tabla_de_calificaciones_1(self):
        # Verificar si la columna 'Alumno' está presente en el DataFrame
        if 'Alumno' not in self.registro.columns:
            print("Error: La columna 'Alumno' no está presente en el DataFrame.")
            return

        # Crear una figura de Matplotlib
        fig, ax = plt.subplots(figsize=(10, 6))

        # Ocultar ejes
        ax.axis('off')

        # Crear la tabla con la información del DataFrame
        tabla = ax.table(cellText=self.registro.values, colLabels=self.registro.columns, loc='center')

        # Establecer el tamaño de la fuente
        tabla.set_fontsize(14)

        # Ajustar el diseño de la tabla
        tabla.auto_set_column_width([0, 1, 2])

        # Mostrar la figura
        plt.show()
        
    def mostrar_modelo_tabla_de_calificaciones_2(self):
        # Verificar si la columna 'Alumno' está presente en el DataFrame
        if 'Alumno' not in self.registro.columns:
            print("Error: La columna 'Alumno' no está presente en el DataFrame.")
            return

        # Crear la tabla pivote
        tabla_pivote = self.registro.pivot(index='Alumno', columns='Materia', values='Calificación')

        # Crear una figura de Matplotlib
        fig, ax = plt.subplots()
        
        # recorro los valores, reemplazando nan por '-'
        data = np.array(tabla_pivote.values)
        df = pd.DataFrame(data)
        datos_nuevos = df.fillna('-')
        
        # Crear la tabla con las calificaciones de cada alumno en cada materia
        tabla = ax.table(cellText=datos_nuevos.values ,
                         colLabels=tabla_pivote.columns,
                         rowLabels=tabla_pivote.index,
                         loc='center')

        # Ocultar ejes
        ax.axis('off')

        # Establecer el tamaño de la fuente
        tabla.set_fontsize(14)

        # Ajustar el diseño de la tabla
        tabla.auto_set_column_width([i for i in range(len(tabla_pivote.columns))])  # Ajustar el ancho de las columnas automáticamente

        # Centrar los valores de las celdas
        for key, cell in tabla.get_celld().items():
            cell.set_text_props(fontsize=12, ha='center', va='center')

        # Resaltar los nombres de las columnas en negro
        for key, cell in tabla.get_celld().items():
            if key[0] == 0:  # Filas de encabezado
                cell.set_text_props(weight='bold', color='black')
        # Mostrar la tabla
        plt.show()
    
    
        

if __name__ == "__main__":
    # Ejemplo de uso
    registro = RegistroCalificaciones()
    
    print("----------------------------\n" +
        "1- Agregar Alumno y Calificacion.\n" + 
          "2- Mostrar tablas de calificaciones.\n" +
          "3- Guardar archivo.\n" +
          "4- Calcular promedio de un alumno.\n" +
          "5- Visualizar promedio de calificaciones por materia.\n" + 
          "6- Salir.\n" +
          "-----------------------------")
    while True:
        try:
            opcion = int(input("Elija una opción: "))
        except:
            print("Ingrese una opcion válida.")
            
        if(opcion == 1):
            nombre = input("Nombre del alumno: ")
            materia = input("Materia: ")
            calificacion = input("Ingrese calificacion de la materia: ")
            registro.asignar_calificacion(nombre, materia, calificacion)
        elif (opcion == 2):
            registro.mostrar_modelo_tabla_de_calificaciones_1()
            registro.mostrar_modelo_tabla_de_calificaciones_2()
        elif (opcion == 3):
            registro.guardar_registro()
        elif (opcion == 4):
            nombre = input("Nombre alumno: ")
            registro.mostrar_promedio(nombre)
        elif (opcion == 5):   
            registro.visualizar_registro()
        elif (opcion == 6):
            break
        else:
            print("Opcion incorrecta.")