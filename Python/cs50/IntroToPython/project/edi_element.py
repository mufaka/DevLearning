class EdiElement:
    """
    Represents a single element within a segment

    Although infrequent, EDI Elements can be repeating as well as being composite which
    makes modeling a little bit of a challenge. In a segment, positionally,
    there can be multiple occurences of an element and that element can have
    multiple occurences of positional values. 

    eg:
    BGM*SubA-1:SubB-1^SubA-2:SubB-2^SubA-3:SubB-3*Field2~

    Here, BGM-01 (first element of the BGM segment) has the following values:
    BGM-01[0] = SubA-1, SubB-1
    BGM-01[1] = SubA-2, SubB-2
    BGM-01[2] = SubA-3, SubB-3

    To support this edge case, EdiElement encapsulates an array of EdiElement that
    has an array of composite values.

    A convenience property, value, is provided for getting the first composite value
    of the first sub element.
    """
    def __init__(self):
        self._sub_elements = []
        self._values = []

    @property
    def sub_elements(self):
        return self._sub_elements 

    @sub_elements.setter 
    def sub_elements(self, sub_elements):
        self._sub_elements = sub_elements 

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, values):
        self._values = values 

    @property
    def value(self):
        """
        A convenience property that returns the value of the first sub elements
        first composite value.
        """
        if len(self._sub_elements) > 0:
            sub_element = self._sub_elements[0]
            return sub_element.values[0] if len(sub_element.values) > 0 else ""

        return "" 
    
    def populate_from_raw(self, raw_edi, delimiters):
        # CTX*CLM01:123456789~
        # CTX*SITUATIONAL TRIGGER*CLM*43**5:3~
        # BGM*SubA-1:SubB-1^SubA-2:SubB-2^SubA-3:SubB-3*Field2~
        elements = raw_edi.split(delimiters["repeat"])

        for element in elements:
            sub_element = EdiElement()
            sub_element.values = raw_edi.split(delimiters["composite"])
            self._sub_elements.append(sub_element)
        