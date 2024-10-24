class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        props_str = ""
        for prop, val in self.props.items():
            props_str += f' {prop}=\"{val}\"'
        return props_str
    
    def __repr__(self):
        return f'HTMLNode(tag=\"{self.tag}\", value=\"{self.value}\", children={self.children}, props={self.props})'
    

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value is required.")
        elif self.tag == None:
            return f'{self.value}'
        else:
            if self.props:
                if self.tag == "img":
                    return f'<{self.tag}{self.props_to_html()} />'
                return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
            

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("ParentNode tag is required.")
        elif not self.children:
            raise ValueError("ParentNode children are required.")
        else:
            html = f'<{self.tag}>'
            for child in self.children:
                html += f'{child.to_html()}'
            return f'{html}</{self.tag}>'
