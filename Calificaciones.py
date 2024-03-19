
#Registro de alumnos y calificaciones
#Crea un programa para registrar alumnos y sus calificaciones en diferentes materias. 
# El programa debe permitir agregar alumnos, asignar calificaciones, mostrar el promedio de calificaciones
# y guardar esta información en un archivo.

import pandas as pd
import matplotlib.pyplot as plt

#Clase del programa
class RegistroCalificaciones:
    def __init__(self):
        try:
            archivo_csv = 'calificaciones.csv'
            datos_existente = pd.read_csv(archivo_csv)
        except:
            self.registro = pd.DataFrame(columns=['Alumno', 'Materia', 'Calificación'])
              
        # Abrir el archivo CSV existente
        
        #Crea el DataFrame con las columnas Alumno, Materia y Calificacion        

    def agregar_alumno(self, nombre_alumno): 
        #Por cada materia existente en la tabla se agrega una fila con el nombre del alumno
        #y cada materia encontrada, sin clasificacion.
        for materia in self.registro['Materia'].unique():
            self.registro = self.registro.append({'Alumno': nombre_alumno, 'Materia': materia, 'Calificación': None}, ignore_index=True)

    def asignar_calificacion(self, nombre_alumno, materia, calificacion):
        self.registro.loc[len(self.registro)] = [nombre_alumno, materia, calificacion]

    def mostrar_promedio(self, nombre_alumno):
        promedios = []
        for materia in self.registro['Materia'].unique():
            calificaciones = self.registro.loc[(self.registro['Alumno'] == nombre_alumno) & (self.registro['Materia'] == materia), 'Calificación']
            print(calificaciones)
        
        if not calificaciones.empty:
            promedio = calificaciones.mean()
            promedios.append((nombre_alumno, promedio))
        
        if promedios:
            promedios_df = pd.DataFrame(promedios, columns=['Alumno', 'Promedio'])
            print("Promedio de calificaciones para", nombre_alumno)
            print(promedios_df)
        else:
            print("No hay calificaciones registradas para", nombre_alumno)

    def guardar_registro(self, filename):
        self.registro.to_csv(filename, index=False)

    def cargar_registro(self, filename):
        self.registro = pd.read_csv(filename)

    def visualizar_registro(self):
        self.registro.set_index('Alumno', inplace=True)
        self.registro['Calificación'] = pd.to_numeric(self.registro['Calificación'], errors='coerce')
        self.registro.groupby('Materia')['Calificación'].mean().plot(kind='bar')
        plt.title('Promedio de calificaciones por materia')
        plt.ylabel('Promedio')
        plt.xlabel('Materia')
        plt.show()

# Ejemplo de uso
registro = RegistroCalificaciones()
registro.agregar_alumno('Juan')
registro.agregar_alumno('María')
registro.agregar_alumno("Agustin")
registro.asignar_calificacion('Agustin', 'Matemáticas', 10)
registro.asignar_calificacion('Agustin', 'Historia', 2)
registro.asignar_calificacion('Juan', 'Matemáticas', 8)
registro.asignar_calificacion('Juan', 'Historia', 7)
registro.asignar_calificacion('María', 'Matemáticas', 9)
registro.asignar_calificacion('María', 'Historia', 8)
registro.mostrar_promedio('Juan')
registro.mostrar_promedio('María')
registro.mostrar_promedio("Agustin")
registro.guardar_registro('calificaciones.csv')
registro.visualizar_registro()
