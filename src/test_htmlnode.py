import unittest

from htmlnode import HTMLNode, LeafNode


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

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_eq_leaf(self):
        node = LeafNode("p", "this is a paragraph")
        node2 = LeafNode("p", "this is a paragraph")
        self.assertEqual(node, node2)

    def test_not_eq_leaf(self):
        node = LeafNode("p", "this is a paragraph")
        node2 = LeafNode("p", "this is a different paragraph")
        self.assertNotEqual(node, node2)

    def test_leaf_repr(self):
        node = LeafNode("a", "this is an anchor", {"href": "www.whatever.com"})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(a, this is an anchor, {'href': 'www.whatever.com'})"
        )

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
        

if __name__ == "__main__":
    unittest.main()