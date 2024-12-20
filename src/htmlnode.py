class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for prop, val in self.props.items():
            props_str += f' {prop}="{val}"'
        return props_str
    
    def __repr__(self):
        return f'HTMLNode(tag="{self.tag}", value="{self.value}", children={self.children}, props={self.props})'
    

class LeafNode(HTMLNode):

    def __init__(self, value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
    
    def to_html(self):
        if self.value is None:
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
            
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
            

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None or self.tag == "":
            raise ValueError("ParentNode tag is required.")
        if self.children == None:
            raise ValueError("ParentNode children are required.")
        children_html = f'<{self.tag}>'
        for child in self.children:
            children_html += f'{child.to_html()}'
        if self.props:
            return f'{self.props_to_html()}{children_html}</{self.tag}>'
        else:
            return f'{children_html}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props})'
