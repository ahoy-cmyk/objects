"""Command-line interface for nlprint3d."""

import argparse

from . import parse_description, generate_mesh


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate 3D object from text")
    parser.add_argument("description", help="Text description of the object")
    parser.add_argument("output", help="Output 3MF file (must end with .3mf)")
    args = parser.parse_args(argv)

    if not args.output.lower().endswith(".3mf"):
        parser.error("Output file must end with .3mf")

    descs = parse_description(args.description)
    if descs is None:
        parser.error("Could not parse description")

    mesh = generate_mesh(descs)
    if mesh is None:
        parser.error("Mesh generation failed (is trimesh installed?)")
    mesh.export(args.output)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

