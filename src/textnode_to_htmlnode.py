from leafnode import LeafNode
from textnode import *

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT.value:
            return LeafNode(tag=None, value=text_node.text)
        case TextType.BOLD.value:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC.value:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE.value:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK.value:
            return LeafNode(tag="a", value=text_node.text, props={ "href": text_node.url })
        case TextType.IMAGE.value:
            return LeafNode(tag="img", value="", props={ "src": text_node.url, "alt": text_node.text })
        
        case _:
            raise Exception("Invalid TextNode.")