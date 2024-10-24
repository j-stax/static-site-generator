from markdown_to_blocks import *
from htmlnode import *
from block_to_block_type import *
from textnode import text_node_to_html_node
from text_to_children import *

def markdown_to_html_node(markdown):
    parent_node = HTMLNode("div", value=None, children=[])

    md_blocks = markdown_to_blocks(markdown)

    for block in md_blocks:
        block_type = block_to_block_type(block)
        text = ""

        # Extract text-only from Markdown
        if block_type[0] == "h":
            heading_num = int(block_type[1])
            text = block[heading_num:].strip()
        elif block_type == "blockquote":
            text = block[1:]
        elif block_type == "code":
            text = block[3:-3]
        elif block_type == "p":
            text = block
        else:
            # Handle ul and ol Markdown
            sections = block.split("\n")
            for i in range(len(sections)):
                list_item = sections[i]
                if i != len(sections)-1:
                    text += f'{list_item[2:]}\n'
                else:
                    text += f'{list_item[2:]}'

        children = text_to_children(text)
        new_htmlnode = HTMLNode(block_type, text, children)
        parent_node.children.append(new_htmlnode)
    
    return parent_node




if __name__ == '__main__':
    md = "This is a p block text and a ![rick roll](https://i.imgur.com/aKaOqIh.gif) image.\n\n" \
            "1. This is a ol markdown.\n2. Another ol markdown."
    md2 = "## This is an h2 heading.\n\n" \
            ">This is a quote block with a [link to boot.dev](https://www.boot.dev) link.\n\n" \
            "* One unordered list item.\n* And another unordered list item."
    htmlnodes = markdown_to_html_node(md2)
    print(htmlnodes)

