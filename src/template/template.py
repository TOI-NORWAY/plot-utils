"""Template module."""


import logging

# Always use the module-level logger, so that it can be configured by the end user.
# Logging configuration should be done by the end user, not in the module.
logger = logging.getLogger(__name__)


def hello():
    """Hello world."""

    logger.info("Hello world!")

    print("Hello world!")
