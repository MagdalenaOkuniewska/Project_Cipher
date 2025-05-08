import pytest
from unittest.mock import patch, call
from buffer.buffer import Buffer
from buffer.text import Text


class TestBuffer:
    @pytest.fixture
    def empty_buffer(self):
        return Buffer()

    @pytest.fixture
    def filled_buffer(self):
        buffer = Buffer()
        buffer.storage = [
            Text(content="Hello", rot_type="ROT13", status="encrypted"),
            Text(content="Good morning", rot_type="ROT47", status="decrypted"),
        ]
        return buffer

    def test_init_should_create_empty_storage(self, empty_buffer):
        assert empty_buffer.storage == []

    def test_str_should_return_message_when_storage_empty(self, empty_buffer):
        assert str(empty_buffer) == "Buffer empty"

    def test_str_should_return_content_on_filled_buffer(self, filled_buffer):
        result = str(filled_buffer)
        assert "Buffer content:" in result
        assert "Hello" in result
        assert "Good morning" in result
        assert "ROT47" in result
        assert "encrypted" in result

    def test_add_should_append_text_to_storage(self, empty_buffer):
        empty_buffer.add("Test", "ROT13", "encrypted")

        assert empty_buffer.storage[0].content == "Test"
        assert empty_buffer.storage[0].rot_type == "ROT13"
        assert empty_buffer.storage[0].status == "encrypted"

        assert len(empty_buffer.storage) == 1

    def test_add_bulk_should_append_multiple_text_to_storage(self, empty_buffer):
        data = [
            {"content": "First", "rot_type": "ROT13", "status": "decrypted"},
            {"content": "Second", "rot_type": "ROT47", "status": "encrypted"},
        ]
        empty_buffer.add_bulk(data)

        assert empty_buffer.storage[0].content == "First"
        assert empty_buffer.storage[1].content == "Second"
        assert len(empty_buffer.storage) == 2

    def test_clear_all_should_clear_storage(self, filled_buffer):
        assert len(filled_buffer.storage) != 0
        filled_buffer.clear_all()
        assert filled_buffer.storage == []

    def test_display_on_empty_buffer(self, empty_buffer):
        with patch("builtins.print") as mock_print:
            empty_buffer.display()

        mock_print.assert_called_once_with("Buffer empty")

        assert mock_print.call_count == 1

    def test_display_on_filled_buffer(self, filled_buffer):
        with patch("builtins.print") as mock_print:
            filled_buffer.display()

        expected_calls = [
            call("Buffer content:"),
            call("1. ROT:[ROT13], STATUS[encrypted]: Hello"),
            call("2. ROT:[ROT47], STATUS[decrypted]: Good morning"),
        ]

        mock_print.assert_has_calls(expected_calls)

        assert mock_print.call_count == 3
