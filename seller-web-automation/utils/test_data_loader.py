"""
Test data loading module with caching and validation.

Provides centralized test data management with:
- Automatic JSON file loading
- LRU caching to avoid repeated file I/O
- Error handling for missing or malformed files
- Support for environment-specific overrides
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional
from functools import lru_cache
from config import settings
from utils.logger import setup_logger

logger = setup_logger(__name__)


class TestDataLoader:
    """
    Load and cache test data from JSON files.

    Implements LRU caching to avoid repeated file reads,
    improving test execution performance.
    """

    BASE_DIR = settings.TEST_DATA_DIR

    @classmethod
    @lru_cache(maxsize=32)
    def load(cls, module_name: str) -> Dict[str, Any]:
        """
        Load test data for given module with caching.

        Args:
            module_name: Name of test module (e.g., 'login', 'registration')
                        Corresponds to JSON file: {module_name}_test_data.json

        Returns:
            Dictionary containing test data

        Raises:
            FileNotFoundError: If test data file doesn't exist
            json.JSONDecodeError: If JSON file is malformed

        Example:
            >>> data = TestDataLoader.load('login')
            >>> email = data['valid_credentials']['email']
        """
        json_file = cls.BASE_DIR / f"{module_name}_test_data.json"

        if not json_file.exists():
            # Fallback: strip category suffix (e.g. employee_functional → employee)
            suffixes = ["_functional", "_ui", "_security", "_validation", "_e2e",
                        "_search", "_boundary", "_files"]
            base_name = module_name
            for suffix in suffixes:
                if base_name.endswith(suffix):
                    base_name = base_name[: -len(suffix)]
                    break
            fallback_file = cls.BASE_DIR / f"{base_name}_test_data.json"
            if fallback_file.exists():
                logger.info(f"Fallback: {module_name} → {base_name}_test_data.json")
                json_file = fallback_file
            else:
                # Try without underscores (shop_create → shopcreate, product_create → productcreate)
                no_underscore = base_name.replace("_", "")
                no_us_file = cls.BASE_DIR / f"{no_underscore}_test_data.json"
                if no_us_file.exists():
                    logger.info(f"Fallback: {module_name} → {no_underscore}_test_data.json")
                    json_file = no_us_file
                else:
                    error_msg = f"Test data file not found: {json_file}"
                    logger.error(error_msg)
                    raise FileNotFoundError(error_msg)

        try:
            with open(json_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            logger.info(f"Loaded test data from {json_file.name}")
            logger.debug(f"Test data keys: {list(data.keys())}")

            return data

        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON in {json_file}: {e}"
            logger.error(error_msg)
            raise json.JSONDecodeError(
                f"Failed to parse {json_file}",
                e.doc,
                e.pos
            ) from e

        except Exception as e:
            logger.error(f"Unexpected error loading {json_file}: {str(e)}")
            raise

    @classmethod
    def load_with_defaults(
        cls,
        module_name: str,
        defaults: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Load test data with default fallback values.

        Args:
            module_name: Name of test module
            defaults: Default values to use if file not found

        Returns:
            Test data dictionary (loaded or defaults)

        Example:
            >>> defaults = {"timeout": 5000}
            >>> data = TestDataLoader.load_with_defaults('config', defaults)
        """
        try:
            return cls.load(module_name)
        except FileNotFoundError:
            logger.warning(
                f"Test data file for '{module_name}' not found. "
                f"Using defaults: {defaults}"
            )
            return defaults or {}

    @classmethod
    def get_value(
        cls,
        module_name: str,
        key_path: str,
        default: Any = None
    ) -> Any:
        """
        Get specific value from test data using dot notation.

        Args:
            module_name: Name of test module
            key_path: Dot-separated path to value (e.g., 'user.credentials.email')
            default: Default value if key not found

        Returns:
            Value at specified path or default

        Example:
            >>> email = TestDataLoader.get_value(
            ...     'login',
            ...     'valid_credentials.email',
            ...     'default@example.com'
            ... )
        """
        try:
            data = cls.load(module_name)

            # Navigate nested dictionary using dot notation
            keys = key_path.split('.')
            value = data

            for key in keys:
                if isinstance(value, dict):
                    value = value.get(key)
                else:
                    logger.warning(
                        f"Cannot navigate to '{key}' in non-dict value: {value}"
                    )
                    return default

            return value if value is not None else default

        except (FileNotFoundError, KeyError) as e:
            logger.warning(
                f"Could not get value at '{key_path}' from '{module_name}': {e}"
            )
            return default

    @classmethod
    def load_for_env(cls, module_name: str, env: str = 'dev') -> Dict[str, Any]:
        """
        Load test data with environment-specific overrides.

        Looks for environment-specific file first (e.g., login_test_data_staging.json),
        falls back to base file (login_test_data.json).

        Args:
            module_name: Name of test module
            env: Environment name ('dev', 'staging', 'prod')

        Returns:
            Test data dictionary with environment overrides

        Example:
            >>> # Loads staging-specific data if available
            >>> data = TestDataLoader.load_for_env('login', env='staging')
        """
        # Try environment-specific file first
        env_file = cls.BASE_DIR / f"{module_name}_test_data_{env}.json"

        if env_file.exists():
            logger.info(f"Using environment-specific data: {env_file.name}")
            with open(env_file, "r", encoding="utf-8") as f:
                return json.load(f)

        # Fall back to base file
        logger.info(f"No environment-specific file for '{env}', using base data")
        return cls.load(module_name)

    @classmethod
    def clear_cache(cls) -> None:
        """
        Clear the LRU cache, forcing fresh file reads.

        Useful when test data files are modified during test execution.

        Example:
            >>> TestDataLoader.clear_cache()
            >>> data = TestDataLoader.load('login')  # Fresh read from file
        """
        cls.load.cache_clear()
        logger.info("Test data cache cleared")

    @classmethod
    def list_available_modules(cls) -> list:
        """
        List all available test data modules.

        Returns:
            List of module names (without _test_data.json suffix)

        Example:
            >>> modules = TestDataLoader.list_available_modules()
            >>> print(modules)
            ['login', 'registration', 'becomeseller']
        """
        if not cls.BASE_DIR.exists():
            logger.warning(f"Test data directory not found: {cls.BASE_DIR}")
            return []

        json_files = cls.BASE_DIR.glob("*_test_data.json")
        modules = [
            f.stem.replace('_test_data', '')
            for f in json_files
        ]

        logger.debug(f"Available test data modules: {modules}")
        return sorted(modules)


# Convenience function for backward compatibility
def load_test_data(module_name: str) -> Dict[str, Any]:
    """
    Load test data for module (convenience function).

    Args:
        module_name: Name of test module

    Returns:
        Dictionary containing test data

    Example:
        >>> from utils.test_data_loader import load_test_data
        >>> data = load_test_data('login')
    """
    return TestDataLoader.load(module_name)