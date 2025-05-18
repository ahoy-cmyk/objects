import unittest

from nlprint3d.parser import parse_description, ShapeDescriptor


class ParserTests(unittest.TestCase):
    def test_parse_cube(self):
        desc = parse_description("cube with side 2")
        self.assertEqual(desc, ShapeDescriptor(type="cube", params={"size": 2.0}))

    def test_parse_sphere(self):
        desc = parse_description("sphere radius 4")
        self.assertEqual(desc, ShapeDescriptor(type="sphere", params={"radius": 4.0}))


if __name__ == "__main__":
    unittest.main()
