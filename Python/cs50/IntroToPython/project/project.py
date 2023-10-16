from openedi_spec_loader import OpenEDISpecLoader
from openedi_spec import OpenEDISpec 
from dict_util import DictUtil 

def main():
    # instantiate a specification loader with a path to spec files
    spec_loader = OpenEDISpecLoader("openedi_schemas")

    # get a dictionary with mappings for all spec files
    message_file_map = spec_loader.get_message_file_map()

    # get an individual spec
    eligibility_response_spec = spec_loader.read_openedi_message_by_key("271:X12:None")

    # create an OpenEDISpec with the loaded spec
    open_edi_spec = OpenEDISpec(eligibility_response_spec)

    # get the root schema
    root_schema = open_edi_spec.get_root_schema()
    #print(root_schema)

    # get a specific schema from spec
    # #/components/schemas/ST
    #st = DictUtil.get_value_by_reference_path(open_edi_spec.spec, "#/components/schemas/ST")
    #st = DictUtil.get_value_by_reference_path(open_edi_spec.spec, "#/3/0/ST")

    st = DictUtil.get_value_by_reference_path(open_edi_spec.spec, "#/3/0/STA")

    print(st)

    

if __name__ == "__main__":
    main()
