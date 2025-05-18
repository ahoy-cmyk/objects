import importlib
import sys
from pathlib import Path
import unittest
from unittest import mock

from nlprint3d.cli import ensure_dependencies


class CLIDependencyTests(unittest.TestCase):
    def test_ensure_dependencies_missing_user_declines(self):
        with mock.patch.dict(sys.modules, {'trimesh': None}):
            with mock.patch('builtins.input', return_value='n'):
                self.assertFalse(ensure_dependencies())

    def test_ensure_dependencies_missing_user_accepts(self):
        with mock.patch.dict(sys.modules, {'trimesh': None}):
            with mock.patch('builtins.input', return_value='y'):
                with mock.patch('subprocess.check_call') as cc:
                    cc.return_value = 0
                    self.assertTrue(ensure_dependencies())
                    cc.assert_called()


