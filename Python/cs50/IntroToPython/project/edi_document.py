from edi_segment import EdiSegment 
from edi_transaction import EdiTransaction 

class EdiDocument:
    def __init__(self):
        self._isa_header = EdiSegment()
        self._isa_trailer = EdiSegment()
        self._transaction_sets = []
        self._functional_group_header = EdiSegment()
        self._functional_group_trailer = EdiSegment()
        self._all_segments_raw = []
        self._delimiters = {}

    @property
    def isa_header(self):
        return self._isa_header

    @isa_header.setter
    def isa_header(self, isa_header):
        self._isa_header = isa_header 

    @property
    def isa_trailer(self):
        return self._isa_trailer

    @isa_trailer.setter
    def isa_trailer(self, isa_trailer):
        self._isa_trailer = isa_trailer 

    @property
    def functional_group_header(self):
        return self._functional_group_header

    @functional_group_header.setter 
    def functional_group_header(self, functional_group_header):
        self._functional_group_header = functional_group_header

    @property
    def functional_group_trailer(self):
        return self._functional_group_trailer

    @functional_group_trailer.setter 
    def functional_group_trailer(self, functional_group_trailer):
        self._functional_group_trailer = functional_group_trailer

    @property
    def document_type(self):
        """
        Returns a Tuple of Transaction Set Identifier Code (ST01) and Implementation Convention Reference (GS08).
        ST03 also contains the Implementation Convention Reference for some specfications but not all.

        By specification, all Transaction Sets (ST) must be of the same type in a single document so it is OK
        to just get the information at the document level.

        This information allows for determining which specification matches the provided EDI.
        """
        if len(self._functional_group_header.elements) >=8:
            if len(self._transaction_sets) > 0:
                return self._transaction_sets[0].segments[0].elements[1].value, self._functional_group_header.elements[8].value

    @property
    def transaction_sets(self):
        return self._transaction_sets 

    def add_transaction_set(self, transaction_set):
        self._transaction_sets.append(transaction_set)
        
    @property
    def all_segments_raw(self):
        return self._all_segments_raw

    @all_segments_raw.setter 
    def all_segments_raw(self, all_segments):
        self._all_segments_raw = all_segments         

    @property
    def delimiters(self):
        return self._delimiters

    @delimiters.setter
    def delimiters(self, delimiters):
        self._delimiters = delimiters 
