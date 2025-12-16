"""
Pydantic compatibility layer supporting both v1 and v2 with type safety.

This module provides a unified interface that works with both Pydantic v1 and v2,
allowing the SDK to be used alongside packages that require either version.
The compatibility is implemented through minimal abstractions to ensure
type checker compatibility.
"""

from __future__ import annotations

from typing import Any, Dict, TypeVar, cast

# Import pydantic and determine version
try:
    from pydantic import VERSION as PYDANTIC_VERSION

    IS_V2 = PYDANTIC_VERSION.startswith("2.")

    if IS_V2:
        from pydantic import BaseModel as BaseModelV2
        from pydantic import Field as FieldV2
        from pydantic.fields import FieldInfo as FieldInfoV2

        # Type aliases for Pydantic v2
        BaseModel = BaseModelV2
        FieldInfo = FieldInfoV2
        Field = FieldV2

        def get_model_config() -> dict[str, Any]:
            """Get model configuration for Pydantic v2."""
            return {"populate_by_name": True}

        # Try to import field_validator for v2
        try:
            from pydantic import field_validator as _field_validator_v2  # type: ignore
        except (ImportError, AttributeError):
            _field_validator_v2 = None

    else:
        from pydantic import (
            BaseModel as BaseModelV1,
        )
        from pydantic import (
            Field as FieldV1,
        )
        from pydantic import (
            validator as validatorV1,
        )

        # FieldInfo fallback for v1
        try:
            from pydantic.fields import ModelField as FieldInfoV1
        except (ImportError, AttributeError):
            FieldInfoV1 = type  # type: ignore

        # Type aliases for Pydantic v1
        BaseModel = BaseModelV1
        FieldInfo = cast(Any, FieldInfoV1)
        Field = FieldV1
        validator = validatorV1
        _field_validator_v2 = None

        def get_model_config() -> dict[str, Any]:
            """Get model configuration for Pydantic v1."""

            class Config:
                allow_population_by_field_name: bool = True

            return {"Config": Config}

except ImportError as e:
    raise ImportError("Pydantic is required. Please install either 'pydantic>=1.10.14' or 'pydantic>=2.0'") from e

# Type variables
T = TypeVar("T", bound="CompatBase")


# Standalone compatibility functions instead of mixin class


def compat_to_dict(model, **kwargs):
    """
    Convert model to dictionary using version-appropriate method.

    This function provides a unified interface that works with both Pydantic v1 and v2.
    Use this function to avoid version-specific method names when migrating between versions.
    """
    if IS_V2 and hasattr(model, "model_dump"):
        # Pydantic v2
        return model.model_dump(**kwargs)  # type: ignore
    else:
        # Pydantic v1
        return model.dict(**kwargs)  # type: ignore


def compat_to_json(model, **kwargs):
    """
    Convert model to JSON string using version-appropriate method.

    This function provides a unified interface that works with both Pydantic v1 and v2.
    Use this function to avoid version-specific method names when migrating between versions.
    """
    if IS_V2 and hasattr(model, "model_dump_json"):
        # Pydantic v2
        return model.model_dump_json(**kwargs)  # type: ignore
    else:
        # Pydantic v1
        return model.json(**kwargs)  # type: ignore


def compat_from_dict(model_class, obj, **kwargs):
    """
    Parse dictionary into model instance using version-appropriate method.

    This function provides a unified interface that works with both Pydantic v1 and v2.
    Use this function to avoid version-specific method names when migrating between versions.
    """
    if IS_V2 and hasattr(model_class, "model_validate"):
        # Pydantic v2
        return model_class.model_validate(obj, **kwargs)  # type: ignore
    else:
        # Pydantic v1
        return model_class.parse_obj(obj, **kwargs)  # type: ignore


def compat_from_json(model_class: type[T], data: str, **kwargs: Any) -> T:
    """
    Parse JSON string into model instance using version-appropriate method.

    This function provides a unified interface that works with both Pydantic v1 and v2.
    Use this function to avoid version-specific method names when migrating between versions.
    """
    if IS_V2 and hasattr(model_class, "model_validate_json"):
        # Pydantic v2
        return model_class.model_validate_json(data, **kwargs)  # type: ignore
    else:
        # Pydantic v1
        return model_class.parse_raw(data, **kwargs)  # type: ignore


