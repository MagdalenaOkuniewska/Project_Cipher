from abc import ABC, abstractmethod


class Menu(ABC):

    @abstractmethod
    @property
    def menu_items(self):
        pass


class MainMenu(Menu):
    """Handle displaying options and executing selected actions."""

    @property
    def menu_items(self):
        return [
            "Encrypt text",
            "Decrypt text",
            "Save to JSON file",
            "Load from JSON file",
            "Exit",
        ]

    def display_menu(self) -> None:
        print("\n===MENU===")
        for i, item in enumerate(self.menu_items, start=1):
            print(f"{i}. {item}")
        print("==========")

    def get_choice(self) -> int:
        """Get and validate user menu choice."""

        while True:
            try:
                choice = int(input("Please provide a menu choice (number): "))
                if 1 <= choice <= len(self.menu_items):
                    return choice
                else:
                    print(f"Please enter a number between 1 and {len(self.menu_items)}")
            except ValueError:
                print("Please enter a valid number")
