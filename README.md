# Library Management System

## Introduction
This project is a Library Management System built in Python. It allows managing customers, book rentals, penalties, and more.

## Features
- **Add Customer:** Add new customers to the system.
- **Add Book Rental:** Rent a book to a customer with specified rental and due dates.
- **List Customers:** Display a list of all customers.
- **List Current Rentals:** Show currently rented books with customer details.
- **List Overdue Rentals:** Display rentals that are overdue along with penalties.
- **Return Book:** Allow customers to return books, updating penalties if applicable.
- **Edit Customer Details:** Update customer information.
- **Exit:** Exit the program.

## Requirements
- Python 3.11
- SQLite (for database operations)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ammarhamzi/library-management-system.git
   cd library-management-system

## Usage

1. Through Terminal (VSCode or any terminal):
    ```bash
    python library.py
    
2. Using Executable (Windows):

  Download the zip file from Library Management System.
  Extract the zip file and run LIBRARY MANAGEMENT SYSTEM.exe.
  
## Files and Directories
  
library.py: Main Python script containing the Library Management System logic.
init_db.py: Script to initialize the SQLite database (library.db).
data/: Directory containing the SQLite database file library.db.
services.py, models.py, utils.py: Python modules for database operations, business logic, and utility functions.

## Contributing
Fork the repository, make changes, and submit a pull request.
For major changes, open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License - see the LICENSE file for details.









