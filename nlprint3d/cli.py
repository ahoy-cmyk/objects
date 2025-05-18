"""Command-line interface for nlprint3d."""

import argparse
import importlib
import subprocess
import sys
from pathlib import Path

from . import parse_description, generate_mesh


def ensure_dependencies() -> bool:
    """Check that required dependencies are installed.

    If ``trimesh`` is missing, prompt the user to install packages from
    ``requirements.txt``.

    Returns
    -------
    bool
        ``True`` if dependencies are satisfied or were installed successfully.
    """

    try:
        importlib.import_module("trimesh")
        return True
    except ImportError:
        print("The 'trimesh' package is required to generate meshes.")
        ans = input("Install missing dependencies now? [y/N] ")
        if ans.lower().startswith("y"):
            req = Path(__file__).resolve().parent.parent / "requirements.txt"
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req)])
                return True
            except Exception:
                print("Automatic installation failed. Please run 'pip install -r requirements.txt'.")
        return False


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate 3D object from text")
    parser.add_argument("description", help="Text description of the object")
    parser.add_argument("output", help="Output STL file")
    args = parser.parse_args(argv)

    if not ensure_dependencies():
        parser.error("Required dependencies are missing")

    desc = parse_description(args.description)
    if desc is None:
        parser.error("Could not parse description")

    mesh = generate_mesh(desc)
    if mesh is None:
        parser.error("Mesh generation failed (is trimesh installed?)")
    mesh.export(args.output)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

