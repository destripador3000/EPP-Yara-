import yara
from logger import Logger  
from colorama import Style, Fore

class Scanner:
    def __init__(self, rule_path="malware.yar", log_file="logs/epp_logs.txt"):
        self.logger = Logger(log_file)
        try:
            self.rules = yara.compile(filepath=rule_path)
            self.logger.log_info(f"Reglas YARA cargadas desde {rule_path}")
        except yara.SyntaxError as e:
            self.logger.log_error(Fore.RED+f"Error en las reglas YARA: {e}")
            self.rules = None   
            print(Style.RESET_ALL)

    def scan_file(self, file_path):
        if self.rules:
            matches = self.rules.match(file_path)
            if matches:
                log_message = Fore.RED + f"[ALERTA] Archivo malicioso detectado en {file_path}: {matches}"+Fore.RESET
                self.logger.log_warning(log_message)
               
                return log_message
            log_message = Fore.GREEN + f"[OK] Archivo seguro: {file_path}"+Fore.RESET
            self.logger.log_info(log_message)
            
            return log_message
        self.logger.log_error("[ERROR] No se pudieron cargar las reglas YARA.")
        return "[ERROR] No se pudieron cargar las reglas YARA."
