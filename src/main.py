from copy_directory_contents import copy_directory_contents
from generate_page import generate_page

def main():
    src_dir = './static'
    dst_dir = './public'
    from_path = './content/index.md'
    template_path = 'template.html'
    dest_path = './public/index.html'

    copy_directory_contents(src_dir, dst_dir)
    generate_page(from_path, template_path, dest_path)

main()