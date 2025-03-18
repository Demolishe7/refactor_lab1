import requests
import logging

UPDATE_URL = "https://example.com/version.txt"  # Заменить на реальный URL

class Updater:
    
    CURRENT_VERSION = "2.4.3"

    @staticmethod
    def check_for_updates():
        try:
            response = requests.get(UPDATE_URL, timeout=5)
            response.raise_for_status()
            latest_version = response.text.strip()

            if latest_version > Updater.CURRENT_VERSION:
                logging.info(f"Доступна новая версия: {latest_version}. Обновите плеер!")
            else:
                logging.info("Обновлений нет.")
        except requests.RequestException as e:
            logging.warning(f"Ошибка проверки обновлений: {e}")