# Optional mixin class for those who prefer instance methods
class CompatBase:
    """
    Optional mixin class providing compatibility methods as instance methods.

    Note: This mixin is safe for multiple inheritance because it only adds
    new methods and doesn't override __init__ or __new__.

    For type safety and to avoid inheritance issues, consider using the
    standalone functions instead: compat_to_dict(), compat_to_json(), etc.
    """

    def compat_to_dict(self, **kwargs: Any) -> Dict[str, Any]:
        """
        Convert model to dictionary.

        This method provides a unified interface that works with both Pydantic v1 and v2.
        Use this method to avoid version-specific method names when migrating between versions.
        """
        if IS_V2 and hasattr(self, "model_dump"):
            # Pydantic v2
            return self.model_dump(**kwargs)  # type: ignore
        else:
            # Pydantic v1
            return self.dict(**kwargs)  # type: ignore

    def compat_to_json(self, **kwargs: Any) -> str:
        """
        Convert model to JSON string.

        This method provides a unified interface that works with both Pydantic v1 and v2.
        Use this method to avoid version-specific method names when migrating between versions.
        """
        if IS_V2 and hasattr(self, "model_dump_json"):
            # Pydantic v2
            return self.model_dump_json(**kwargs)  # type: ignore
        else:
            # Pydantic v1
            return self.json(**kwargs)  # type: ignore

    @classmethod
    def compat_from_dict(cls: type[T], obj: Dict[str, Any], **kwargs: Any) -> T:
        """
        Parse dictionary into model instance.

        This method provides a unified interface that works with both Pydantic v1 and v2.
        Use this method to avoid version-specific method names when migrating between versions.
        """
        if IS_V2 and hasattr(cls, "model_validate"):
            # Pydantic v2
            return cls.model_validate(obj, **kwargs)  # type: ignore
        else:
            # Pydantic v1
            return cls.parse_obj(obj, **kwargs)  # type: ignore

    @classmethod
    def compat_from_json(cls: type[T], data: str, **kwargs: Any) -> T:
        """
        Parse JSON string into model instance.

        This method provides a unified interface that works with both Pydantic v1 and v2.
        Use this method to avoid version-specific method names when migrating between versions.
        """
        if IS_V2 and hasattr(cls, "model_validate_json"):
            # Pydantic v2
            return cls.model_validate_json(data, **kwargs)  # type: ignore
        else:
            # Pydantic v1
            return cls.parse_raw(data, **kwargs)  # type: ignore


def create_field(
    default: Any = ...,
    alias: str | None = None,
    title: str | None = None,
    description: str | None = None,
    **kwargs: Any,
) -> Any:
    """
    Create a field that works with both Pydantic v1 and v2.

    This function provides a unified interface for creating fields with optional
    aliasing and other field configurations.
    """
    return Field(default, alias=alias, title=title, description=description, **kwargs)


def field_validator(*fields: str, **kwargs: Any) -> Any:
    """
    Create a field validator that works with both Pydantic v1 and v2.

    This function provides a unified interface for creating field validators.
    """
    if IS_V2 and _field_validator_v2 is not None:
        # Pydantic v2
        return _field_validator_v2(*fields, **kwargs)
    else:
        # For v1, use the validator decorator
        mode = kwargs.get("mode", "before")
        return validator(*fields, pre=(mode == "before"))


def get_version_info() -> dict[str, Any]:
    """Get information about the Pydantic version being used."""
    return {
        "version": PYDANTIC_VERSION,
        "is_v2": IS_V2,
        "major": 2 if IS_V2 else 1,
    }


# Export public API
__all__ = [
    # Core types
    "BaseModel",
    "Field",
    "FieldInfo",
    "CompatBase",
    # Configuration
    "get_model_config",
    # Field creation
    "create_field",
    # Validation
    "field_validator",
    # Version info
    "get_version_info",
    "IS_V2",
    "PYDANTIC_VERSION",
]

# Add validator only for v1
if not IS_V2:
    __all__.append("validator")
