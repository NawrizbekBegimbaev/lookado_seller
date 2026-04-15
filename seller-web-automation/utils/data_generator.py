"""
Random test data generator for product creation tests.

Generates unique, randomized data for each test run to avoid
data conflicts and ensure test independence.
"""

import random
import string
from datetime import datetime
from typing import Dict, Any


class ProductDataGenerator:
    """
    Generates random product data for testing.

    Each run produces unique values to prevent:
    - SKU conflicts
    - Duplicate product names
    - Test data collision
    """

    # Available categories for random selection
    CATEGORIES = [
        {
            "main": "Мужчинам",
            "sub": "Одежда",
            "item": "Верхняя одежда"
        },
        {
            "main": "Мужчинам",
            "sub": "Одежда",
            "item": "Футболки и поло"
        },
    ]

    # Available brands
    BRANDS = ["PET PRIDE", "Zara", "Samsung", "LG", "Sony"]

    # Available countries
    COUNTRIES = ["Узбекистан", "Турция", "Россия", "Китай"]

    # IKPU options
    IKPU_OPTIONS = [
        "Rediska (007060060010000000)",
        "kurtkalar",
        "sviter",
    ]

    @staticmethod
    def generate_sku(prefix: str = "", length: int = 5) -> str:
        """
        Generate random unique SKU.

        Args:
            prefix: Optional prefix (e.g., "ZT", "ZH")
            length: Total SKU length (max 5 for system limit)

        Returns:
            Random SKU string
        """
        available_length = min(length, 5) - len(prefix)
        random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=available_length))
        return f"{prefix}{random_part}"[:5]

    @staticmethod
    def generate_barcode() -> str:
        """Generate random 13-digit barcode (EAN-13 format)."""
        return ''.join(random.choices(string.digits, k=13))

    @staticmethod
    def generate_product_name(base_name: str = "Test Product") -> Dict[str, str]:
        """
        Generate unique product names in UZ and RU.

        Args:
            base_name: Base product name

        Returns:
            Dict with uz_name and ru_name
        """
        timestamp = datetime.now().strftime("%H%M%S")
        random_suffix = ''.join(random.choices(string.digits, k=3))
        unique_id = f"{timestamp}{random_suffix}"

        return {
            "uz_name": f"{base_name} UZ {unique_id}",
            "ru_name": f"{base_name} RU {unique_id}",
            "uz_description": f"Test mahsulot tavsifi {unique_id}. Yuqori sifatli material ishlatilgan.",
            "ru_description": f"Описание тестового товара {unique_id}. Высокое качество материалов."
        }

    @staticmethod
    def generate_variant_data(
        price_range: tuple = (1, 100),
        discount_percent: int = 1
    ) -> Dict[str, str]:
        """
        Generate random variant/SKU data.

        Args:
            price_range: (min_price, max_price) tuple
            discount_percent: Discount percentage (default 10%)

        Returns:
            Dict with all variant fields
        """
        price = random.randint(price_range[0], price_range[1])
        discount_price = int(price * (1 - discount_percent / 100))

        return {
            "sku": ProductDataGenerator.generate_sku(),
            "quantity": str(random.randint(10, 500)),
            "barcode": ProductDataGenerator.generate_barcode(),
            "price": str(price),
            "discount_price": str(discount_price),
            "width": str(random.randint(100, 1000)),
            "length": str(random.randint(100, 1000)),
            "height": str(random.randint(50, 500)),
            "weight": str(round(random.uniform(0.1, 10.0), 1))
        }

    @classmethod
    def generate_full_product(
        cls,
        category_index: int = None,
        brand: str = None,
        country: str = None,
        base_name: str = "Auto Test Product",
        sku_prefix: str = "",
        price_range: tuple = (1000, 100000)
    ) -> Dict[str, Any]:
        """
        Generate complete product data with all required fields.

        Args:
            category_index: Index of category to use (random if None)
            brand: Brand name (random if None)
            country: Country name (random if None)
            base_name: Base product name
            sku_prefix: SKU prefix (e.g., "ZT")
            price_range: Price range tuple

        Returns:
            Complete product data dictionary
        """
        # Select or randomize values
        if category_index is None:
            category = random.choice(cls.CATEGORIES)
        else:
            category = cls.CATEGORIES[category_index % len(cls.CATEGORIES)]

        if brand is None:
            brand = random.choice(cls.BRANDS)

        if country is None:
            country = random.choice(cls.COUNTRIES)

        # Generate names
        names = cls.generate_product_name(base_name)

        # Generate variant data
        variant = cls.generate_variant_data(price_range)
        if sku_prefix:
            variant["sku"] = cls.generate_sku(prefix=sku_prefix)

        return {
            "category": category,
            "ikpu": random.choice(cls.IKPU_OPTIONS),
            "country": country,
            "brand": brand,
            "model": f"{brand} Model {random.choice(['A', 'B', 'C', 'X', 'Pro'])}",
            **names,
            "variant": variant
        }

    @classmethod
    def generate_staging_product(
        cls,
        product_type: str = "jacket",
        shop_name: str = "Zara"
    ) -> Dict[str, Any]:
        """
        Generate staging-specific product data.

        Args:
            product_type: "jacket" or "hoodie"
            shop_name: Shop name to use

        Returns:
            Staging product data
        """
        configs = {
            "jacket": {
                "category_path": ["Мужчинам", "Одежда", "Верхняя одежда"],
                "ikpu_search": "kurtkalar",
                "sku_prefix": "ZT",
                "base_name": "Zara Test Kurtka"
            },
            "hoodie": {
                "category_path": ["Мужчинам", "Одежда", "Свитшоты и худи"],
                "ikpu_search": "sviter",
                "sku_prefix": "ZH",
                "base_name": "Zara Test Hoodie"
            }
        }

        config = configs.get(product_type, configs["jacket"])
        names = cls.generate_product_name(config["base_name"])

        return {
            "shop_name": shop_name,
            "category_path": config["category_path"],
            "ikpu_search": config["ikpu_search"],
            "country": "Турция",
            "brand": "Zara",
            "sku": cls.generate_sku(prefix=config["sku_prefix"]),
            "barcode": cls.generate_barcode(),
            "price": "10",
            "discount_price": "1",
            "width": str(random.randint(400, 600)),
            "length": str(random.randint(600, 800)),
            "height": str(random.randint(40, 80)),
            "weight": str(round(random.uniform(0.5, 1.5), 1)),
            **names
        }

    @classmethod
    def generate_multi_product(
        cls,
        product_type: str = "smartfon",
        shop_name: str = "Zara"
    ) -> Dict[str, Any]:
        """
        Generate multi-product data with variants.

        Args:
            product_type: Product type ("smartfon")
            shop_name: Shop name

        Returns:
            Complete multi-product data dictionary
        """
        configs = {
            "smartfon": {
                "category_path": ["Мужчинам", "Одежда", "Футболки и поло"],
                "ikpu_search": "telefon",
                "country": "Китай",
                "brand": "Samsung",
                "model": "Samsung Model A",
                "base_name": "Test Smartfon Pro Max",
                "characteristics": {
                    "dropdowns": {
                        "Ekran turi": "AMOLED",
                        "Yangilanish chastotasi": "120 Hz",
                        "Ekran o'lchamlari": "Full HD+ (2400x1080)",
                        "Protsessor": "Qualcomm Snapdragon",
                        "Operativ xotira (RAM)": "8 GB",
                        "Tez quvvatlash": "67 Vt",
                        "SIM karta": "2 SIM (Dual SIM)",
                        "Bluetooth versiyasi": "Bluetooth 5.3",
                        "Optik zoom": "3x",
                        "Video yozish": "4K (2160p)"
                    },
                    "fields": {
                        "Ekran diagonali": "6.7",
                        "Asosiy kamera": "108",
                        "Frontal kamera": "32",
                        "Batareya sig'imi": "5000"
                    },
                    "checkboxes": ["Simsiz quvvatlash", "5G qo'llab-quvvatlash", "NFC"]
                },
                "variant_options": {
                    "Ichki xotira": ["128 GB", "256 GB"],
                    "Rang": ["Qora", "Oq"]
                }
            }
        }

        config = configs.get(product_type, configs["smartfon"])
        names = cls.generate_product_name(config["base_name"])
        sku = cls.generate_sku(prefix="TSM")

        return {
            "shop_name": shop_name,
            "category_path": config["category_path"],
            "ikpu_search": config["ikpu_search"],
            "country": config["country"],
            "brand": config["brand"],
            "model": config.get("model"),
            "characteristics": config["characteristics"],
            "variant_options": config["variant_options"],
            "bulk_fill": {
                "sku": sku,
                "barcode_prefix": cls.generate_barcode()[:6],
                "price": "100",
                "discount_price": "10"
            },
            **names
        }

    # ==================== BOUNDARY VALUE TEST DATA GENERATORS ====================

    @staticmethod
    def generate_boundary_sku(length: int) -> str:
        """
        Generate SKU with specific length for boundary testing.

        Args:
            length: Exact length of SKU to generate

        Returns:
            SKU string of specified length
        """
        if length <= 0:
            return ""
        chars = string.ascii_uppercase + string.digits
        return ''.join(random.choices(chars, k=length))

    @staticmethod
    def generate_boundary_name(length: int, lang: str = "uz") -> str:
        """
        Generate product name with specific length for boundary testing.

        Args:
            length: Exact length of name to generate
            lang: Language ("uz" or "ru")

        Returns:
            Name string of specified length
        """
        if length <= 0:
            return ""

        if lang == "ru":
            chars = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЭЮЯабвгдежзиклмнопрстуфхцчшщэюя "
        else:
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz "

        result = ''.join(random.choices(chars, k=length))
        return result.strip() or result[:length]

    @staticmethod
    def generate_boundary_price(value_type: str = "min") -> str:
        """
        Generate price for boundary testing.

        Args:
            value_type: "min", "max", "zero", "negative", "typical"

        Returns:
            Price string
        """
        prices = {
            "min": "1",
            "max": "9999999999",
            "zero": "0",
            "negative": "-1000",
            "typical": str(random.randint(100000, 5000000))
        }
        return prices.get(value_type, prices["typical"])

    @staticmethod
    def generate_boundary_barcode(length: int = 6) -> str:
        """
        Generate barcode prefix with specific length.

        Args:
            length: Length of barcode prefix

        Returns:
            Numeric barcode prefix
        """
        if length <= 0:
            return ""
        return ''.join(random.choices(string.digits, k=length))

    @classmethod
    def generate_invalid_multi_product(cls, invalid_type: str = "empty_name") -> Dict[str, Any]:
        """
        Generate multi-product data with specific invalid field for negative testing.

        Args:
            invalid_type: Type of invalid data to generate:
                - "empty_name": Empty UZ/RU names
                - "special_sku": Special characters in SKU
                - "xss_name": XSS attempt in name
                - "negative_price": Negative price
                - "discount_greater": Discount > price
                - "no_variants": No variant options selected

        Returns:
            Multi-product data with specified invalid field
        """
        # Start with valid base data
        base = cls.generate_multi_product()

        invalid_configs = {
            "empty_name": {
                "uz_name": "",
                "ru_name": ""
            },
            "empty_uz_name": {
                "uz_name": ""
            },
            "empty_ru_name": {
                "ru_name": ""
            },
            "special_sku": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "sku": "!@#$%"
                }
            },
            "sku_over_max": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "sku": "ABCDEF"  # 6 chars, max is 5
                }
            },
            "xss_name": {
                "uz_name": "<script>alert('xss')</script>",
                "ru_name": "<script>alert('xss')</script>"
            },
            "sql_injection": {
                "uz_name": "'; DROP TABLE products; --",
                "ru_name": "'; DROP TABLE products; --"
            },
            "negative_price": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "price": "-5000",
                    "discount_price": "-1000"
                }
            },
            "zero_price": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "price": "0",
                    "discount_price": "0"
                }
            },
            "discount_greater": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "price": "1000000",
                    "discount_price": "2000000"
                }
            },
            "no_variants": {
                "variant_options": {
                    "Ichki xotira": [],
                    "Rang": []
                }
            },
            "name_too_long": {
                "uz_name": "A" * 300,
                "ru_name": "Б" * 300
            },
            "alpha_barcode": {
                "bulk_fill": {
                    **base["bulk_fill"],
                    "barcode_prefix": "ABCDEF"
                }
            }
        }

        config = invalid_configs.get(invalid_type, {})
        base.update(config)
        return base

    @classmethod
    def generate_variant_combination(
        cls,
        memory_options: int = 2,
        color_options: int = 2
    ) -> Dict[str, Any]:
        """
        Generate multi-product with specific variant combination for pairwise testing.

        Args:
            memory_options: Number of memory options (1-3)
            color_options: Number of color options (1-3)

        Returns:
            Multi-product data with specified variant options
        """
        all_memory = ["128 GB", "256 GB", "512 GB"]
        all_colors = ["Qora", "Oq", "Ko'k"]

        base = cls.generate_multi_product()
        base["variant_options"] = {
            "Ichki xotira": all_memory[:memory_options],
            "Rang": all_colors[:color_options]
        }
        base["expected_variant_count"] = memory_options * color_options

        return base