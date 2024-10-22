from htmlnode import *
from leafnode import *

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("ParentNode tag is required.")
        elif not self.children:
            raise ValueError("ParentNode children are required.")
        else:
            html = f'<{self.tag}>'
            for child in self.children:
                html += f'{child.to_html()}'
            return f'{html}</{self.tag}>'
        


if __name__ == '__main__':       
    bold_node = LeafNode(tag="b", value="Bold text")
    textnode1 = LeafNode(tag=None, value="Normal text1")
    anchor_node = LeafNode(tag="a", value="Anchor text", props={ "href": "https://www.boot.dev"})
    italic_node = LeafNode(tag="i", value="Italic text")
    textnode2 = LeafNode(tag=None, value="Normal text2")
    parentnode_p1 = ParentNode(tag="p", children=[bold_node, textnode1, anchor_node])
    parentnode_p2 = ParentNode(tag="p", children=[italic_node, textnode2])
    parentnode_div = ParentNode(tag="div", children=[parentnode_p1, parentnode_p2])
    print(parentnode_div.to_html())


            
