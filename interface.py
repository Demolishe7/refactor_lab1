import logging

class Interface:
    
    def __init__(self, player):
        self.player = player

    def run(self):
        while True:
            command = input("> ").strip().lower()
            
            if command in ("exit"):
                self.player.stop()
                logging.info("Выход из программы.")
                break
            elif command == "play":
                self.player.play()
            elif command == "pause":
                self.player.pause()
            elif command == "resume":
                self.player.resume()
            elif command == "stop":
                self.player.stop()
            elif command == "skip":
                self.player.skip()
            else:
                logging.warning("Неизвестная команда.")