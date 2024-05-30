# This is a simple Flask based Backend Application


## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  
## Description

This API project is built using Python, Flask and SQL. It provides a simple yet powerful for posting and update, delete data within your local system. It can be used as a backend service for various applications.

## Features

- **CRUD Operations**: Perform Create, Read, Update, and Delete operations on employee records.
- **RESTful API**: Follows REST principles for designing APIs, making it easy to integrate with frontend and other backend systems.
- **PYtest Integration**: pytest is a test library used for testing python based application this project is tested using pytest library with a coverage of 86%(i am currently working on it and i will improve the test coverage).
- **Error Handling**: Implements robust error handling to provide informative responses in case of errors.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/UB2002/Backend-Flask-pytest.git
2. **Navigate to the project directory and Install dependencies:**
   ```bash
   pip install -r requirements.txt
   //run this command to install required libraries
## usage
 1. **start the server**
 
    ```bash
    EXPORT_FLASKAPP=run.py
 
 2.**database setup**

    ```bash
    flask db init
    flask db migrate
    flask db upgrade

3.**Runt tests**
    ```bash
    pytest
    //to get covrage report
    pytest --cov
    
