# Indian Sign Language Conversion Tool

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Steps to Install](#steps-to-install)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [How to Convert Text to ISL](#how-to-convert-text-to-isl)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The **Indian Sign Language Conversion Tool** is a web application designed to convert text input into corresponding Indian Sign Language (ISL) images. This tool helps in bridging communication gaps between the hearing-impaired community and others.

## Features

- Converts alphabets (A-Z) and numbers (0-9) into ISL images.
- User-friendly web interface with support for batch processing.
- Built with Flask for the backend and responsive front-end design.

## Technologies Used

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning Model:** TensorFlow
- **Database:** None (static mapping used)

## Installation

### Prerequisites

1. Python 3.8 or higher
2. Pip (Python package manager)
3. Git (optional, for cloning the repository)
4. Virtual Environment (recommended)

### Steps to Install

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repo/ISLAR.git
   ```
2. Navigate to the project directory:

   ```bash
   cd ISLAR
   ```

3. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. Start the Flask server:

   ```bash
   python app.py
   ```

2. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

### How to Convert Text to ISL

1. Enter text (alphabets A-Z or numbers 0-9) into the input box.
2. Click on the **Convert** button.
3. View the corresponding ISL images displayed on the screen.

## Folder Structure

```
ISLAR/
├── app.py                  # Flask application file
├── requirements.txt        # Dependencies
├── static/                 # Static assets (CSS, images, etc.)
├── templates/              # HTML templates
├── models/                 # Pretrained model files
├── dataset/                # ISL dataset (alphabets and numericals)
└── README.md               # Project README
```

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Submit a pull request with detailed explanations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
