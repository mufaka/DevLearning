import os 
import codecs
from openedi_spec_loader import OpenEDISpecLoader
from openedi_spec import OpenEDISpec 
from dict_util import DictUtil 
from edi_parser import EdiParser 
from edi_segment import EdiSegment

def main():
    # instantiate a specification loader with a path to spec files
    spec_loader = OpenEDISpecLoader("openedi_schemas")

    # get a dictionary with mappings for all spec files
    message_file_map = spec_loader.get_message_file_map()

    # get an individual spec
    #eligibility_response_spec = spec_loader.read_openedi_message_by_key("270:X12:None")
    eligibility_response_spec = spec_loader.read_openedi_message_by_key("999:X12:005010X231A1")

    # create an OpenEDISpec with the loaded spec
    open_edi_spec = OpenEDISpec(eligibility_response_spec)

    #schema_tree = open_edi_spec.get_schema_tree()
    #schema_tree.debug_node()

    file_name = os.path.join("edi_samples", "999-response-to-3-837s.edi")
    #file_name = os.path.join("edi_samples", "837P-ambulance.edi")
    #file_name = os.path.join("edi_samples", "delete.txt")

    parser = EdiParser()
    documents = parser.parse_file(file_name)

    

if __name__ == "__main__":
    main()
