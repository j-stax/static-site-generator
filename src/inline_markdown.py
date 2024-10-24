import re

from textnode import TextNode, TextType


def text_to_textnode(text):
    original_text = TextNode(text, TextType.TEXT)
    new_textnode_list = split_nodes_delimiter([original_text], "**", TextType.BOLD)
    new_textnode_list = split_nodes_delimiter(new_textnode_list, "*", TextType.ITALIC)
    new_textnode_list = split_nodes_delimiter(new_textnode_list, "`", TextType.CODE)
    new_textnode_list = split_nodes_images(new_textnode_list)
    new_textnode_list = split_nodes_links(new_textnode_list)
    return new_textnode_list


"""
The function takes a list of "old nodes", a delimiter, and 
a text type. It returns a new list of nodes, 
where any "text" type nodes in the input list are 
(potentially) split into multiple nodes based on 
the syntax.
"""
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue

        sections = old_node.text.split(delimiter)

        # Even number of sections represents invalid Markdown syntax
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        
        # Textnode not containing the delimiter is added to list with no changes
        if len(sections) == 1:
            new_nodes.append(old_node)
            continue
              
        tmp_list = []
        for i in range(len(sections)):
            if sections[i] == " ":
                continue
            if i % 2 == 0:
                new_node = TextNode(sections[i], TextType.TEXT.value)
                tmp_list.append(new_node)
            else:
                new_node = TextNode(sections[i], text_type)
                tmp_list.append(new_node)

        new_nodes.extend(tmp_list)

    return new_nodes


def split_nodes_images(old_nodes):

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        matches_list = extract_markdown_images(original_text)

        if len(matches_list) == 0:
            new_nodes.append(old_node)
            continue
        
        temp_list = []
        for i in range(len(matches_list)):
            image_alt = matches_list[i][0]
            image_link = matches_list[i][1]
            sections = original_text.split(f'![{image_alt}]({image_link})', 1)

            if len(sections[0]) == 0:
                continue

            plain_textnode = TextNode(sections[0], TextType.TEXT)
            image_textnode = TextNode(image_alt, TextType.IMAGE, image_link)
            temp_list.append(plain_textnode)
            temp_list.append(image_textnode)

            # Account for text after the final image link markdown
            if i == len(matches_list) - 1 and len(sections[1]) != 0:
                last_textnode = TextNode(sections[1], TextType.TEXT)
                temp_list.append(last_textnode)

            original_text = sections[1]     # Continue to next iteration with the section after the current image alt text and link
        
        new_nodes.extend(temp_list)

    return new_nodes


def split_nodes_links(old_nodes):
    
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != "text":
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        matches_list = extract_markdown_links(original_text)

        if len(matches_list) == 0:
            new_nodes.append(old_node)
            continue

        temp_list = []
        for i in range(len(matches_list)):
            link_alt = matches_list[i][0]
            link_url = matches_list[i][1]
            sections = original_text.split(f'[{link_alt}]({link_url})', 1)

            if len(sections[0]) == 0:
                continue
            
            plain_textnode = TextNode(sections[0], TextType.TEXT)
            link_textnode = TextNode(link_alt, TextType.LINK, link_url)
            temp_list.append(plain_textnode)
            temp_list.append(link_textnode)

            if i == len(matches_list) - 1 and len(sections[1]) != 0:
                last_textnode = TextNode(sections[1], TextType.TEXT)
                temp_list.append(last_textnode)

            original_text = sections[1]

        new_nodes.extend(temp_list)

    return new_nodes


def extract_markdown_images(text):
    image_md_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_md_matches


def extract_markdown_links(text):
    link_md_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_md_matches