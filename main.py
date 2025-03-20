# python -m main.py
# python main.py

from manager.manager import Manager
from cipher.cipher import CipherFacade
from buffer.buffer import Buffer
from files_service.file_handler import FileHandler
from menu.menu_items import MainMenu


def main():
    cipher = CipherFacade()
    buffer = Buffer()
    file_handler = FileHandler()
    menu = MainMenu()

    manager = Manager(cipher, buffer, file_handler, menu)
    manager.run()


if __name__ == "__main__":
    main()
