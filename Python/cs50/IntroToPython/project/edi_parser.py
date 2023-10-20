import codecs
import os
from edi_document import EdiDocument 
from edi_transaction import EdiTransaction 
from edi_segment import EdiSegment 
from edi_loop import EdiLoop 
from edi_element import EdiElement 
from openedi_spec import OpenEDISpec 
from openedi_spec_loader import OpenEDISpecLoader

class EdiParser:
    DELIMITER_NAME_ELEMENT = "element"
    DELIMITER_NAME_COMPOSITE = "composite"
    DELIMITER_NAME_SEGMENT = "segment"
    DELIMITER_NAME_REPEAT = "repeat"

    def __init__(self):
        self._edi_document = EdiDocument()
        self._raw_edi = "" 
        self._raw_segments = []
        self._delimiters = {}

    def parse_file(self, file_path) -> EdiDocument:
        with open(file_path, "r") as edi_file:
            # some files may have a BOM
            file_text = edi_file.read().strip(codecs.BOM_UTF8.decode(edi_file.encoding))
            edi_file.close()
        return self.parse_text(file_text)

    def parse_text(self, file_text) -> EdiDocument:
        self._raw_edi = file_text 
        self._populate_delimiters()
        return self._build_structured_documents()

    def _build_structured_documents(self):
        # temp_document contains all segments from the file but
        # do not have a structure other than being populated
        temp_document = self._populate_document()

        # use the OpenEDI specs to create structured documents from
        # the temp_document transaction sets (1 document per transaction_set)
        spec_loader = OpenEDISpecLoader("openedi_schemas")
        transaction_set, implementation = temp_document.document_type 
        spec_key = OpenEDISpecLoader.get_message_key(transaction_set, "X12", implementation)
        openedi_spec = OpenEDISpec(spec_loader.read_openedi_message_by_key(spec_key))
        openedi_schema = openedi_spec.get_schema_tree()

        documents = []

        for transaction_set in temp_document.transaction_sets:
            documents.append(self._build_structured_document(transaction_set, openedi_schema))

        return documents 

    def _build_structured_document(self, transaction_set, open_edi_schema):
        self._debug_schema(open_edi_schema, 0)
        return None 

    def _debug_schema(self, open_edi_schema, level):
        print("    " * level, open_edi_schema.name)

        level += 1
        for child_schema in open_edi_schema.children:
            self._debug_schema(child_schema, level)

    def _populate_delimiters(self):
        self._delimiters[EdiParser.DELIMITER_NAME_ELEMENT] = self._raw_edi[3]
        self._delimiters[EdiParser.DELIMITER_NAME_COMPOSITE] = self._raw_edi[104]
        self._delimiters[EdiParser.DELIMITER_NAME_SEGMENT] = self._raw_edi[105]
        self._raw_segments = self._raw_edi.split(self._raw_edi[105])
        isa_elements = self._raw_segments[0].split(self._raw_edi[3])
        self._delimiters[EdiParser.DELIMITER_NAME_REPEAT] = isa_elements[11]

    def _populate_document(self):
        document = EdiDocument()
        document.delimiters = self._delimiters
        document.all_segments_raw = self._raw_segments

        current_transaction = None

        for raw_segment in self._raw_segments:
            segment = EdiSegment()
            segment.populate_from_raw(raw_segment, document.delimiters)

            if segment.name == "ISA":
                document.isa_header = segment 
            elif segment.name == "IEA":
                document.isa_trailer = segment 
            elif segment.name == "GS":
                document.functional_group_header = segment 
            elif segment.name == "GE":
                # catch the last transaction
                if current_transaction != None:
                    document.add_transaction_set(current_transaction)

                document.functional_group_trailer = segment 
            elif segment.name == "ST":
                # new transaction
                if current_transaction != None:
                    document.add_transaction_set(current_transaction)
                current_transaction = EdiTransaction()
                current_transaction.add_raw_segment(raw_segment, document.delimiters)
            else:
                if current_transaction != None:
                    current_transaction.add_raw_segment(raw_segment, document.delimiters)

        return document
