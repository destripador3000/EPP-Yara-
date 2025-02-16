from scanner import Scanner
from logger import Logger
import yara
from colorama import Fore
import os

scanner = Scanner()
logger = Logger()

def main():
    while True:
        try:
            print("1. Escanear un archivo\n2. Escanear archivos de una carpeta\n0. Salir")
            
            try:
                opcion = int(input("Elige una opción: "))
           
                if opcion == 1:
                    archivo = input("Ingrese la ruta del archivo: ")
                    resultado = scanner.scan_file(archivo)
                    print(resultado)
                    logger.log_event(resultado)  

                elif opcion == 2:
                    ruta = input("Escribe la ruta a analizar: ")
                    
                    if not os.path.exists(ruta):  # Verifica si la ruta existe
                        print(Fore.RED + "Error: La ruta no existe." + Fore.RESET)
                        continue

                    for archivo in os.listdir(ruta):
                        rutaCompleta = os.path.join(ruta, archivo)

                        if os.path.isfile(rutaCompleta):
                            
                            resultado = scanner.scan_file(rutaCompleta)  
                            print(resultado)
                            logger.log_event(resultado)  
                        else:
                            print(Fore.YELLOW + "No es un archivo, no puede ser escaneado: " + archivo + Fore.RESET)

                elif opcion == 0:
                    break

                else:
                    print(Fore.RED + "Opción inválida, intenta de nuevo." + Fore.RESET)

            except ValueError:
                print(Fore.RED + "El valor ingresado no es válido." + Fore.RESET)

        except (yara.Error, FileNotFoundError, PermissionError) as e:
            print(Fore.RED + f" Error: {e}" + Fore.RESET)

if __name__ == "__main__":
    main()

