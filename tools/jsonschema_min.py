"""Dependency-free validator for the JSON Schema subset this repo uses.

Not a general JSON Schema engine. It supports exactly the keywords the
human-mind and human-atlas schemas rely on (draft 2020-12 subset):

    type, const, enum, required, additionalProperties (false only),
    properties, items, minimum, maximum, minLength, uniqueItems.

That is enough to validate every schema in ``schemas/`` without pulling a
third-party library into an offline environment. If a schema starts using a
keyword not listed here, add it here rather than reaching for a dependency.
"""

from __future__ import annotations

from typing import Any


_JSON_TYPES = {
    "object": dict,
    "array": list,
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "null": type(None),
}


def _type_ok(value: Any, expected: str) -> bool:
    # booleans are a subtype of int in Python; keep number/integer honest.
    if expected in ("number", "integer") and isinstance(value, bool):
        return False
    py = _JSON_TYPES.get(expected)
    return py is not None and isinstance(value, py)


def validate(instance: Any, schema: dict, path: str = "$") -> list[str]:
    """Return a list of human-readable errors. Empty list means valid."""
    errors: list[str] = []

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: {instance!r} not in enum {schema['enum']}")

    expected_type = schema.get("type")
    if expected_type and not _type_ok(instance, expected_type):
        errors.append(f"{path}: expected type {expected_type}, got {type(instance).__name__}")
        return errors  # further checks assume the type held

    if expected_type == "object" and isinstance(instance, dict):
        props = schema.get("properties", {})
        for req in schema.get("required", []):
            if req not in instance:
                errors.append(f"{path}: missing required property '{req}'")
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in props:
                    errors.append(f"{path}: additional property '{key}' not allowed")
        for key, subschema in props.items():
            if key in instance:
                errors.extend(validate(instance[key], subschema, f"{path}.{key}"))

    if expected_type == "array" and isinstance(instance, list):
        if schema.get("uniqueItems") and len(instance) != len({repr(x) for x in instance}):
            errors.append(f"{path}: array items must be unique")
        item_schema = schema.get("items")
        if item_schema:
            for i, item in enumerate(instance):
                errors.extend(validate(item, item_schema, f"{path}[{i}]"))

    if expected_type == "string" and isinstance(instance, str):
        min_len = schema.get("minLength")
        if min_len is not None and len(instance) < min_len:
            errors.append(f"{path}: string shorter than minLength {min_len}")

    if expected_type in ("number", "integer") and isinstance(instance, (int, float)):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} > maximum {schema['maximum']}")

    return errors
