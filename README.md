# Password Manager

## Overview
This is a secure and user-friendly **Password Manager** application built using Python, Tkinter for the graphical user interface, MySQL for storing encrypted passwords, and the `cryptography` library for encryption and decryption of sensitive data.

The application allows users to:
- **Add** passwords for different websites securely.
- **Retrieve** passwords, ensuring encryption during storage and secure decryption upon retrieval.

## Features
- **Secure Encryption**: Uses the `Fernet` module from the `cryptography` package to encrypt passwords before storing them in the database.
- **Environment Variables**: Connects to the MySQL database using credentials stored in environment variables, improving security.
- **Intuitive GUI**: Built using Tkinter, providing an easy-to-use interface to manage passwords.
  
## Tech Stack
- **Python 3.x**
- **Tkinter** for the graphical interface
- **MySQL** for the database backend
- **cryptography** for password encryption and decryption

## Prerequisites
- **Python 3.x**
- **MySQL**
- Required Python packages: 
  - `mysql-connector-python`
  - `cryptography`
