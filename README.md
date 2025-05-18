# NLPrint3D

NLPrint3D is a minimal proof-of-concept that converts natural language
descriptions into 3D objects ready for printing.  Simple shape descriptions
are parsed directly, while arbitrary objects are passed through an optional
generative model (Shap-E) if available.  The resulting mesh can be exported as
an STL file for printing.

## Usage

```bash
# Create a cube with side length 2 and save as cube.stl
python -m nlprint3d.cli "cube with side 2" cube.stl
```

Only a few shapes are recognised by the built-in parser: cubes, spheres and
cylinders.  Other requests fall back to the generative pipeline which requires
the `shap_e` and `torch` packages.

## Development

Install dependencies and run the tests:

```bash
pip install -r requirements.txt
python -m unittest discover -v tests
```
