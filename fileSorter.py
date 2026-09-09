#ORDENAR ARCHIVOS EN CARPETAS
#ej. IMAGENES, DOCS, AUDIOS, ETC. ETC.

import os 

CATEGORIAS = {
    ".jpg": "Imagenes", ".png": "Imagenes", ".gif": "Imagenes",
    ".pdf": "Documentos", ".docx": "Documentos", ".txt": "Documentos",
    ".mp3": "Musica", ".wav": "Musica",
    ".csv": "Datos", ".json": "Datos", ".xls": "Datos",
    ".mp4": "Video", ".avi": "Video", ".mov": "Video"

    }

def main():
    usuario = os.path.expanduser("~")
    
    carpeta = input("¿Que directorio queres ordenar?: ").strip()
    
    for dirs, subdirs, files in os.walk(usuario, topdown=True, onerror=None):
        if carpeta in subdirs:
            path = os.path.join(dirs, carpeta)
    
    print(path)
    
    if os.path.exists(path):
        try:            
            for file in os.listdir(path):
                ruta_origen = os.path.join(path, file)
                _, extension = os.path.splitext(file)        
                extension = extension.lower()
                create_dirs(ruta_origen, extension, path)
                
        except Exception as e:
            print(f"ERROR: {e}")       
    else:
        print("El path no existe")

def create_dirs(file, file_type, base_path):
    tipos = ['imagenes', 'documentos', 'musica', 'datos', 'video']
    for type, folder in CATEGORIAS.items():
        if type == file_type:
            for tipo in tipos:
                if folder.lower() == tipo:    
                    carpeta_destino = os.path.join(base_path, folder)                  
                    if (os.path.isdir(carpeta_destino) == False):
                        os.makedirs(carpeta_destino, exist_ok=True)
                        
                    ruta_completa = os.path.join(carpeta_destino, os.path.basename(file))

                    os.rename(file, ruta_completa)
                
if __name__ == "__main__":
    main()
