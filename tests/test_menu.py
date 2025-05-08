import pytest
from unittest.mock import patch, call
from menu.menu_items import MainMenu, Menu


class TestMainMenu:

    @pytest.fixture
    def main_menu(self):
        return MainMenu()

    def test_menu_items_should_return_list_of_options(self, main_menu):
        items = main_menu.menu_items

        assert isinstance(items, list)
        assert len(items) == 7
        assert items[0] == "Encrypt text"
        assert items[-1] == "Exit"

    def test_display_menu_prints_menu_items(self, main_menu, mocker):
        mock_print = mocker.patch("builtins.print")
        main_menu.display_menu()

        mock_print.assert_any_call("\n===MENU===")

        for i, item in enumerate(main_menu.menu_items, start=1):
            mock_print.assert_any_call(f"{i}. {item}")

        mock_print.assert_any_call("==========")

    def test_get_choice_should_return_menu_option(self, main_menu):
        with patch("builtins.input", return_value=1):
            choice = main_menu.get_choice()

        assert choice == 1

    def test_get_choice_should_print_when_number_is_outside_range(self, main_menu):
        with patch("builtins.input", side_effect=[99, 1]):
            with patch("builtins.print") as mock_print:
                main_menu.get_choice()
                mock_print.assert_any_call("Please enter a number between 1 and 7")

    def test_get_choice_should_reject_non_numeric_input(self, main_menu):
        with patch("builtins.input", side_effect=["numer", "trzy", 1]):
            with patch("builtins.print") as mock_print:
                main_menu.get_choice()
                mock_print.assert_any_call("Please enter a valid number")
