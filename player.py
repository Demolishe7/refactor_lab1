import pygame
import random
import logging
import threading
from pathlib import Path
from time import sleep

MUSIC_DIR = Path("Music")

class MusicPlayer:
    
    def __init__(self, console_mode=False):
        pygame.init()
        pygame.mixer.init()
        self.console_mode = console_mode
        self.playlist = self.get_music_files()
        self.current_track = None
        self.is_playing = False
        self.skip_flag = False
        self.play_thread = None

    def get_music_files(self):
        if not MUSIC_DIR.exists():
            MUSIC_DIR.mkdir()
            logging.warning("Папка 'Music' создана, но пустая.")
            return []
        
        files = list(MUSIC_DIR.glob("*.mp3"))
        if not files:
            logging.error("Нет доступных треков!")
        return files

    def _play_music(self):
        self.is_playing = True
        random.shuffle(self.playlist)

        for idx, track in enumerate(self.playlist, start=1):
            if not self.is_playing:
                break

            self.current_track = track
            logging.info(f"Воспроизведение {idx}/{len(self.playlist)}: {track.name}")
            
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()
            self.skip_flag = False

            while pygame.mixer.music.get_busy() and self.is_playing:
                if self.skip_flag:
                    pygame.mixer.music.stop()
                    break
                sleep(0.5)

        self.is_playing = False
        logging.info("Все треки проиграны или остановлены.")

    def play(self):
        if not self.playlist:
            logging.error("Нет доступных треков!")
            return
        
        if self.is_playing:
            logging.warning("Музыка уже играет!")
            return

        self.play_thread = threading.Thread(target=self._play_music, daemon=True)
        self.play_thread.start()

    def stop(self):
        self.is_playing = False
        pygame.mixer.music.stop()
        logging.info("Музыка остановлена.")

    def pause(self):
        pygame.mixer.music.pause()
        logging.info("Музыка на паузе.")

    def resume(self):
        pygame.mixer.music.unpause()
        logging.info("Музыка возобновлена.")

    def skip(self):
        if not self.is_playing:
            logging.warning("Сейчас музыка не играет.")
            return
        
        logging.info("Пропуск трека...")
        self.skip_flag = True