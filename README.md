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

## Creating `requirements.txt`

To generate a `requirements.txt` file that includes all the currently installed packages in your virtual environment, follow these steps:

1. **Activate your virtual environment** (if not already activated):

   ```sh
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```

2. **Install the necessary packages**:

   ```sh
   pip install pytest flake8 pylint
   ```

3. **Generate the `requirements.txt` file**:

   ```sh
   pip freeze > requirements.txt
   ```

## Folder Structure

The directory is organized into three main difficulty levels: `easy`, `medium`, and `hard`. Each level contains various categories of algorithm problems, and each category includes both the problem implementations and their corresponding tests.

```plaintext
openalgocode/
├── easy/
│   ├── arrays/
│   │   ├── tests/
│   │   │   └── test_arrays.py
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

OpenAlgoCode uses Python with Pytest to focus on algorithm solutions while demonstrating proficiency in testing:

### Unit Testing Frameworks

- **Pytest:** A robust and flexible testing framework for Python.

### Static Code Analysis and Linting

- **Flake8:** For linting Python code.
- **pylint:** Another popular Python linter.

Each of these frameworks is represented in the repository with examples and best practices to demonstrate testing skills and proficiency in automation.

## Note on Solution Optimization

The solutions provided in this repository prioritize readability and understanding of the logic. While some solutions may not be the most optimized in terms of time and space complexity, they are written to be clear and easy to follow. This approach helps in understanding the fundamental concepts and logic behind each algorithm.

## How to Contribute

We welcome contributions from the community! If you'd like to add a new problem or improve an existing solution, please follow these steps:

1. **Fork the repository:**

   Click the "Fork" button on the top right of this page to create a copy of this repository under your GitHub account.

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

5. **Push to your fork:**

   ```sh
   git push origin your-feature-branch
   ```

6. **Submit a pull request:**

   Open a pull request on the original repository and describe your changes.

### Why Forking?

Forking is a common and recommended practice for contributing to open source projects. It allows you to make changes freely in your own copy of the repository and submit those changes for review via a pull request. This process ensures that all contributions are reviewed and approved by the maintainers before being merged, maintaining the integrity and quality of the codebase.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
