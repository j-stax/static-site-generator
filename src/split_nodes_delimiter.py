from textnode import *

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
        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdown syntax")      
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



if __name__ == '__main__':
#   node = TextNode("This text has a **bold** word.", "text")
#   new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    node = TextNode("This text has a `code block` here, and another `code block` here.", "text")
    new_nodes = split_nodes_delimiter([node], "`", "code")
    print(new_nodes)         


