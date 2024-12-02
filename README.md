# SQLite to JSON Converter

This Python script converts an SQLite database into a formatted JSON file. It simplifies the process of extracting database content and saving it in a JSON format for use in other applications or tools.

## Features
- Extracts all tables from an SQLite database.
- Automatically maps rows to a list of dictionaries.
- Outputs a human-readable JSON file with UTF-8 encoding.

## Prerequisites
- Python 3.x installed on your machine.
- SQLite database file (`.db`) to convert.

## How It Works
The script connects to an SQLite database, retrieves all table names, extracts data from each table, and saves the data in a structured JSON file.  

### Key Steps:
1. Connects to the SQLite database.
2. Retrieves table names using a query to `sqlite_master`.
3. Reads all rows and maps them into a dictionary format (column name -> value).
4. Saves the formatted data into a JSON file with proper indentation.
