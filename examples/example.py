"""Example usage of the template package."""


import logging

logging.basicConfig(level=logging.WARNING)

# Import all other packages/modules after logging is configured:
from template import hello

hello()
