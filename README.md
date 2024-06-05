# 🌐🐍 - Flask JSON api using Python

This repository contains a simple Flask application for creating an API that handles JSON data. It also includes three Python scripts for interacting with the API.

## Contents

- [Description](#description)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Description

This Flask application serves as a foundation for building an API that can handle JSON data. It provides endpoints for storing, retrieving, and interacting with JSON data. The application includes the following key components:

- **`app_flask.py`**: The main Flask application that defines API endpoints and data handling.
- **`get.py`**: A Python script for making GET requests to retrieve data from the API.
- **`env.py`**: A Python script for making POST requests to send data to the API.
- **`chat.py`**: A Python script for sending chat messages to the API.

## Getting Started

To get started with this repository, follow these steps:

1. Clone the repository to your local machine:

  ```shell
  https://github.com/d4v1-sudo/flask-json-api.git
  ```

2. Set up a virtual environment (recommended) and install the required packages:

  ```shell
  cd flask-json-api
  python3 -m venv venv
  source venv/bin/activate # On Windows, use: venv\Scripts\activate
  pip install -r requirements.txt
  ```

3. Start the Flask application:

  ```shell
  python3 app_flask.py
  ```

The Flask application will run locally, and you can interact with it using the provided Python scripts (`get.py`, `env.py`, and `chat.py`).

## Usage

You can use the provided Python scripts to interact with the Flask API. Here's a brief overview of their usage:

- **`get.py`**: Use this script to make GET requests and retrieve data from the API.

- **`env.py`**: Use this script to make POST requests and send data to the API.

- **`chat.py`**: Use this script to send chat messages to the API.

Make sure to replace the placeholder URLs and routes in the scripts with your own API endpoint details.

## Contributing

If you'd like to contribute to this project, please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

<a href="https://visitorbadge.io/status?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2Fflask-json-api"><img src="https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2Fd4v1-sudo%2Fflask-json-api&label=Thanks%20for%20dropping%20in&labelColor=%23000000&countColor=%23FFFFFF" /></a>
