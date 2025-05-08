from unittest.mock import patch, Mock, call
import tempfile
import json
import os
import json
import pytest
from files_service.file_handler import FileHandler
from buffer.text import Text


class TestFileHandler:

    @pytest.fixture
    def mock_buffer(self):
        buffer = Mock()
        buffer.storage = [
            Text("text1", "rot13", "encrypted"),
            Text("text2", "rot47", "decrypted"),
        ]
        return buffer

    @pytest.fixture
    def test_filename_json(self):
        return "test_filename.json"

    def test_buffer_to_dict_should_convert_buffer_items_to_dicts(self, mock_buffer):
        result = FileHandler.buffer_to_dict(mock_buffer)

        expected = [
            {"content": "text1", "rot_type": "rot13", "status": "encrypted"},
            {"content": "text2", "rot_type": "rot47", "status": "decrypted"},
        ]
        assert result == expected

    def test_get_filename_should_prompt_user_if_filename_is_none(self):
        with patch("builtins.input", return_value="filename.json") as mock_input:
            result = FileHandler.get_filename(None)

        mock_input.assert_any_call("Enter a filename: ")

        assert result == "filename.json"

    def test_get_filename_should_add_json_extension_if_missing(self):
        filename = "test_filename"
        result = FileHandler.get_filename(filename)

        assert result == "test_filename.json"

    def test_save_to_file_should_save_data_to_buffer_in_write_mode(self, mock_buffer):
        test_data = {
            "data": [
                {"content": "text1", "rot_type": "rot13", "status": "encrypted"},
                {"content": "text2", "rot_type": "rot47", "status": "decrypted"},
            ]
        }
        file_path = "test_filehandler_output.json"

        try:
            FileHandler.save_to_file(mock_buffer, file_path, "w")

            with open(file_path, "r") as infile:
                infile.seek(0)
                saved_data = json.load(infile)
                assert saved_data == test_data

        finally:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_save_to_file_should_use_append_mode_when_invalid_mode_is_given(
        self, mock_buffer, test_filename_json
    ):
        with patch("builtins.open") as mock_open:
            with patch("builtins.print") as mock_print:
                FileHandler.save_to_file(
                    mock_buffer, test_filename_json, "invalid_mode"
                )

        mock_open.assert_called_once_with(test_filename_json, "a", encoding="utf-8")
        mock_print.assert_any_call("Invalid mode. Setting up to default 'append' mode.")

    def test_save_to_file_should_use_file_not_found_error(
        self, mock_buffer, test_filename_json
    ):

        invalid_path = f"invalid_directory/{test_filename_json}"

        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch("builtins.print") as mock_print:
                FileHandler.save_to_file(mock_buffer, invalid_path, "w")
        mock_print.assert_called_once_with(f"File {invalid_path} not found.")

    def test_load_from_file_should_add_data_to_the_buffer(
        self, mock_buffer, test_filename_json
    ):
        test_data = {
            "data": [{"content": "text1", "rot_type": "rot13", "status": "encrypted"}]
        }

        with open(test_filename_json, mode="w", encoding="utf-8") as infile:
            json.dump(test_data, infile)
        try:
            FileHandler.load_from_file(mock_buffer, test_filename_json)
            mock_buffer.add_bulk.assert_called_once_with(test_data)

        finally:
            if os.path.exists(test_filename_json):
                os.remove(test_filename_json)

    def test_load_from_file_should_use_file_not_found_error(
        self, mock_buffer, test_filename_json
    ):

        invalid_path = f"invalid_directory/{test_filename_json}"

        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch("builtins.print") as mock_print:
                FileHandler.load_from_file(mock_buffer, invalid_path)
        mock_print.assert_called_once_with(f"File {invalid_path} not found.")

    def test_load_from_file_should_use_json_decoder_error(
        self, mock_buffer, test_filename_json
    ):
        test_data = {
            "data": [{"content": "text1", "rot_type": "rot13", "status": "encrypted"}]
        }

        with open(test_filename_json, mode="w", encoding="utf-8") as infile:
            json.dump(test_data, infile)

        decode_error = json.decoder.JSONDecodeError("invalid Json", doc="", pos=0)
        try:
            with patch("builtins.open", side_effect=decode_error):
                with patch("builtins.print") as mock_print:
                    FileHandler.load_from_file(mock_buffer, test_filename_json)
                    mock_print.assert_called_once_with(
                        f"File {test_filename_json} is not valid JSON."
                    )

        finally:
            if os.path.exists(test_filename_json):
                os.remove(test_filename_json)
