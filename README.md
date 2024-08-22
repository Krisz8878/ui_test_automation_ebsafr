# Saucedemo Automated UI Tests

This repository contains automated UI tests for verifying the sorting functionality on the Saucedemo website.

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (make sure it's in your PATH)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/Krisz8878/ui_test_automation_ebsafr.git
    cd ui_test_automation_ebsafr
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

## Running Tests Locally

1. To run the tests and generate an HTML report:
    ```bash
    pytest --html=report.html
    ```

2. Open the generated `report.html` in your browser to view the results.

## Continuous Integration

This project is configured to run tests on GitHub Actions. The workflow file is located in `.github/workflows/ci.yml`.

## CI Status

![CI](https://github.com/yourusername/ui_test_automation_ebsafr/actions/workflows/ci.yml/badge.svg)
