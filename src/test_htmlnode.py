import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

    # Leaf nodes:
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
    
    # Parent nodes
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>"
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaisesRegex(ValueError, "Parent node without children."):
            parent_node.to_html()

    def test_to_html_with_no_children(self):
        parent_node = ParentNode(None, None)
        with self.assertRaisesRegex(ValueError, "Parent node has no tag property."):
            parent_node.to_html()

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()