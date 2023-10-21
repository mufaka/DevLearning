from edi_node import EdiNode
from edi_segment import EdiSegment

class EdiTransaction(EdiNode):
    def __init__(self, name):
        super().__init__(name)

    def add_raw_segment(self, raw_segment, delimiters):
        segment = EdiSegment.populate_from_raw(raw_segment, delimiters)
        segment.parent = self 
        self._children.append(segment)
