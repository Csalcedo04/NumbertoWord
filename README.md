# Number to Words Converter

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## Description

This project is a proposed solution for a Google interview question involving converting numbers into words. The program takes an integer as input and returns its English word representation.

## Example

- Input: `438237764`
- Output: `Four Hundred Thirty Eight Million Two Hundred Thirty Seven Thousand Seven Hundred Sixty Four`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/number-to-words.git
    ```

2. Navigate to the project directory:

    ```bash
    cd number-to-words
    ```

3. (Optional) Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

To use the number-to-words converter, simply import and use the `NumberToWords` class in your code:

```python
from number2string import NumberToWords

converter = NumberToWords()
result = converter.number2string(438237764)
print(result)  # Output: Four Hundred Thirty Eight Million Two Hundred Thirty Seven Thousand Seven Hundred Sixty Four
