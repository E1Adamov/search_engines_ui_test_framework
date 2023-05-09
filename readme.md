# Description
The framework is based on the ptest runner
It automatically downloads the required web drivers

# Installation
1. [download](https://www.python.org/downloads/release/python-3113/) and install Python 3.11.3
2. clone the framework
3. open a terminal window and navigate to the framework's root directory
4. create a virtual environment: 
    ```commandline 
    python -m venv <path to the framework root directory>/venv
    ```
5. activate the virtual environment:
   * POSIX:
     ```commandline 
     source venv/bin/activate
     ```
   * Windows:
     ```commandline 
     venv\Scripts\activate.bat
     ```
6. install dependencies: ``
     ```commandline 
     pip install -r requirements.txt
     ```

# Running tests:
In order to run test, you have to navigate to the framework's root directory

## CLI options
* all the pytest's option - [see documentation](https://docs.pytest.org/en/6.2.x/usage.html)
* --browser  
  `required`: yes  
  `default value`: none  
  `options`: chrome, firefox
* --headless  
  `required`: yes  
  `default value`: True  
  `options`: True, False
* --browser_width  
  `required`: yes  
  `default value`: 1920
* --browser_height  
  `required`: yes  
  `default value`: 1080
* --search_string  
  `required`: no  
  `default value`: none

For example, to run all the tests in 
[tests/search_results/test_search_engine_results.py](tests/search_results/test_search_engine_results.py) 
and pass the <search_string>="quantum", in a headless firefox browser, screen size 1920x1080, 
you should use this command:
```commandline
pytest --browser="firefox" --search_string="quantum" "tests/search_results/test_search_engine_results.py"
```