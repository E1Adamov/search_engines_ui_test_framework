__doc__ = """
    Allows running tests in debug mode from your IDE
    propagates CLI arguments passed to this script to pytest
    and adds a few on top, to make debugging process easier
"""


import sys

import pytest


def main() -> int | pytest.ExitCode:
    result = pytest.main(args=[
        "--headless=False",
        "--log-cli-level=DEBUG",
        *sys.argv[1:]
    ])
    return result


if __name__ == '__main__':
    pytest_result = main()
    exit_code = int(pytest_result)
    sys.exit(exit_code)
