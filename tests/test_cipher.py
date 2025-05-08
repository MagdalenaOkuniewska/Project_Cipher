import pytest
from unittest.mock import patch, call
from cipher.cipher import (
    CipherROT13,
    CipherROT47,
    CipherFacade,
    Cipher,
    CipherNotFoundError,
)


class TestCiphers:
    @pytest.fixture
    def rot13_cipher(self):
        return CipherROT13()

    @pytest.fixture
    def rot47_cipher(self):
        return CipherROT47()

    @pytest.fixture
    def cipher_facade(self):
        return CipherFacade()

    @pytest.mark.parametrize("value,result", [("hello", "uryyb"), ("HELLO", "URYYB")])
    def test_rot13_should_encrypt_text_by_shifting_13_positions(
        self, value, result, rot13_cipher
    ):
        assert rot13_cipher.encrypt(value) == result

    def test_rot13_should_decrypt_text_back_to_original(self, rot13_cipher):
        assert rot13_cipher.decrypt("uryyb") == "hello"

    def test_rot13_should_only_change_letters(self, rot13_cipher):
        result = rot13_cipher.encrypt("a1b! c")
        assert result == "n1o! p"

    def test_rot47_should_encrypt_and_decrypt_text(self, rot47_cipher):
        text = "Hello123!"
        encrypted = rot47_cipher.encrypt(text)

        assert encrypted != text
        assert rot47_cipher.decrypt(encrypted) == text

    def test_rot47_should_shift_characters_by_47_positions(self, rot47_cipher):
        assert rot47_cipher.perform_shift("A", 47) == "p"
        assert rot47_cipher.perform_shift("!", 47) == "P"

    def test_rot47_should_shift_characters_from_33_to_126_ascii(self, rot47_cipher):
        text = "Hello\nWorld\t"

        assert rot47_cipher.perform_shift(text, 47) == "w6==@\n(@C=5\t"

    def test_facade_encrypt_with_correct_cipher_type(self, cipher_facade):
        text = "Hello World"

        assert cipher_facade.encrypt(text, "rot13") == "Uryyb Jbeyq"
        assert cipher_facade.encrypt(text, "rot47") != "Uryyb Jbeyq"

    def test_facade_decrypt_with_correct_cipher_type(self, cipher_facade):
        text = "Hello World"
        encrypted_rot13 = cipher_facade.encrypt(text, "rot13")
        encrypted_rot47 = cipher_facade.encrypt(text, "rot47")

        assert cipher_facade.decrypt(encrypted_rot13, "rot13") == text
        assert cipher_facade.decrypt(encrypted_rot47, "rot47") == text

    def test_facade_should_raise_error_for_invalid_cipher_type(self, cipher_facade):
        with pytest.raises(Exception) as exception_info:
            cipher_facade.check_cipher_type("invalid_cipher")

        assert str(exception_info.value)
