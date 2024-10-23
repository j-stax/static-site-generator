from split_image_and_link_nodes import *
from split_nodes_delimiter import *

def text_to_textnode(text):
    original_text = TextNode(text, TextType.TEXT)
    new_textnode_list = split_nodes_delimiter([original_text], "**", TextType.BOLD)
    new_textnode_list = split_nodes_delimiter(new_textnode_list, "*", TextType.ITALIC)
    new_textnode_list = split_nodes_delimiter(new_textnode_list, "`", TextType.CODE)
    new_textnode_list = split_nodes_images(new_textnode_list)
    new_textnode_list = split_nodes_links(new_textnode_list)
    return new_textnode_list



if __name__ == '__main__':
    text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    text_to_textnode(text)
    


