import unittest

from block_to_block_type import *

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_true(self):
        block = "### This is an h3 heading."
        result = block_to_block_type(block)
        self.assertEqual(result, "h3")

    def test_heading_false(self):
        block = "####### This text has seven hashtags."
        result = block_to_block_type(block)
        self.assertNotEqual(result, "h7")
    
    def test_code_block_true(self):
        block = "```This is a code block.```"
        result = block_to_block_type(block)
        self.assertEqual(result, "code")

    def test_code_block_false(self):
        block = "```This is an INVALID code block.``"
        result = block_to_block_type(block)
        self.assertNotEqual(result, "code")

    def test_quote_block_true(self):
        block = ">This is a quote block."
        result = block_to_block_type(block)
        self.assertEqual(result, "blockquote")

    def test_quote_block_false(self):
        block = ">>This should not be a quote block."
        result = block_to_block_type(block)
        self.assertNotEqual(result, "blockquote")

    def test_unordered_list_block_true(self):
        block = "* This is a unordered list block.\n- This is an ul block.\n* This is an ul block."
        result = block_to_block_type(block)
        self.assertEqual(result, "ul")

    def test_ul_block_false(self):
        block = "- This is not a ul block.\n-This is an ul block.\n- This is an ul block."
        result = block_to_block_type(block)
        self.assertNotEqual(result, "ul")

    def test_ordered_list_block_true(self):
        block = "1. ordered list block.\n2. ordered list block.\n3. ordered list block."
        result = block_to_block_type(block)
        self.assertEqual(result, "ol")

    def test_ol_block_false(self):
        block = "0.... This is not an ordered list block.\n1. Already invalid ol block."
        result = block_to_block_type(block)
        self.assertNotEqual(result, "ol")

    def test_paragraph_block_true(self):
        block = "This >is ```an 1. old-fashioned paragraph ##block."
        result = block_to_block_type(block)
        self.assertEqual(result, "p")

    def test_p_block_false(self):
        block = ">This is not a p block"
        result = block_to_block_type(block)
        self.assertNotEqual(result, "p")
