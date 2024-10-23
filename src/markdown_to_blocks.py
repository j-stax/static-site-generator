def markdown_to_blocks(markdown):
    sections = markdown.split("\n\n")
    block_strings = []
    for section in sections:
        if len(section) == 0:
            continue
        block_strings.append(section.strip())
    return block_strings


if __name__ == '__main__':
    md = "# This is a heading\n\n" \
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n" \
            "* This is the first list item in a list block\n" \
            "* This is a list item\n" \
            "* This is another list item"
    block_strings = markdown_to_blocks(md)
    for string in block_strings:
        print(f'> {string}')