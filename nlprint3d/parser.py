"""Simple parser for converting natural language to shape descriptors."""

import re
from dataclasses import dataclass
from typing import Optional, Dict, Any, List, Tuple


@dataclass
class ShapeDescriptor:
    type: str
    params: Dict[str, Any]
    position: Tuple[float, float, float] = (0.0, 0.0, 0.0)


_SHAPE_PATTERNS = [
    (r"cube(?: with)? side (?P<size>\d+(?:\.\d+)?)", "cube"),
    (r"sphere(?: with)? radius (?P<radius>\d+(?:\.\d+)?)", "sphere"),
    (r"cylinder(?: with)? radius (?P<radius>\d+(?:\.\d+)?) height (?P<height>\d+(?:\.\d+)?)", "cylinder"),
]


def parse_description(text: str) -> Optional[List[ShapeDescriptor]]:
    """Parse a simple text description into shape descriptors.

    Parameters
    ----------
    text:
        Natural language description of the object.

    Returns
    -------
    list of :class:`ShapeDescriptor` or ``None`` if parsing failed.
    """
    text = text.lower().strip()

    stacked = re.search(
        r"(?P<count>\d+) cubes stacked(?: on (?:top of )?each other)?(?: with side (?P<size>\d+(?:\.\d+)?))?",
        text,
    )
    if stacked:
        count = int(stacked.group("count"))
        size = float(stacked.group("size")) if stacked.group("size") else 1.0
        return [
            ShapeDescriptor(
                type="cube",
                params={"size": size},
                position=(0.0, 0.0, i * size),
            )
            for i in range(count)
        ]

    for pattern, shape_type in _SHAPE_PATTERNS:
        m = re.search(pattern, text)
        if m:
            params = {k: float(v) for k, v in m.groupdict().items()}
            return [ShapeDescriptor(type=shape_type, params=params)]
    return None

