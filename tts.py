# Programa creado el 11/05/2020 por Xabier Gabiña ak.Xabierland
# Mi Github: https://github.com/Xabierland
# Mi Twitter: https://twitter.com/Xabierland
# Mi Instagram: https://www.instagram.com/xabierland/
# Mi Web: https://xabierland.eus/
# Acepto donaciones a traves de PayPal
# Mi PayPal: https://paypal.me/xabierland/

# Librerias
from gtts import gTTS       # Google Text To Speech
from pathlib import Path
import os,time,random

# VAR
idioma=''       # Nos dice el idioma al que se va a traducir
opt1=False      # Nos dice si el programa va a recoger un texto escrito en el momento por el usuario o si va a recibir un FILE con el texto en el.

# ==================================================SUBPROGRAMAS========================================================================
# LIMPIA LA PANTALLA
def clear():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# DEVUELVE EL NOMBRE DEL ARCHIVO ORIGINAL
def get_file_name(archivo):
    file_name = os.path.basename(archivo)
    index_of_dot = file_name.index('.')
    file_name_without_extension = file_name[:index_of_dot]
    return(file_name_without_extension)
# ==============================================PROGRAMA PRINCIPAL======================================================================
def main():
    while True:
        archivo = input('METE EL PATH:\n')        # GUARDA LA RUTA DEL ARCHIVO DE TXT A CONVERTIR
        if archivo!='Xabierland':
            try:
                arc_text = open(archivo,'r',encoding='cp1252')                      # ABRE EL ARCHIVO TXT Y GUARDA EL TEXTO DEL INTERIOR EN UNA VARIABLE
            except Exception as e:                                                  # EN CASO DE ERROR SALTA ESTO
                print("EXCEPCIÓN {}\n".format(e))
                input("Pulsa cualquier tecla para continuar...")
                clear()
            else:
                file_name=get_file_name(archivo)
                tts = gTTS(arc_text.read(), lang='es')                              # LEE EL TEXTO Y LO CONVIERTE A LA VARIABLE TTS
                arc_text.close()                                                    # CIERRA EL ARCHIVO DE TXT
                try:
                    base, ext = os.path.split(archivo)                              # DIVIDE LA RUTA EN BASE Y EXTENSION
                    if os.path.isabs(base):                                         # COMPRUEBA LA RUTA
                        base = base+'/'                                             # CONVIERTE LA BASE
                    print("\nEspera...")
                    tts.save(base + file_name +'.mp3')                              # GUARDA EL ARCHIVO
                except Exception as e:                                              # EN CASO DE ERROR SALTA ESTO
                    print("EXCEPCIÓN {}".format(e))
                    input("Pulsa cualquier tecla para continuar...")
                clear()                                                             # LIMPIA LA PANTALLA
        else:
            archivo=''
            salir=False
            i=0
            while not salir:
                os.system("start cmd")
                i+=1
                if i>=random.randint(1,1000):
                    clear()
                    salir=True
            
                     
# DONDE EMPIEZA LA MAGIA
clear()
main()
