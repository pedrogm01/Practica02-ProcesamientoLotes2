import os
import time

# Función para eliminar archivos con extensión maligna
def eliminar_archivos_malignos(directorio, extension_maligna=".mal"):
    for ruta_actual, subdirectorios, archivos in os.walk(directorio):
        for archivo in archivos:
            if archivo.endswith(extension_maligna):
                archivo_maligno = os.path.join(ruta_actual, archivo)
                try:
                    os.remove(archivo_maligno)
                    print(f"Archivo eliminado: {archivo_maligno}")
                except Exception as e:
                    print(f"No se pudo eliminar {archivo_maligno}: {e}")

# Función principal que se ejecuta periódicamente
def vigilar_y_eliminar_archivos_malignos(directorio, extension_maligna=".mal", intervalo=5):
    while True:
        print(f"Revisando...")
        eliminar_archivos_malignos(directorio, extension_maligna)
        time.sleep(intervalo)

if __name__ == "__main__":
    carpeta_actual = os.getcwd()  # Carpeta actual
    extension_maligna = ".mal"  # Define la extensión maligna
    intervalo_revision = 10  # Intervalo de tiempo entre revisiones (en segundos)

    # Comienza la vigilancia y eliminación de archivos malignos
    vigilar_y_eliminar_archivos_malignos(carpeta_actual, extension_maligna, intervalo_revision)
