import importlib
import unittest
from unittest import mock

from nlprint3d.parser import ShapeDescriptor
from nlprint3d import generator


class GeneratorTests(unittest.TestCase):
    def test_generate_mesh_without_trimesh(self):
        with mock.patch.object(generator, "trimesh", None):
            desc = [ShapeDescriptor(type="cube", params={"size": 1})]
            self.assertIsNone(generator.generate_mesh(desc))


if __name__ == "__main__":
    unittest.main()
