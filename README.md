# NLPrint3D

NLPrint3D is a minimal proof-of-concept that converts very simple natural
language descriptions into 3D objects ready for printing. The project parses
text descriptions and generates basic shapes using `trimesh`.

The CLI checks that required dependencies are installed. If `trimesh` is
missing you will be prompted to install everything listed in
`requirements.txt`.

## Usage

```bash
# Create a cube with side length 2 and save as cube.stl
python -m nlprint3d.cli "cube with side 2" cube.stl
```

Only a few shapes are supported in this MVP: cubes, spheres and cylinders.

The code is pure Python and runs on Linux, Windows and macOS. It has been
tested on an Apple Silicon Mac with an M4 processor.

## Development

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
python -m unittest discover -v tests
```
