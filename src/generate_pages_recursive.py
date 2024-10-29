import os, pathlib

from generate_page import generate_page

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

