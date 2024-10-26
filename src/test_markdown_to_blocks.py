import unittest

from markdown_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_input(self):
        md = "# This is a heading\n\n" \
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" \
            "* This is the first list item in a list block\n" \
            "* This is a list item\n" \
            "* This is another list item"
        result = markdown_to_blocks(md)
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected_result)

    def test_extra_whitespace(self):
        md = "     # This is a heading\n\n\n" \
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n\n\n       " \
            "                 * This is the first list item in a list block\n" \
            "* This is a list item\n" \
            "* This is another list item             "
        result = markdown_to_blocks(md)
        expected_result = [
            "# This is a heading", 
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
        self.assertEqual(result, expected_result)