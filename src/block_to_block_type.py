import re

def block_to_block_type(block):
    heading_matches = re.findall(r"^(?!#{7,})#{1,6} ", block)
    code_matches = re.findall(r"^```(.*?)```$", block)
    quote_matches = re.findall(r"^>(?!>)", block)
    ul_matches = re.findall(r"^[-*] .*(\n[-*] .*)*$", block)
    ol_matches = re.findall(r"^[1-9][0-9]*\. (?!\.)(.*)(\n[1-9][0-9]*\. (?!\.).*)*$", block)

    if len(heading_matches) > 0: 
        return f'h{len(heading_matches[0])-1}'
    if len(code_matches) > 0:
        return "code"
    if len(quote_matches) > 0:
        return "blockquote"
    if len(ul_matches) > 0:
        return "ul"
    if len(ol_matches) > 0:
        return "ol"
    
    return "p"


if __name__ == '__main__':
    text = "### This is an h3 block."
    text2 = "1. ordered list block.\n2. ordered list block.\n3. ordered list block."
    print(block_to_block_type(text))
    print(block_to_block_type(text2))