
import logging
from pathlib import Path
from colorlog import ColoredFormatter


# Create logger
logger = logging.getLogger("login_system")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers
if not logger.handlers:

    # Create log file path
    log_file = Path(__file__).parent / "login.log"

    # Create file handler
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Normal formatter for file
    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)-8s - %(message)s"
    )

    # Colour formatter for console
    console_formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)-8s - %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bold",
        },
    )

    # Apply formatters
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    # Attach handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

logger.propagate = False
