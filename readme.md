# Description
This is a simple example of a test automation framework based on `pytest` and `selenium`.  
It's testing search engines `Google` and `Bing`.

# Requirements
- Python 3.11.3
- Supported operating systems: Linux, macOS, Windows

# Features:
- Automatic download of the required web drivers
- Page Object Model
- Custom wrapper around `selenium` with automatic wait
- Execution parallelization
- Customizable browser type
- Customizable browser window size

# Installation
1. [Download and install Python 3.11.3](https://www.python.org/downloads/release/python-3113/)
2. Clone the framework
3. Open a terminal window and navigate to the framework's root directory
4. Create a virtual environment:
    ```commandline 
    python -m venv venv
    ```
5. Activate the virtual environment:
    * POSIX:
      ```commandline 
      source venv/bin/activate
      ```
    * Windows:
      ```commandline 
      venv\Scripts\activate.bat
      ```
6. Install dependencies:
     ```commandline 
     pip install -r requirements.txt
     ```

# Running Tests:
To run tests, navigate to the framework's root directory.

## CLI Options
- All the pytest's options - [see documentation](https://docs.pytest.org/en/6.2.x/usage.html)
- --browser
    - Required: yes
    - Default value: none
    - Options: chrome, firefox
- --headless
    - Required: yes
    - Default value: True
    - Options: True, False
- --browser_width
    - Required: yes
    - Default value: 1920
- --browser_height
    - Required: yes
    - Default value: 1080
- --search_string
    - Required: no
    - Default value: none

### Example Command:
```commandline
pytest --browser="firefox" --search_string="quantum" "tests/search_results/test_search_engine_results.py"
```
