from edi_element import EdiElement

class EdiSegment:
    def __init__(self):
        self._elements = []

    @property
    def name(self):
        return self.elements[0].value if len(self._elements) > 0 else None 

    @property
    def elements(self):
        return self._elements

    def add_element(self, edi_element):
        self._elements.append(edi_element)

    def populate_from_raw(self, raw_edi, delimiters):
        # CTX*CLM01:123456789~
        # CTX*SITUATIONAL TRIGGER*CLM*43**5:3~
        # BGM*SubA-1:SubB-1^SubA-2:SubB-2^SubA-3:SubB-3*Field2~
        parts = raw_edi.split(delimiters["element"])

        for part in parts:
            edi_element = EdiElement()
            edi_element.populate_from_raw(part, delimiters)
            self._elements.append(edi_element)

    def __str__(self):
        return self.name 