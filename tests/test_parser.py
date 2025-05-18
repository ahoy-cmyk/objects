import unittest

from nlprint3d.parser import parse_description, ShapeDescriptor


class ParserTests(unittest.TestCase):
    def test_parse_cube(self):
        desc = parse_description("cube with side 2")
        self.assertEqual(desc, [ShapeDescriptor(type="cube", params={"size": 2.0})])

    def test_parse_sphere(self):
        desc = parse_description("sphere radius 4")
        self.assertEqual(desc, [ShapeDescriptor(type="sphere", params={"radius": 4.0})])

    def test_parse_stacked_cubes(self):
        desc = parse_description("I want 3 cubes stacked on each other")
        expected = [
            ShapeDescriptor(type="cube", params={"size": 1.0}, position=(0.0, 0.0, 0.0)),
            ShapeDescriptor(type="cube", params={"size": 1.0}, position=(0.0, 0.0, 1.0)),
            ShapeDescriptor(type="cube", params={"size": 1.0}, position=(0.0, 0.0, 2.0)),
        ]
        self.assertEqual(desc, expected)


if __name__ == "__main__":
    unittest.main()
