class EdiNode:
    def __init__(self, name):
        self._name = name
        self._parent = None
        self._children = [] 

    @property
    def name(self):
        return self._name 

    @name.setter 
    def name(self, name):
        self._name = name 

    @property
    def parent(self):
        return self._parent 

    @parent.setter 
    def parent(self, parent):
        self._parent = parent 

    @property 
    def children(self):
        return self._children 

    def add_child(self, child):
        child.parent = self 
        self._children.append(child)

    def debug_node(self):
        self._print_node_recursive(self, 0)

    def _print_node_recursive(self, edi_node, level):
        if hasattr(edi_node, "sub_elements"):
            print("   " * level, edi_node.name)

            for element in edi_node.sub_elements:
                print("   " * (level + 1), element.values)

        else:
            print("   " * level, edi_node.name)

        for child_node in edi_node.children:
            self._print_node_recursive(child_node, level + 1)
    