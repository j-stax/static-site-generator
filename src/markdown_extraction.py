import re

def extract_markdown_images(text):
    image_md_matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return image_md_matches

def extract_markdown_links(text):
    link_md_matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return link_md_matches


