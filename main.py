import logging
from player import MusicPlayer
from updater import Updater
from interface import Interface

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

if __name__ == "__main__":
    logging.info("Запуск музыкального плеера...")
    
    Updater.check_for_updates()
    player = MusicPlayer(console_mode=True)
    interface = Interface(player)
    
    interface.run()