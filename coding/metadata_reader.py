#Importaciones
import os
import exifread
from PyPDF2 import PdfReader

# os >> maneja rutas verificando si un archivo existe y obtener su extensión.
# exifread >> extrae metadatos EXIF de imágenes.
# PyPDF2 >> permite leer y obtener metadatos de archivo PDF.

# Funcion que analiza imagen
def analizar_imagen(ruta):
    print(f"\n Metadatos de imagen. {ruta}")
    with open(ruta, 'rb') as f:
        etiquetas = exifread.process_file(f)
        if etiquetas:
           for tag in etiquetas.keys():
               print(f"{tag}: {etiquetas[tag]}")
        else:
            print("No se encontraron metadatos EXIF.")

# Abre archivo de imagen en modo binario ('rb').
# Usa exifread.process_file() para leer los metadatos EXIF.
# Si no tiene EXIF imrpime que no hay metadatos.

# Funcion que analiza PDF
def analizar_pdf(ruta):
    print(f"\n Metadatos de PDF: {ruta}")
    try:
        pdf = PdfReader(ruta)
        meta = pdf.metadata
        if meta:
            for k, v in meta.items():
                print(f"{k}: {v}")
        else:
            print(f"no hay metadatos en este PDF.")
    except Exception as e:
        print(f"Error leyendo el PDF")

# Abre el PDF con PdfReader.
# Extrae los metadatos con pdf.metadata.
# Usa try/except para evitar que el programa se caiga si el PDF esta dañado o protegido.

#Funcion principal
 def main():
     print("=== Analizador de Metadatos ===")
     ruta = input("Introduce la ruta del archivo: ").strip()

     if not os.path.exists(ruta):
        print("El archivo no existe.")
            return
        
     extension = os.path.splitext(ruta)[1].lower()

     if extension in ['.jpg', 'jpeg', '.png']:
        analizar_imagen(ruta)
     elif extension == '.pdf':
        analizar_pdf(ruta)
     else:
            print("Tipo de archivo no soportado. Usa JPG, PNG o PDF.")

# Pide al usuario una ruta de archivo.
# Verifica con os.path.exists() si el archivo realmente existe.
# Usa os.path.splitext() para obtener la extensión del archivo.

#Ejecución del programa
if __name__ == "__main__":
    main()

# Esto hace que se ejecute solo si lo corres directamente (ej. metadatos.py)
# Si se importa como modulo no se ejecutará automáticamente.
