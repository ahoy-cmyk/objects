# NLPrint3D

NLPrint3D is a minimal proof-of-concept that converts very simple natural
language descriptions into 3D objects ready for printing. The project parses
text descriptions and generates basic shapes using `trimesh`.

The CLI outputs `.3mf` files which can be loaded in slicers like OrcaSlicer or
Bambu Studio.

## Usage

```bash
# Create a cube with side length 2 and save as cube.3mf
python -m nlprint3d.cli "cube with side 2" cube.3mf

# Create three cubes stacked on top of each other and export to cubes.3mf
python -m nlprint3d.cli "I want 3 cubes stacked on each other" cubes.3mf
```

Only a few shapes are supported in this MVP: cubes, spheres and cylinders.

## Development

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
python -m unittest discover -v tests
```
