import os

def copy_directory_contents(src_dir, dst_dir):
    # Remove existing contents in the destination directory
    for filename in os.listdir(dst_dir):
        file_path = os.path.join(dst_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                delete_directory(file_path)     # Call to delete_directory
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    
    # Copy contents from the source directory
    for filename in os.listdir(src_dir):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)
        try:
            if os.path.isfile(src_path) or os.path.islink(src_path):
                with open(src_path, 'rb') as src_file:
                    with open(dst_path, 'wb') as dst_file:
                        dst_file.write(src_file.read())
            elif os.path.isdir(src_path):
                os.mkdir(dst_path)
                copy_directory_contents(src_path, dst_path)
        except Exception as e:
            print(f'Failed to copy {src_path}. Reason: {e}')


# Recursively delete contents for a given directory
def delete_directory(dir_path):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                delete_directory(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')
    os.rmdir(dir_path)


if __name__ == '__main__':
    src_dir = "../static"
    dst_dir = "../test"
    copy_directory_contents(src_dir, dst_dir)
        
    