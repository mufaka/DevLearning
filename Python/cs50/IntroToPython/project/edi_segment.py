from edi_node import EdiNode 
from edi_element import EdiElement

class EdiSegment(EdiNode):
    def __init__(self, name):
        super().__init__(name)

    @classmethod
    def populate_from_raw(cls, raw_edi, delimiters):
        # CTX*CLM01:123456789~
        # CTX*SITUATIONAL TRIGGER*CLM*43**5:3~
        # BGM*SubA-1:SubB-1^SubA-2:SubB-2^SubA-3:SubB-3*Field2~
        parts = raw_edi.split(delimiters["element"])

        position = 0
        segment_name = parts[0]

        segment = EdiSegment(segment_name)
        for part in parts:
            if position > 0:
                name = f"{segment_name}{position:02d}"
            else:
                name = "ID"

            edi_element = EdiElement(name)
            edi_element.populate_from_raw(part, delimiters)
            edi_element.parent = segment 
            segment.add_child(edi_element)
            position += 1

        return segment

    def __str__(self):
        return self.name 