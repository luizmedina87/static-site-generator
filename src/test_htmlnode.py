import unittest

from htmlnode import HTMLNode


class testHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("<p>", "This is a paragraph")
        node2 = HTMLNode("<p>", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = HTMLNode("<p>", "This is a paragraph")
        node2 = HTMLNode("<a>", "This is an anchor")
        self.assertNotEqual(node, node2)
        
    def test_repr(self):
        node = HTMLNode("<p>", "This is a paragraph")
        self.assertEqual("HTMLNode(<p>, This is a paragraph, None, None)", repr(node))
