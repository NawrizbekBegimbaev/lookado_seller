"""
JSON schema validation for test data.

Provides schema validation to ensure test data files are well-formed
and contain required fields before tests execute.
"""

from typing import Dict, Any
from utils.logger import setup_logger

logger = setup_logger(__name__)

# Try to import jsonschema, but don't fail if not installed
try:
    import jsonschema
    from jsonschema import validate, ValidationError
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    logger.warning(
        "jsonschema package not installed. Install with: pip install jsonschema"
    )


class TestDataValidator:
    """
    Validate test data against JSON schemas.

    Ensures test data files contain required fields and correct data types
    before tests execute, preventing runtime errors.
    """

    # ==================== Schema Definitions ====================

    LOGIN_SCHEMA = {
        "type": "object",
        "properties": {
            "valid_credentials": {
                "type": "object",
                "required": ["email", "password"],
                "properties": {
                    "email": {"type": "string", "format": "email"},
                    "password": {"type": "string", "minLength": 8}
                }
            },
            "invalid_email": {"type": "string"},
            "short_password": {"type": "string"},
            "wrong_password": {"type": "string"}
        },
        "required": ["valid_credentials"]
    }

    REGISTRATION_SCHEMA = {
        "type": "object",
        "properties": {
            "valid_data": {
                "type": "object",
                "required": ["first_name", "phone", "email", "password"],
                "properties": {
                    "first_name": {"type": "string", "minLength": 1},
                    "phone": {
                        "type": "string",
                        "pattern": "^\\+998[0-9]{9}$"
                    },
                    "email": {"type": "string", "format": "email"},
                    "password": {"type": "string", "minLength": 8}
                }
            },
            "invalid_phone": {"type": "string"},
            "invalid_email": {"type": "string"},
            "weak_password": {"type": "string"},
            "invalid_name": {"type": "string"}
        },
        "required": ["valid_data"]
    }

    BECOMESELLER_SCHEMA = {
        "type": "object",
        "properties": {
            "valid_data": {
                "type": "object",
                "required": [
                    "organization_name",
                    "full_name",
                    "pinfl",
                    "passport_number",
                    "inn",
                    "bank_account"
                ],
                "properties": {
                    "organization_name": {"type": "string", "minLength": 3},
                    "full_name": {"type": "string", "minLength": 3},
                    "pinfl": {"type": "string", "pattern": "^[0-9]{14}$"},
                    "passport_number": {"type": "string"},
                    "inn": {"type": "string"},
                    "bank_account": {
                        "type": "object",
                        "required": ["account_name", "account_number", "mfo"],
                        "properties": {
                            "account_name": {"type": "string"},
                            "account_number": {"type": "string"},
                            "mfo": {"type": "string"}
                        }
                    }
                }
            },
            "login_credentials": {
                "type": "object",
                "required": ["email", "password"],
                "properties": {
                    "email": {"type": "string"},
                    "password": {"type": "string"}
                }
            }
        },
        "required": ["valid_data", "login_credentials"]
    }

    # ==================== Validation Methods ====================

    @classmethod
    def validate_login_data(cls, data: Dict[str, Any]) -> None:
        """
        Validate login test data against schema.

        Args:
            data: Login test data dictionary

        Raises:
            ValidationError: If data doesn't match schema

        Example:
            >>> data = {"valid_credentials": {"email": "test@example.com", "password": "pass1234"}}
            >>> TestDataValidator.validate_login_data(data)
        """
        if not JSONSCHEMA_AVAILABLE:
            logger.warning("Skipping validation - jsonschema not installed")
            return

        try:
            validate(instance=data, schema=cls.LOGIN_SCHEMA)
            logger.info("Login test data validation passed")
        except ValidationError as e:
            logger.error(f"Login test data validation failed: {e.message}")
            raise

    @classmethod
    def validate_registration_data(cls, data: Dict[str, Any]) -> None:
        """
        Validate registration test data against schema.

        Args:
            data: Registration test data dictionary

        Raises:
            ValidationError: If data doesn't match schema
        """
        if not JSONSCHEMA_AVAILABLE:
            logger.warning("Skipping validation - jsonschema not installed")
            return

        try:
            validate(instance=data, schema=cls.REGISTRATION_SCHEMA)
            logger.info("Registration test data validation passed")
        except ValidationError as e:
            logger.error(f"Registration test data validation failed: {e.message}")
            raise

    @classmethod
    def validate_becomeseller_data(cls, data: Dict[str, Any]) -> None:
        """
        Validate become seller test data against schema.

        Args:
            data: Become seller test data dictionary

        Raises:
            ValidationError: If data doesn't match schema
        """
        if not JSONSCHEMA_AVAILABLE:
            logger.warning("Skipping validation - jsonschema not installed")
            return

        try:
            validate(instance=data, schema=cls.BECOMESELLER_SCHEMA)
            logger.info("Become seller test data validation passed")
        except ValidationError as e:
            logger.error(f"Become seller test data validation failed: {e.message}")
            raise

    @classmethod
    def validate_by_module(cls, module_name: str, data: Dict[str, Any]) -> None:
        """
        Validate test data by module name.

        Args:
            module_name: Name of test module ('login', 'registration', 'becomeseller')
            data: Test data dictionary

        Raises:
            ValueError: If module_name is not recognized
            ValidationError: If data doesn't match schema

        Example:
            >>> TestDataValidator.validate_by_module('login', login_data)
        """
        validators = {
            'login': cls.validate_login_data,
            'registration': cls.validate_registration_data,
            'becomeseller': cls.validate_becomeseller_data,
        }

        validator = validators.get(module_name)

        if validator:
            validator(data)
        else:
            logger.warning(
                f"No validator defined for module '{module_name}'. "
                f"Available: {list(validators.keys())}"
            )

    @classmethod
    def validate_custom(cls, data: Dict[str, Any], schema: Dict[str, Any]) -> None:
        """
        Validate data against custom schema.

        Args:
            data: Data to validate
            schema: JSON schema definition

        Raises:
            ValidationError: If data doesn't match schema

        Example:
            >>> custom_schema = {"type": "object", "required": ["name"]}
            >>> TestDataValidator.validate_custom({"name": "Test"}, custom_schema)
        """
        if not JSONSCHEMA_AVAILABLE:
            logger.warning("Skipping validation - jsonschema not installed")
            return

        try:
            validate(instance=data, schema=schema)
            logger.info("Custom schema validation passed")
        except ValidationError as e:
            logger.error(f"Custom schema validation failed: {e.message}")
            raise


# Convenience function for quick validation
def validate_test_data(module_name: str, data: Dict[str, Any]) -> bool:
    """
    Validate test data and return success status.

    Args:
        module_name: Name of test module
        data: Test data dictionary

    Returns:
        True if validation passed, False otherwise

    Example:
        >>> if validate_test_data('login', data):
        ...     print("Data is valid")
    """
    try:
        TestDataValidator.validate_by_module(module_name, data)
        return True
    except Exception as e:
        logger.error(f"Validation failed: {e}")
        return False