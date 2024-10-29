from copy_directory_contents import copy_directory_contents
from generate_page import generate_pages_recursive

def main():
    src_dir = './static'
    dst_dir = './public'
    dir_path_content = './content'
    template_path = 'template.html'
    dest_path = './public'

    copy_directory_contents(src_dir, dst_dir)
    generate_pages_recursive(dir_path_content, template_path, dest_path)

main()