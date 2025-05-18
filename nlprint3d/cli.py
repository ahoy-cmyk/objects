"""Command-line interface for nlprint3d."""

import argparse

from . import parse_description, generate_mesh, generate_from_text


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Generate 3D object from text")
    parser.add_argument("description", help="Text description of the object")
    parser.add_argument("output", help="Output STL file")
    args = parser.parse_args(argv)

    desc = parse_description(args.description)
    if desc is not None:
        mesh = generate_mesh(desc)
    else:
        mesh = generate_from_text(args.description)

    if mesh is None:
        parser.error(
            "Mesh generation failed (unsupported description or missing dependencies)"
        )
    mesh.export(args.output)
    print(f"Wrote {args.output}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())

