"""Generate 3D meshes from shape descriptors."""

from typing import Optional, List

try:
    import trimesh
except ImportError:  # pragma: no cover - trimesh is optional for tests
    trimesh = None

from .parser import ShapeDescriptor


def _generate_single_mesh(desc: ShapeDescriptor) -> Optional["trimesh.Trimesh"]:
    """Create a mesh from a single :class:`ShapeDescriptor`.

    Parameters
    ----------
    desc:
        Shape descriptor describing the object.

    Returns
    -------
    trimesh.Trimesh or ``None`` if trimesh is not available or the type is
    unsupported.
    """

    if trimesh is None:
        return None

    if desc.type == "cube":
        size = desc.params.get("size", 1)
        return trimesh.creation.box((size, size, size))
    if desc.type == "sphere":
        radius = desc.params.get("radius", 1)
        return trimesh.creation.icosphere(radius=radius)
    if desc.type == "cylinder":
        radius = desc.params.get("radius", 1)
        height = desc.params.get("height", 1)
        return trimesh.creation.cylinder(radius=radius, height=height)
    return None


def generate_mesh(descs: List[ShapeDescriptor]) -> Optional["trimesh.Trimesh"]:
    """Create a mesh from a list of :class:`ShapeDescriptor` objects.

    Parameters
    ----------
    descs:
        List of shape descriptors describing the objects.

    Returns
    -------
    trimesh.Trimesh or ``None`` if trimesh is not available or no meshes
    could be created.
    """
    if trimesh is None:
        return None

    meshes = []
    for d in descs:
        m = _generate_single_mesh(d)
        if m is not None:
            m.apply_translation(d.position)
            meshes.append(m)

    if not meshes:
        return None
    return trimesh.util.concatenate(meshes)

