import codecs
import os
from edi_document import EdiDocument 
from edi_transaction import EdiTransaction 
from edi_segment import EdiSegment 
from edi_loop import EdiLoop 
from edi_element import EdiElement 
from openedi_spec import OpenEDISpec 
from openedi_spec_loader import OpenEDISpecLoader
from schema_node import SchemaNode, SchemaNodeType 

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
        return self._build_structured_document()

    def _build_structured_document(self):
        # temp_document contains all segments from the file but
        # do not have a structure other than being populated
        temp_document = self._populate_document()

        # use the OpenEDI specs to create a structured document from
        # the temporary document
        spec_loader = OpenEDISpecLoader("openedi_schemas")
        transaction_set, implementation = temp_document.document_type 
        spec_key = OpenEDISpecLoader.get_message_key(transaction_set, "X12", implementation)
        openedi_spec = OpenEDISpec(spec_loader.read_openedi_message_by_key(spec_key))
        openedi_schema = openedi_spec.get_schema_tree()

        structured_document = EdiDocument()
        structured_document.isa_header = temp_document.isa_header 
        structured_document.isa_trailer = temp_document.isa_trailer 
        structured_document.functional_group_header = temp_document.functional_group_header
        structured_document.functional_group_trailer = temp_document.functional_group_trailer 

        for transaction in temp_document.transaction_sets:
            structured_document.transaction_sets.append(self._build_structured_transaction(transaction, openedi_schema))

        return structured_document 

    def _build_structured_transaction(self, transaction_set, openedi_schema):
        #st_spec = self._get_schema_child_by_name(openedi_schema, "ST")
        transaction = EdiTransaction("Transaction")
        current_object = transaction 
        current_schema = openedi_schema 

        for segment in transaction_set.children:
            segment_schema = self._get_schema_child_by_name(current_schema, segment.name)
            
            if segment_schema != None:
                # no add_segment anymore
                current_object.add_child(segment)
            else:
                while True:
                    loop_schema = self._get_loop_schema(current_schema, segment)
                    if loop_schema != None:
                        edi_loop = EdiLoop(loop_schema.id)
                        edi_loop.add_child(segment)
                        current_object.add_child(edi_loop)
                        current_object = edi_loop
                        current_schema = loop_schema 
                        break
                    else:
                        if current_schema.parent != None:
                            current_schema = current_schema.parent #if current_schema.parent != None else current_schema 
                            current_object = current_object.parent #if current_object.parent != None else current_object
                        else:
                            # couldn't find the appropriate place for the segment
                            break

        return transaction 

    def _get_schema_child_by_name(self, openedi_schema, name):
        for child_schema in openedi_schema.children:
            if child_schema.id == name:
                return child_schema
        
        return None

    def _get_loop_schema(self, openedi_schema, segment):
        for child_schema in openedi_schema.children:
            if child_schema.node_type == SchemaNodeType.LOOP:
                loop_segment_id, allowed_values = child_schema.get_loop_markers()

                if loop_segment_id == segment.name:
                    if allowed_values == None:
                        return child_schema 
                    else:
                        if segment.children[1].value in allowed_values:
                            return child_schema 
                else:
                    temp_schema = self._get_loop_schema(child_schema, segment)    

                    if temp_schema != None:
                        return temp_schema 

        return None

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
            segment = EdiSegment.populate_from_raw(raw_segment, document.delimiters)

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
                current_transaction = EdiTransaction("ST")
                current_transaction.add_raw_segment(raw_segment, document.delimiters)
            else:
                if current_transaction != None:
                    current_transaction.add_raw_segment(raw_segment, document.delimiters)

        return document
