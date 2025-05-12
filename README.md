# 🔐 Project Cipher

**Project Cipher** is a Python-based application that allows you to encrypt and decrypt text using classic cipher algorithm of Caesar cipher with ROT13 and ROT47 algorithms.

## Content of Project

* [General information](#general-information)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)
* [Testing](#testing)
* [Usage](#usage)

## General info

A simple Python implementation of Caesar cipher with ROT13 and ROT47 variants.<br><br>
This project was created as a learning exercise to understand basic cryptographic concepts and Python programming.
The Caesar cipher is one of the simplest and most widely known encryption techniques. 
It is a type of substitution cipher where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.<br><br>
- <b>ROT13:</b> Shifts each character by 13 positions in the alphabet.<br>
- <b>ROT47:</b> Uses all printable characters of ASCII (from "!" to "~") and shifts each by 47 positions.

## Features

- Encrypt and decrypt text directly from the terminal
- Supports ROT13 and ROT47 cipher algorithms
- Exception handling for unsupported cipher types
- Unit tests written using `pytest`

## Technologies

  Project is created with:
  <ul>
    <li>Python 3.12</li>
    <li>pytest</li>
  </ul>

## Setup

  To run this project, install it locally:<br><br>
```git clone https://github.com/MagdalenaOkuniewska/Project_Cipher.git```<br/>
```cd Project_Cipher```<br/>
No additional dependencies are required to run the basic functionality. <br/><br/>
For running tests, install pytest:<br><br>
```pip install pytest```


## Testing

Tests are written using pytest. To run the tests:<br><br>
```pytest```<br/><br>
The tests verify the correct functionality of both ROT13 and ROT47 implementations, ensuring that encryption and decryption work as expected with various inputs.<br>

## Usage
<details>
<summary>Click here to see the example usage of <b>Project Cipher</b>!</summary><br>
The project uses a facade pattern to provide a simple interface for different cipher implementations.<br>
Currently, it supports ROT13 and ROT47 variants of the Caesar cipher.<br><br>
You can run the application directly using the `main.py` file:<br>

```python main.py```<br>
By default, the script will prompt you to choose a cipher type and enter the text to encrypt or decrypt.

<h3>Basic Usage with CipherFacade</h3>
  
```
from cipher import CipherFacade

# Create a cipher facade
cipher_facade = CipherFacade()

# Encrypt a message using ROT13
encrypted_rot13 = cipher_facade.encrypt("Hello World!", "rot13")
print(f"ROT13 Encrypted: {encrypted_rot13}")

# Decrypt the ROT13 message
decrypted_rot13 = cipher_facade.decrypt(encrypted_rot13, "rot13")
print(f"ROT13 Decrypted: {decrypted_rot13}")

# Encrypt a message using ROT47
encrypted_rot47 = cipher_facade.encrypt("Hello World!", "rot47")
print(f"ROT47 Encrypted: {encrypted_rot47}")

# Decrypt the ROT47 message
decrypted_rot47 = cipher_facade.decrypt(encrypted_rot47, "rot47")
print(f"ROT47 Decrypted: {decrypted_rot47}")
```

</details>
