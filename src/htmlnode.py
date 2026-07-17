from __future__ import annotations


class HTMLNode:
    def __init__(
        self, 
        tag: str | None = None, 
        value: str | None = None, 
        children: list[HTMLNode] | None = None, 
        props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError
    
    def props_to_html(self) -> str:
        formatted_string = ""
        if self.props:
            for key, value in self.props.items():
                formatted_string += f''' {key}="{value}"'''
        return formatted_string
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, 
        tag: str | None, 
        value: str, 
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return self.value
        if self.tag == "img":
            return f"<{self.tag}{self.props_to_html()}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(
        self, 
        tag: str,  
        children: list[HTMLNode], 
        props: dict[str, str] | None = None
    ):
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if not self.tag:
            raise ValueError("Parent node has no tag property.")
        if not self.children:
            raise ValueError("Parent node without children.")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"