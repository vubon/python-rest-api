import os
import sys

if __name__ == '__main__':
    try:
        from core.management import command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Py Rest. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    command_line(sys.argv)

