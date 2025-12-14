#Imports
import os
import exifread
from PyPDF2 import PdfReader

# os >> handles paths checking if an archive exists or by obtaining its extension.
# exifread >> extracts images metadata EXIF.
# PyPDF2 >> allows read and obtain PDF archive metadata.

# Function that analyze images
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

# Open PDF with PdfReader.
# Extracts metadata with pdf.metadata.
# Use try/except to prevent the program from crashing if the PDF is damaged or protected.

#Principal function
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
            print("Archive types not supported. Usa JPG, PNG o PDF.")

# Ask the user for a file path.
# Verify with os.path.exists() if archive really exists.
# Use os.path.splitext() to obtain the file path.

#Program execution
if __name__ == "__main__":
    main()

# This means it will run only if you run it directly. (ex. metadatos.py)
# if it imports as a module it will not run automatically.
