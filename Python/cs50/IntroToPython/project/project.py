import os 
from edi_parser import EdiParser 

def main():
    #file_name = os.path.join("edi_samples", "270-generic-request-dependent.edi")
    file_name = os.path.join("edi_samples", "999-response-to-3-837s.edi")

    parser = EdiParser()
    document = parser.parse_file(file_name)

    for transaction_set in document.transaction_sets:
        transaction_set.debug_node()

if __name__ == "__main__":
    main()
