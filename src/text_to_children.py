from inline_markdown import text_to_textnode
from textnode import text_node_to_html_node

def text_to_children(text):
    children_list = []
    text_to_textnode_list = text_to_textnode(text)

    # Markdown text has no inline elements
    if len(text_to_textnode_list) == 1:
        return None
    
    for textnode in text_to_textnode_list:
        new_leafnode = text_node_to_html_node(textnode)
        # Only append nodes that have been assigned a tag
        if new_leafnode.tag:
            children_list.append(new_leafnode)

    return children_list