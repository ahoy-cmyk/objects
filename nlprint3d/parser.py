"""Simple parser for converting natural language to shape descriptors."""

import re
from dataclasses import dataclass
from typing import Optional, Dict, Any


@dataclass
class ShapeDescriptor:
    type: str
    params: Dict[str, Any]


_SHAPE_PATTERNS = [
    (r"cube(?: with)? side (?P<size>\d+(?:\.\d+)?)", "cube"),
    (r"sphere(?: with)? radius (?P<radius>\d+(?:\.\d+)?)", "sphere"),
    (r"cylinder(?: with)? radius (?P<radius>\d+(?:\.\d+)?) height (?P<height>\d+(?:\.\d+)?)", "cylinder"),
]


def parse_description(text: str) -> Optional[ShapeDescriptor]:
    """Parse a simple text description into a :class:`ShapeDescriptor`.

    Parameters
    ----------
    text:
        Natural language description of the object.

    Returns
    -------
    ShapeDescriptor or ``None`` if parsing failed.
    """
    text = text.lower().strip()
    for pattern, shape_type in _SHAPE_PATTERNS:
        m = re.search(pattern, text)
        if m:
            params = {k: float(v) for k, v in m.groupdict().items()}
            return ShapeDescriptor(type=shape_type, params=params)
    return None

