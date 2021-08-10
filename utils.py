import os
import sys
import logging

from logging.handlers import RotatingFileHandler


def get_logger():
    logs_folder_path = os.getenv('LOGS_FOLDER_PATH')
    app_name = os.getenv('APP_NAME')

    if not os.path.isdir(logs_folder_path):
        os.mkdir(logs_folder_path)
    log_file_path = logs_folder_path + '/' + app_name + '.log'
    if not os.path.isfile(log_file_path):
        log_file = open(log_file_path, "a")
        log_file.close()

    logger = logging.getLogger(app_name)
    logger.setLevel('DEBUG')

    log_format = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(log_file_path, maxBytes=(1048576 * 5), backupCount=5)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    logger.info('logger created')

    return logger


def write_env_file(logger):
    logger.info('writing to .env file')

    with open(".env", "w") as f:
        f.write(f"APP_NAME={os.getenv('APP_NAME')}\n")
        f.write(f"LOGS_FOLDER_PATH={os.getenv('LOGS_FOLDER_PATH')}\n")
        f.write(f"DESIRED_FOLLOWING={os.getenv('DESIRED_FOLLOWING')}\n")
        f.write(f"IFC_EMAIL_SENT={os.getenv('IFC_EMAIL_SENT')}\n")
        f.write(f"LAN={os.getenv('LAN')}\n")
        f.write(f"SMTP_PORT={os.getenv('SMTP_PORT')}\n")
        f.write(f"SMTP_SERVER={os.getenv('SMTP_SERVER')}\n")
        f.write(f"SENDER_EMAIL={os.getenv('SENDER_EMAIL')}\n")
        f.write(f"EMAIL_PASSWORD={os.getenv('EMAIL_PASSWORD')}\n")
        f.write(f"RECEIVER_EMAIL={os.getenv('RECEIVER_EMAIL')}\n")
        f.write(f"IG_USERNAME={os.getenv('IG_USERNAME')}\n")
        f.write(f"IG_PASSWORD={os.getenv('IG_PASSWORD')}\n")
