import unittest

from markdown_blocks import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_olist,
    block_type_ulist,
    block_type_quote
)

class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is a **bolded** paragraph

This is another paragraph with *italic* and `code` here.
This is another paragraph on a new line

* This is a list
* with items
"""        
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with *italic* and `code` here.\nThis is another paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )


    def test_markdown_to_blocks_newlines(self):
        md = """
This is a **bolded** paragraph





This is another paragraph with *italic* and `code` here.
This is another paragraph on a new line


* This is a list
* with items
"""   
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is another paragraph with *italic* and `code` here.\nThis is another paragraph on a new line",
                "* This is a list\n* with items"
            ]
        )


    def test_block_to_block_type(self):
        block = "## heading"
        self.assertEqual(block_to_block_type(block), block_type_heading)
        block = "```\nsome code\n```"
        self.assertEqual(block_to_block_type(block), block_type_code)
        block = "> quote\n> another quote"
        self.assertEqual(block_to_block_type(block), block_type_quote)
        block = "* ulist item 1\n* ulist item 2"
        self.assertEqual(block_to_block_type(block), block_type_ulist)
        block = "1. olist 1\n2. olist 2\n3. olist 3"
        self.assertEqual(block_to_block_type(block), block_type_olist)
        block = "This is just a paragraph"
        self.assertEqual(block_to_block_type(block), block_type_paragraph)
    

    def test_paragraph(self):
        md = """
This is a **bolded** paragraph text in a p tag.
""" 
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a <b>bolded</b> paragraph text in a p tag.</p></div>"
        )

    
    def test_paragraphs(self):
        md = """
There is a **bolded** word in this
paragraph with a
p tag.


Here is a second paragraph with *italic*
text and `code`

"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>There is a <b>bolded</b> word in this paragraph with a p tag.</p>" \
            "<p>Here is a second paragraph with <i>italic</i> text and <code>code</code></p></div>"
        )

    
    def test_lists(self):
        md = """
- This is a list
- with an *italic* item
- and a **bold** item

1. This is an `ordered` list
2. with some items
3. and some more items
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with an <i>italic</i> item</li><li>and a <b>bold</b> item</li></ul>" \
            "<ol><li>This is an <code>ordered</code> list</li><li>with some items</li><li>and some more items</li></ol></div>"
        )


    def test_headings(self):
        md = """
# This is an h1 heading

This is a paragraph text with a **bold** word.

###### This is an h6 heading
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is an h1 heading</h1><p>This is a paragraph text with a <b>bold</b> word.</p>" \
            "<h6>This is an h6 heading</h6></div>"
        )

    
    def test_blockquote(self):
        md = """
> This is a
> blockquote block
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote></div>"
        )
