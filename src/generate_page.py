import os
from markdown_blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type, block_type_heading


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    # Open Markdown and HTML template files
    md_file = open(from_path)
    template_file = open(template_path)
    
    md = md_file.read()
    template = template_file.read()

    # Close files
    md_file.close()
    template_file.close()

    # Convert Markdown to HTML
    md_to_html = markdown_to_html_node(md).to_html()
    title = extract_title(md)

    # Inject title and newly converted html into the template
    rendered_html = template.replace('{{Title}}', title)
    rendered_html = rendered_html.replace('{{Content}}', md_to_html)

    # Create directory if it doesn't exist
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)

    # Write the new markup to a file
    with open(dest_path, 'w') as new_file:
        new_file.write(rendered_html)
    

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            if block.startswith("# "):
                text = block[2:].strip()
                return text
    raise ValueError("Error: No h1 header found.")
