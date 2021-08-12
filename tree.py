
class Tree:
    """
    Represents an ordinary tree data structure
    """
    def __init__(self, id, parent=None):
        self._id = id
        self._children = []
        self._parent = None
        if parent != None:
            if isinstance(parent, Tree):
                parent.add_child(self)
            else:
                raise TypeError("Invalid type: {0} as parent".format(type(parent)))

    # Attributes
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise TypeError("Read-only attribute")

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self.attach(value)

    @property
    def children(self):
        return self._children[:]

    @children.setter
    def children(self, parent):
        raise TypeError("Read-only attribute")

    # Functions
    def find_child_id(self, id):
        numchild = len([item for item in self._children if item._id == id])
        if numchild == 0:
            return False
        if numchild != 1:
            raise ValueError("Duplicated child")
        return True

    def add_child(self, child):
        if not isinstance(child, Tree):
            raise TypeError("Invalid type: {0} as child".format(type(child)))
        child.detach()
        if self.find_child_id(child._id):
            raise ValueError("Duplicated child")
        self._children.append(child)
        self._children.sort(key=lambda item: item.id)
        child._parent = self

    def remove_child(self, child):
        if child in self._children:
            self._children.remove(child)
            child._parent = None

    def detach(self):
        """Removes this child from tree"""
        if self._parent == None:
            # Already detached or root node: noting to do
            return
        self._parent.remove_child(self)

    def attach(self, parent):
        """Connects this node as child to parent."""
        parent.add_child(self)

    def walk(self, nodelist=None):
        if nodelist == None:
            nodelist = []
        nodelist.append(self)
        for child in self._children:
            nodelist = child.walk(nodelist)
        return nodelist

    def walk_id(self, idlist=None):
        if idlist == None:
            idlist = []
        idlist.append(self._id)
        for child in self._children:
            idlist = child.walk_id(idlist)
        return idlist
