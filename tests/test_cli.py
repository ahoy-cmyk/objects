import unittest
from unittest import mock

import nlprint3d.cli as cli


class CLITests(unittest.TestCase):
    def test_fallback_to_generative(self):
        mesh = mock.Mock()
        with mock.patch.object(cli, "parse_description", return_value=None), \
             mock.patch.object(cli, "generate_from_text", return_value=mesh), \
             mock.patch.object(mesh, "export") as export:
            cli.main(["something", "out.stl"])
            export.assert_called_once_with("out.stl")


if __name__ == "__main__":
    unittest.main()
