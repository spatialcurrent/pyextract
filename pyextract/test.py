# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 Spatial Current, Inc.
#
#########################################################################

import unittest


class TextExtract(unittest.TestCase):
    """
    TextExtract is used for testing extract
    """

    def test_simple(self):
        from pyextract.extract import extract
        y = extract(["a"], {"a": "b"}, None)
        self.assertEqual(y, "b")

    def test_depth_2(self):
        from pyextract.extract import extract
        y = extract(["a", "b"], {"a": {"b": "c"}}, None)
        self.assertEqual(y, "c")

    def test_fallback(self):
        from pyextract.extract import extract
        y = extract(["a", "d"], {"a": {"b": "c"}}, "i")
        self.assertEqual(y, "i")

    def test_fallback_with_blank(self):
        from pyextract.extract import extract
        y = extract(["a", "b"], {"a": {"b": ""}}, "i")
        self.assertIsInstance(y, basestring) and len(y) == 0

    def test_fallback_with_blank_2(self):
        from pyextract.extract import extract
        y = extract(["a", "b"], {"a": {"b": ""}}, "") or "i"
        self.assertEqual(y, "i")


if __name__ == '__main__':
    unittest.main()
