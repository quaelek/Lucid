# Lucid Dream Interpreter

Lucid is a web application that interprets dreams in an esoteric fashion using OpenAI's GPT-3.5-turbo model. Users can describe their dreams, and Lucid will provide an interpretation based on the input.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [License](#license)

## Features

1. Interpret dreams using OpenAI's GPT-3.5-turbo model
2. Engaging user interface with animations
3. Responsive design for desktop and mobile devices

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/quaelek/Lucid.git
    cd lucid
    pip install -r requirements.txt
    ```

2. Set up your OpenAI API key as an environment variable:

    ```bash
    export OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. Run the Flask application:

    ```bash
    python app.py
    ```

2. Open your browser and navigate to http://127.0.0.1:5000/ to access the Lucid Dream Interpreter web application.

3. Enter a dream description into the input field and click the "Interpret my dream" button or press enter.

4. The app will display the interpretation of your dream.

## Technologies

- Python
- Flask
- OpenAI API
- HTML
- CSS
- JavaScript (and jQuery)
- Heroku (optional)

## License

This project is licensed under the MIT License.
