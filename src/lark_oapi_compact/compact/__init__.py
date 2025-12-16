"""Compact compatibility layer for lark_oapi_compact."""

from .pydantic_compat import (
    IS_V2,
    PYDANTIC_VERSION,
    BaseModel,
    CompatBase,
    Field,
    FieldInfo,
    compat_from_dict,
    compat_from_json,
    compat_to_dict,
    compat_to_json,
    create_field,
    field_validator,
    get_model_config,
)

__all__ = [
    "BaseModel",
    "CompatBase",
    "Field",
    "FieldInfo",
    "compat_from_dict",
    "compat_from_json",
    "compat_to_dict",
    "compat_to_json",
    "create_field",
    "field_validator",
    "get_model_config",
    "IS_V2",
    "PYDANTIC_VERSION",
]

# Include validator for v1 compatibility
if not IS_V2:
    from .pydantic_compat import validator  # type: ignore

    __all__.append("validator")
