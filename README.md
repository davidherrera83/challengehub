# OpenAlgoCode

Welcome to OpenAlgoCode, where we strive to make algorithm and coding challenges accessible to everyone. This repository features a curated selection of problems from top platforms like LeetCode, HackerRank, and Codeforces. Whether you're prepping for interviews or simply love solving problems, OpenAlgoCode offers diverse challenges to help you enhance your coding skills and algorithmic thinking. Join us, solve problems, and level up your coding expertise!

## Table of Contents

- [Getting Started](#getting-started)
- [Folder Structure](#folder-structure)
- [Test Frameworks](#test-frameworks)
- [How to Contribute](#how-to-contribute)
- [License](#license)

## Getting Started

To begin solving the challenges in this repository, follow these steps:

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/openalgocode.git
    cd openalgocode
    ```

2. **Set up a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Folder Structure

The repository is organized into difficulty levels, and each level is further divided into common topics:

    openalgocode/
    ├── easy/
    │   ├── arrays/
    │   ├── strings/
    │   ├── linked_lists/
    │   ├── trees/
    │   ├── sorting/
    │   ├── searching/
    │   ├── dynamic_programming/
    │   └── miscellaneous/
    ├── medium/
    │   ├── arrays/
    │   ├── strings/
    │   ├── linked_lists/
    │   ├── trees/
    │   ├── graphs/
    │   ├── sorting/
    │   ├── searching/
    │   ├── dynamic_programming/
    │   └── miscellaneous/
    └── hard/
        ├── arrays/
        ├── strings/
        ├── linked_lists/
        ├── trees/
        ├── graphs/
        ├── sorting/
        ├── searching/
        ├── dynamic_programming/
        └── miscellaneous/

Each folder contains Python scripts that solve specific problems. The naming convention for the scripts is `problem_name.py` to make it easier to identify the challenges.

## Test Frameworks

OpenAlgoCode uses Python with Pytest and Pyleniumio to focus on algorithm solutions while demonstrating proficiency in testing:

### Unit Testing Frameworks

- **Pytest:** A robust and flexible testing framework for Python.

### End-to-End Testing Frameworks

- **Pyleniumio:** Combines the power of Selenium WebDriver with the simplicity of Pytest for end-to-end testing.

### Static Code Analysis and Linting

- **Flake8:** For linting Python code.
- **pylint:** Another popular Python linter.

Each of these frameworks is represented in the repository with examples and best practices to demonstrate testing skills and proficiency in automation.

## How to Contribute

We welcome contributions from the community! If you'd like to add a new problem or improve an existing solution, please follow these steps:

1. **Fork the repository:**

    Click the "Fork" button on the top right of this page to create a copy of this repository in your GitHub account.

2. **Clone your fork:**

    ```sh
    git clone https://github.com/yourusername/openalgocode.git
    cd openalgocode
    ```

3. **Create a new branch:**

    ```sh
    git checkout -b your-feature-branch
    ```

4. **Make your changes and commit them:**

    ```sh
    git add .
    git commit -m "Description of your changes"
    ```

5. **Push to your fork and submit a pull request:**

    ```sh
    git push origin your-feature-branch
    ```

    Open a pull request on the original repository and describe your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
