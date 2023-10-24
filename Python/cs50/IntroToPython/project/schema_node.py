from enum import Enum 

class SchemaNodeType(Enum):
    UNKNOWN = 1
    ROOT = 2
    LOOP = 3
    SEGMENT = 4
    ELEMENT = 5
    COMPOSITE = 6
    ENUM = 7
    GROUP = 8

class SchemaNode:
    def __init__(self, name, schema):
        self._name = name
        self._schema = schema
        self._parent = None 
        self._children = []
        self._allowed_values = []

    @property
    def node_type(self):
        if "x-edination-message-id" in self._schema.keys():
            return SchemaNodeType.ROOT
        elif "x-edination-loop-id" in self._schema.keys():
            return SchemaNodeType.LOOP 
        elif "x-edination-segment-id" in self._schema.keys():
            return SchemaNodeType.SEGMENT 
        elif "x-edination-composite-id" in self._schema.keys():
            return SchemaNodeType.COMPOSITE
        elif "x-edination-element-id" in self._schema.keys():
            return SchemaNodeType.ELEMENT 
        elif "enum" in self._schema.keys():
            return SchemaNodeType.ENUM
        elif "x-edination-group-type" in self._schema.keys():
            return SchemaNodeType.GROUP 
        else:
            return SchemaNodeType.ELEMENT 

    @property
    def id(self):
        if "x-edination-message-id" in self._schema.keys():
            return self._schema["x-edination-message-id"]
        elif "x-edination-loop-id" in self._schema.keys():
            return self._schema["x-edination-loop-id"]
        elif "x-edination-segment-id" in self._schema.keys():
            return self._schema["x-edination-segment-id"]
        elif "x-edination-composite-id" in self._schema.keys():
            return self._schema["x-edination-composite-id"]
        elif "x-edination-element-id" in self._schema.keys():
            return self._schema["x-edination-element-id"]
        elif "x-edination-group-type" in self._schema.keys():
            return f"Group - {self.name}"
        else:
            return None

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        self._name = name

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

    @property
    def allowed_values(self):
        if "enum" in self._schema.keys():
            return self._schema["enum"]

    def get_loop_markers(self):
        """
        Returns a tuple containing the first segment name of the
        loop and an array of allowable values for the first element
        in that segment
        """
        if (self.node_type == SchemaNodeType.LOOP or self.node_type == SchemaNodeType.GROUP) and len(self._children) > 0:
            # assume first child is Segment?
            first_segment = self._children[0]

            if len(first_segment.children) > 0:
                first_element = first_segment.children[0]

                # enum is child of element and carries allowed values
                if len(first_element.children) > 0:
                    if first_element.node_type == SchemaNodeType.COMPOSITE:
                        first_element = first_element.children[0]

                    if len(first_element.children) > 0:
                        return first_segment.id, first_element.children[0].allowed_values

            return first_segment.id, None
        return None 

    def debug_node(self):
        self.debug_node_recursive(self, 0)

    def debug_node_recursive(self, schema_node, level):
        print("    " * level, f"{schema_node.id} {schema_node.name}")
        print("    " * (level + 1), f"{schema_node.get_loop_markers()}")

        for child in schema_node.children:
            self.debug_node_recursive(child, level + 1)

