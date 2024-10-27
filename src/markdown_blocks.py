import re

from htmlnode import ParentNode
from inline_markdown import text_to_textnode
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    sectional_blocks = []
    for section in sections:
        if len(section) == 0:
            continue
        sectional_blocks.append(section.strip())
    return sectional_blocks


def block_to_block_type(block):
    heading_matches = re.findall(r"^(?!#{7,})#{1,6} ", block)
    quote_matches = re.findall(r"^>(?!>)", block)
    ul_matches = re.findall(r"^[-*] .*(\n[-*] .*)*$", block)

    lines = block.split("\n")

    if len(heading_matches) > 0: 
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if len(quote_matches) > 0:
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if len(ul_matches) > 0:
        for line in lines:
            ul_line_matches = re.findall(r"^[-*] .*", line)
            if ul_line_matches == 0:
                return block_type_paragraph
        return block_type_ulist
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return block_type_paragraph
            i += 1
        return block_type_olist
    return block_type_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)

    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    return ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnode(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    h_level = block.count("#")
    if h_level + 1 >= len(block):
        raise ValueError(f'Invalid heading level: {h_level}')
    text = block[h_level+1:]
    children = text_to_children(text)
    return ParentNode(f'h{h_level}', children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)


if __name__ == '__main__':
    text = "### This is an h3 block."
    text2 = "1. ordered list block.\n2. ordered list block.\n3. ordered list block."
    print(block_to_block_type(text))
    print(block_to_block_type(text2))