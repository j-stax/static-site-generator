from copy_directory_contents import copy_directory_contents

def main():
    src_dir = './static'
    dst_dir = './public'
    copy_directory_contents(src_dir, dst_dir)

main()