import pytest
from unittest.mock import Mock, patch, ANY, call, create_autospec
from cipher.cipher import CipherFacade, CipherNotFoundError
from buffer.buffer import Buffer
from buffer.text import Text
from files_service.file_handler import FileHandler
from menu.menu_items import MainMenu
from manager.manager import Manager


class TestManager:
    @pytest.fixture
    def mock_cipher_facade(self):
        cipher_facade = Mock(spec=CipherFacade)
        return cipher_facade

    @pytest.fixture
    def mock_buffer(self):
        buffer = Mock(spec=Buffer)
        buffer.storage = [
            Text("text1", "rot13", "encrypted"),
            Text("text2", "rot47", "decrypted"),
        ]
        return buffer

    @pytest.fixture
    def mock_file_handler(self):
        file_handler = Mock(spec=FileHandler)
        return file_handler

    @pytest.fixture
    def mock_menu(self):
        menu = Mock(spec=MainMenu)
        return menu

    @pytest.fixture
    def manager(self, mock_cipher_facade, mock_buffer, mock_file_handler, mock_menu):

        return Manager(
            cipher_facade=mock_cipher_facade,
            buffer=mock_buffer,
            file_handler=mock_file_handler,
            menu=mock_menu,
        )

    def test_init_should_initialize_properties(
        self, manager, mock_buffer, mock_file_handler, mock_cipher_facade, mock_menu
    ):
        assert manager.cipher_facade == mock_cipher_facade
        assert manager.buffer == mock_buffer
        assert manager.file_handler == mock_file_handler
        assert manager.menu == mock_menu
        assert manager.is_running == True

    def test_actions_should_contain_all_methods(self, manager):
        actions = manager.actions

        assert isinstance(actions, dict)
        assert len(actions) == 7
        assert actions[1] == manager.encrypt_text
        assert actions[2] == manager.decrypt_text
        assert actions[3] == manager.display_buffer
        assert actions[4] == manager.clear_buffer
        assert actions[5] == manager.save_to_file
        assert actions[6] == manager.load_from_file
        assert actions[7] == manager.exit_program

    def test_encrypt_text_should_enable_make_cipher_operation_make_call(self, manager):
        with patch.object(
            manager, "_Manager__make_cipher_operation"
        ) as mock_cipher_operation:
            manager.encrypt_text()

            mock_cipher_operation.assert_called_once_with(operation_type="encrypt")

    def test_decrypt_text_should_enable_make_cipher_operation_make_call(self, manager):
        with patch.object(
            manager, "_Manager__make_cipher_operation"
        ) as mock_cipher_operation:
            manager.decrypt_text()

            mock_cipher_operation.assert_called_once_with(operation_type="decrypt")

    def test_encrypt_text_make_cipher_operation_should_encrypt_text(
        self, manager, mock_cipher_facade, mock_buffer
    ):
        manager.cipher_facade.check_cipher_type = Mock()
        mock_buffer.add = Mock()
        manager.buffer = mock_buffer
        with patch("builtins.input", side_effect=["hello", "rot13"]):
            manager.encrypt_text()

            manager.buffer.add.assert_called_once_with(
                content=ANY, rot_type="rot13", status="encrypted"
            )

    def test_make_cipher_operation_should_decrypt_text(
        self, manager, mock_cipher_facade, mock_buffer
    ):
        manager.cipher_facade.check_cipher_type = Mock()
        mock_buffer.add = Mock()
        manager.buffer = mock_buffer
        with patch("builtins.input", side_effect=["hello", "rot13"]):
            manager.decrypt_text()

            manager.buffer.add.assert_called_once_with(
                content=ANY, rot_type="rot13", status="decrypted"
            )

    def test_make_cipher_operation_should_use_error_cipher_not_found(
        self, manager, mock_cipher_facade
    ):
        manager.cipher_facade.check_cipher_type = Mock()
        with patch("builtins.input", side_effect=["hello", "rot_47"]):
            with patch("builtins.print") as mock_print:
                manager._Manager__make_cipher_operation("invalid_option")
                assert (
                    mock_print.call_args_list[1][0][0]
                    == "Invalid operation type: invalid_option"
                )

    def test_display_buffer_should_enable_buffer_display(self, manager, mock_buffer):
        mock_buffer.display = Mock()

        with patch("builtins.print"):
            manager.display_buffer()

        mock_buffer.display.assert_called_once_with()

    def test_clear_all_should_enable_clear_buffer(self, manager, mock_buffer):
        mock_buffer.clear_all = Mock()

        with patch("builtins.print"):
            manager.clear_buffer()

        mock_buffer.clear_all.assert_called_once_with()

    def test_save_to_file_should_handle_empty_buffer(
        self, manager, mock_file_handler, mock_buffer
    ):
        mock_buffer.storage = []

        with patch("builtins.print") as mock_print:
            manager.save_to_file()

        mock_print.assert_any_call("Buffer is empty. Nothing to save.")

    def test_save_to_file_should_use_file_handler(
        self, manager, mock_file_handler, mock_buffer
    ):
        with patch("builtins.input", side_effect=["filename.json", "w"]):
            with patch("builtins.print"):
                manager.save_to_file()

        mock_file_handler.save_to_file.assert_called_once_with(
            mock_buffer, "filename.json", "w"
        )

    def test_save_to_file_should_use_exception(
        self, manager, mock_file_handler, mock_buffer
    ):
        manager.buffer = mock_buffer
        manager.file_handler.save_to_file.side_effect = Exception(
            "Something went wrong"
        )

        with patch("builtins.input", side_effect=["filename.json", "w"]):
            with patch("builtins.print") as mock_print:
                manager.save_to_file()
                mock_print.assert_any_call(
                    "An error occurred while saving to file: Something went wrong"
                )

    def test_load_from_file_should_use_file_handler(
        self, manager, mock_file_handler, mock_buffer
    ):
        manager.file_handler.load_from_file = Mock()

        with patch("builtins.input", side_effect=["filename.json"]):
            with patch("builtins.print") as mock_print:
                manager.load_from_file()

                manager.file_handler.load_from_file.assert_called_once()
                mock_print.assert_any_call(
                    "Data successfully loaded from filename.json."
                )

    def test_load_from_file_should_use_exception(
        self, manager, mock_file_handler, mock_buffer
    ):
        manager.file_handler.load_from_file.side_effect = Exception(
            "Something went wrong"
        )

        with patch("builtins.input", side_effect=["filename.json"]):
            with patch("builtins.print") as mock_print:
                manager.load_from_file()

                mock_print.assert_any_call(
                    "An error occurred while loading from file: Something went wrong"
                )

    def test_exit_program_should_set_is_running_to_false(self, manager):
        with patch("builtins.print") as mock_print:
            manager.exit_program()

        mock_print.assert_called_once_with("\nExiting application. Goodbye!")
        assert manager.is_running == False

    def test_run_should_execute_action_based_on_menu_choice(self, manager, mock_menu):
        manager.menu.get_choice.side_effect = [1, 7]
        with patch.object(manager, "encrypt_text") as mock_encrypt_text:
            manager.run()

        mock_encrypt_text.assert_called_once()

    def test_run_should_handle_invalid_choice(self, manager, mock_menu):
        manager.menu.get_choice.side_effect = [9, 7]
        with patch("builtins.print") as mock_print:
            manager.run()
        assert mock_print.call_args_list[0][0][0] == "Invalid choice: 9"
