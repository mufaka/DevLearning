class SchemaNode:
    def __init__(self, name, schema):
        self._name = name
        self._schema = schema
        self._parent = None 
        self._value = None
        self._children = [] 

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter 
    def value(self, value):
        self._value = value

    @property
    def schema(self):
        return self._schema 

    @property
    def parent(self):
        return self._parent

    @parent.setter 
    def parent(self, schema_node):
        self._parent = schema_node
    
    def add_child(self, schema_node):
        self._children.append(schema_node)

    @property 
    def children(self):
        return self._children 

    def debug_node(self):
        self.debug_node_recursive(self, 0)

    def debug_node_recursive(self, schema_node, level):
        print("    " * level, f"{schema_node.name}")

        for child in schema_node.children:
            self.debug_node_recursive(child, level + 1)

