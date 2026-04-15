"""
Logging configuration module for test automation framework.

Provides centralized logging setup with:
- Console and file handlers
- Rotating file handler to prevent unbounded log growth
- Configurable log levels
- Structured log format with timestamps, module names, and line numbers
"""

import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional
from config import settings


def setup_logger(
    name: str,
    log_file: Optional[str] = None,
    level: Optional[int] = None
) -> logging.Logger:
    """
    Setup logger with console and file handlers.

    Args:
        name: Logger name (usually __name__ of the calling module)
        log_file: Optional log file name (will be created in logs/ directory)
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
               If None, uses settings.LOG_LEVEL

    Returns:
        Configured logger instance

    Example:
        >>> from utils.logger import setup_logger
        >>> logger = setup_logger(__name__, "test_execution.log")
        >>> logger.info("Test started")
    """
    logger = logging.getLogger(name)

    # Set log level
    if level is None:
        level = getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO)
    logger.setLevel(level)

    # Prevent duplicate handlers if logger already configured
    if logger.handlers:
        return logger

    # Create formatter with detailed information
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Console handler (stdout)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler (rotating) if log file specified
    if log_file:
        # Ensure logs directory exists
        settings.LOGS_DIR.mkdir(exist_ok=True, parents=True)

        log_path = settings.LOGS_DIR / log_file

        file_handler = RotatingFileHandler(
            filename=log_path,
            maxBytes=settings.LOG_FILE_MAX_BYTES,  # 10MB default
            backupCount=settings.LOG_BACKUP_COUNT,  # Keep 5 backups
            encoding='utf-8'
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.info(f"Logging to file: {log_path}")

    return logger


# Pre-configured loggers for common use cases
framework_logger = setup_logger("framework", "framework.log")
test_logger = setup_logger("tests", "test_execution.log")
page_logger = setup_logger("pages", "page_objects.log")