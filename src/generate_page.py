import os, pathlib

from markdown_blocks import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):

    # Iterate through source directory
    for filename in os.listdir(dir_path_content):   
        # Create the file path to this filename
        file_path = os.path.join(dir_path_content, filename)

        # File path is a file
        if os.path.isfile(file_path):
            path = pathlib.Path(file_path)
            # File is a Markdown file
            if path.suffix == '.md':
                generate_page(file_path, template_path, f'{dest_dir_path}/index.html')
        elif os.path.isdir(file_path):  # File path leads to a directory
            # print(f'----------file_path: {file_path}')
            # print(f'----------dest_dir_path: {dest_dir_path}')

            dest_file_path = os.path.join(dest_dir_path, filename)
            # print(f'----------dest_file_path: {dest_file_path}')

            # Create the directory in the destination file path
            os.mkdir(dest_file_path)

            # Recursive call
            generate_pages_recursive(file_path, template_path, dest_file_path)


def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} --> {dest_path} using {template_path}')

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
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            text = line[2:].strip()
            return text
    raise ValueError("Error: No h1 header found.")
