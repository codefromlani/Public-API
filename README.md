Public API

This project is a simple Flask-based web application that exposes a public API. The API responds with three pieces of information when someone makes a request to it


API Endpoint
- GET /api
 Example Response
    {
    "email": "rodiathammed48@gmail.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/codefromlani/Public-API.git"
    }


Requirements
To run this project locally, you need to have Python and the required packages installed.

- Python (>=3.6)
- Flask
- pytz


Installation
Clone the repository:

- git clone https://github.com/codefromlani/Public-API.git
- cd Public-API

Create a virtual environment:

- python -m venv venv
`venv\Scripts\activate` # to activate on Windows 
source venv/bin/activate # Mac/os

Install the required dependencies:

- pip install -r requirements.txt

Run the Flask app:

- python app.py
The API will be available at http://127.0.0.1:5000/api.

Dependencies

Flask - A lightweight WSGI web application framework for Python.
pytz - A Python library for working with timezones.


If you're looking for talented Python developers, you can check out: https://hng.tech/hire/python-developers