from markdown_extraction import *
from textnode import *

def split_nodes_images(old_nodes):

    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        matches_list = extract_markdown_images(original_text)

        if len(matches_list) == 0:
            return [old_node]
        
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
            original_text = sections[1]
        
        new_nodes.extend(temp_list)

    return new_nodes


def split_nodes_links(old_nodes):
    
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        matches_list = extract_markdown_links(original_text)
        temp_list = []
        for match in matches_list:
            link_alt = match[0]
            link_url = match[1]
            sections = original_text.split(f'[{link_alt}]({link_url})', 1)
            if len(sections[0]) == 0:
                continue
            plain_textnode = TextNode(sections[0], TextType.TEXT)
            link_textnode = TextNode(link_alt, TextType.LINK, link_url)
            temp_list.append(plain_textnode)
            temp_list.append(link_textnode)
            original_text = sections[1]

        new_nodes.extend(temp_list)

    return new_nodes



if __name__ == '__main__':
    node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_links([node])
    print(new_nodes)
