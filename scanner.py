import yara
from logger import Logger  
from colorama import Style, Fore
import os

class Scanner:
    def __init__(self, rule_path=r"C:\Users\Juan\Desktop\EPPLab\malware.yar", log_file="logs/epp_logs.txt"):
        self.logger = Logger(log_file)
        try:
            self.rules = yara.compile(filepath=rule_path)
            self.logger.log_info(f"Reglas YARA cargadas desde {rule_path}")
        except yara.SyntaxError as e:
            self.logger.log_error(Fore.RED+f"Error en las reglas YARA: {e}")
            self.rules = None   
            print(Style.RESET_ALL)

    def scan_file(self, file_path):
        # Verifica si el archivo existe antes de continuar
        if not os.path.exists(file_path):
            error_msg = f"[ERROR] El archivo {file_path} no existe o intentelo sin comillas dobles(en caso de estarlas usando)."
            self.logger.log_error(error_msg)
            print(error_msg)
            return None

        # Verifica si el archivo está vacío
        if os.path.getsize(file_path) == 0:
            warning_msg = f"[ADVERTENCIA] El archivo {file_path} está vacío, omitiendo análisis."
            self.logger.log_warning(warning_msg)
            print(warning_msg)
            return None

        # Verifica si las reglas de YARA están cargadas
        if not self.rules:
            error_msg = "[ERROR] No se pudieron cargar las reglas YARA."
            self.logger.log_error(error_msg)
            print(error_msg)
            return error_msg

        # Escanea el archivo con YARA
        matches = self.rules.match(file_path)

        if matches:
            log_message = Fore.RED + f"[ALERTA] Archivo malicioso detectado en {file_path}: {matches}" + Fore.RESET
            self.logger.log_warning(log_message)
        else:
            log_message = Fore.GREEN + f"[OK] Archivo seguro: {file_path}" + Fore.RESET
            self.logger.log_info(log_message)

        return log_message