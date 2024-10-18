from htmlnode import *

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None or self.value == "":
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            if self.props:
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'

if __name__ == '__main__':
    def main():
        leafnode = LeafNode(tag="a", value="This is an anchor tag", props={ "href": "https://www.boot.dev" })
        print(leafnode.props_to_html())

    main()