import logging
import os

class Logger:
    def __init__(self, log_file="logs/epp_logs.txt"):
       
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

       
        logging.basicConfig(
            filename=log_file,
            level=logging.INFO,  
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_warning(message):
        logging.warning(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_event(message):
        logging.info(f"Event: {message}")  # Personaliza el formato si es necesario

# Uso de la clase Logger
logger = Logger()
logger.log_event("Este es un evento personalizado")  # Ahora esto funciona
logger.log_info("Este es un mensaje informativo")
logger.log_error("Este es un mensaje de error")