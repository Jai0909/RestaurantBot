

# Restaurant Bot App

## Description
The Restaurant Bot App is a web application designed to assist in the management of restaurant operations. This Python-based application features functionalities for handling menu updates, managing image uploads, generating dynamic reports, and managing supplier interactions.

## Features
- Manage menu updates and image uploads for menus.
- Generate PDF reports and graphical insights.
- Supplier management: track and order inventory, manage supplier details.
- User-friendly web interface.

## General Requirements
### Software
- Operating System: Any system that can run Python (Windows, macOS, Linux)
- MySQL Server: For database management
- Python 3.6 or higher: Required for running the Python script
- Pip: Python package installer, used to install dependencies from the requirements.txt file

### Hardware
- Processor: Minimum 1GHz or faster
- RAM: At least 2GB
- Storage: Minimum 100MB free space for installation

## Installation

### Clone the Repository
To get started with the Restaurant Bot App, clone the repository to your local machine by using the following command:

```bash
git clone https://github.com/yourusername/restaurant-bot-app.git
cd restaurant-bot-app
```

### Install Dependencies (For running from the Python script)
To run the application from the Python script, first ensure that you have Python and pip installed on your system. Then install the required Python libraries using the `requirements.txt` file provided in the repository. This can be done with the following commands:

```bash
# Ensure pip, setuptools, and wheel are up to date
python -m pip install --upgrade pip setuptools wheel

# Install required libraries
pip install -r requirements.txt
```

### Database Setup
Before running the application, you need to set up the MySQL database using the provided SQL dump file:

1. **Install MySQL**: Ensure that MySQL is installed on your machine. Installation guides are available on the MySQL official website (https://dev.mysql.com/doc/refman/8.0/en/installing.html).

2. **Load Database Dump**: Import the SQL dump file into MySQL to create and populate the database. Use the following command:

    ```bash
    mysql -u username -p < /path/to/db.sql
    ```

    Replace `username` with your MySQL username and `/path/to/db.sql` with the actual path to the downloaded SQL file. This step will create the necessary database structure and fill it with initial data required for the application to function properly.

### Database Connection
The application connects to a MySQL database using the following connection settings:

```python
connection = pymysql.connect(host="localhost", user="root", password="pwd", database="restaurant", port=3306)
```
- **host**: The server where your MySQL database is hosted (usually "localhost" for local installations).
- **user**: The username used to access the database (e.g., "root").
- **password**: The password for the database user.
- **database**: The name of the database to connect to.
- **port**: The port number MySQL is running on, typically 3306 for MySQL.

Ensure these settings are correctly configured in your environment. For security reasons, avoid using root in production and keep sensitive information such as passwords out of version control.

## Usage

### Running the Application from Python Script
To run the Restaurant Bot App from the Python script, execute the following command:

```bash
python app.py
```

### Running the Precompiled Executables
No installation of dependencies is required to run the precompiled executables. Navigate to the respective output directory and run the executable for your operating system.

#### On Linux
Navigate to the `linux_output/app` directory and execute:

```bash
./app
```

#### On Windows
Navigate to the `windows_output/app` directory and execute:

```bash
app.exe
```


## Contact
For any queries or further assistance, please contact [jai090901@gmail.com](mailto:jai090901@gmail.com).
