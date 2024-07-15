import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["sqlite3"],  # Include sqlite3 module if required
    "include_files": [("data/library.db", "data/library.db")],  # Include the database file
    "include_msvcr": True  # Include MSVC runtime DLLs if required
}

executables = [
    Executable("library.py", base=None)  # Use None base for console application
]

setup(
    name="LibraryManagementSystem",
    version="0.1",
    description="Library Management System",
    options={"build_exe": build_exe_options},
    executables=executables
)
