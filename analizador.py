import sys
from scanner import Scanner
from logger import Logger
import yara
from colorama import Fore

# Instanciar clases
scanner = Scanner()
logger = Logger()

# Verificar si se pasó un archivo como argumento
if len(sys.argv) < 2:
    print(Fore.RED + "❌ Error: No se proporcionó un archivo para analizar." + Fore.RESET)
    sys.exit(1)

archivo = sys.argv[1]

try:
    resultado = scanner.scan_file(archivo)  # Analizar el archivo
    print(resultado)
    logger.log_event(resultado)  # Registrar el evento
except (yara.Error, FileNotFoundError, PermissionError) as e:
    print(Fore.RED + f"⚠️ Error al analizar el archivo: {e}" + Fore.RESET)
