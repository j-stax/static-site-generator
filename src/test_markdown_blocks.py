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
