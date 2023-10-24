from dict_util import DictUtil
from schema_node import SchemaNode

class OpenEDISpec:
    def __init__(self, spec):
        """
        A wrapper for a dictionary that is in the OpenEDI specification
        format. OpenEDI implements the OpenAPI Schema Object for defining
        message structure and rules.

        OpenEDI documentation: https://github.com/EdiNation/OpenEDI-Specification

        OpenEDI extends OpenAPI with the following attributes. Note, x-openedi
        appears to have been replaced with x-edination

        NOTE: x-openedi is used in the documentation but it appears that x-edination is used "in the wild"

        EDI Message
            x-openedi-message-standard
            x-openedi-message-id
            x-openedi-message-version (optional; exists if multiple implementations of message type)

        EDI Loop
            x-openedi-loop-id

        EDI Segment
            x-openedi-segment-id

        EDI Composite Data Element
            x-openedi-composite-id

        EDI Data Element
            x-openedi-element-id

        EDI Syntax Rules
            x-openedi-syntax (optional, refer to https://github.com/EdiNation/OpenEDI-Specification#edi-syntax-rules)

        EDI Situational Rules
            x-openedi-situational (optional, refer to https://github.com/EdiNation/OpenEDI-Specification#edi-situational-rules)

        Additional grouping of EDI Loops or EDI segments
            x-openedi-group-type

        EDI Sequences
            x-openedi-loop-seq

        :param spec: A dictionary in the OpenEDI specification format.
        :type spec: dict
        """
        self._spec = spec

    def get_root_schema(self):
        return DictUtil.get_dict_containing(self._spec, "x-edination-message-id")

    def get_schemas(self):
        return DictUtil.get_value_by_reference_path(self._spec, "#/components/schemas")

    @property
    def spec(self):
        return self._spec

    def get_schema_tree(self):
        # schema objects are a dictionary with a 'properties' key, among other keys that 
        # define properties and sub-schemas
        root_schema = self.get_root_schema()
        root_node = SchemaNode(root_schema["x-edination-message-id"], root_schema)
        # TODO: set a node type; are there enums in python?
        self._get_schema_tree_recursive(root_schema, root_node)

        return root_node

    def _get_schema_tree_recursive(self, schema, parent_node):
        for k, v in schema["properties"].items():
            if type(v) is dict:
                if "$ref" in v.keys():
                    ref_schema = DictUtil.get_value_by_reference_path(self._spec, v["$ref"])
                    ref_node = SchemaNode(k, ref_schema)
                    ref_node.parent = parent_node 
                    parent_node.add_child(ref_node)
                    
                    self._get_schema_tree_recursive(ref_schema, ref_node)
                elif "type" in v.keys() and v["type"] == "array":
                    if "items" in v.keys() and "$ref" in v["items"].keys():
                        ref_schema = DictUtil.get_value_by_reference_path(self._spec, v["items"]["$ref"])
                        ref_node = SchemaNode(k, ref_schema)
                        ref_node.parent = parent_node 
                        parent_node.add_child(ref_node)
                        
                        self._get_schema_tree_recursive(ref_schema, ref_node)
                    else:
                        ref_node = SchemaNode(k, v)
                        ref_node.parent = parent_node 
                        parent_node.add_child(ref_node)

                        refs = None 

                        if "allOf" in v.keys(): 
                            refs = v["allOf"]
                        elif "anyOf" in v.keys():
                            refs = v["anyOf"]
                        elif "oneOf" in v.keys():
                            refs = v["oneOf"]
                        
                        if refs:
                            for ref in refs:
                                of_schema = DictUtil.get_value_by_reference_path(self._spec, ref["$ref"])
                                of_node = SchemaNode(k, of_schema)
                                of_node.parent = ref_node 
                                ref_node.add_child(of_node)
                else:
                    # assume this is an element?
                    ref_node = SchemaNode(k, v)
                    ref_node.parent = parent_node 
                    parent_node.add_child(ref_node)

                    refs = None 

                    if "allOf" in v.keys(): 
                        refs = v["allOf"]
                    elif "anyOf" in v.keys():
                        refs = v["anyOf"]
                    elif "oneOf" in v.keys():
                        refs = v["oneOf"]
                    
                    if refs:
                        for ref in refs:
                            of_schema = DictUtil.get_value_by_reference_path(self._spec, ref["$ref"])
                            of_node = SchemaNode(k, of_schema)
                            of_node.parent = ref_node 
                            ref_node.add_child(of_node)


'''
          "EntityIdentifierCode_01": {
            "type": "string",
            "allOf": [
              {
                "$ref": "#/components/schemas/X12_ID_98_56"
              }
            ],
            "x-edination-element-id": "98"
          },
          "EntityTypeQualifier_02": {
            "type": "string",
            "allOf": [
              {
                "$ref": "#/components/schemas/X12_ID_1065_2"
              }
            ],
            "x-edination-element-id": "1065"
          },

      "TS999": {
        "type": "object",
        "properties": {
          "Model": {
            "type": "string"
          },
          "ST": {
            "$ref": "#/components/schemas/ST"
          },
          "AK1": {
            "$ref": "#/components/schemas/AK1"
          },
          "Loop_2000": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Loop_2000"
            }
          },
          "AK9": {
            "$ref": "#/components/schemas/AK9"
          },
          "SE": {
            "$ref": "#/components/schemas/SE"
          }
        },
        "x-edination-message-id": "999",
        "x-edination-message-standard": "X12",
        "x-edination-message-version": "005010X231A1"
      }

      "ST": {
        "required": [
          "TransactionSetControlNumber_02",
          "TransactionSetIdentifierCode_01"
        ],
        "type": "object",
        "properties": {
          "TransactionSetIdentifierCode_01": {
            "maxLength": 3,
            "minLength": 3,
            "type": "string",
            "format": "X12_AN",
            "x-edination-element-id": "143"
          },
          "TransactionSetControlNumber_02": {
            "maxLength": 9,
            "minLength": 4,
            "type": "string",
            "format": "X12_AN",
            "x-edination-element-id": "329"
          },
          "ImplementationConventionPreference_03": {
            "maxLength": 35,
            "minLength": 1,
            "type": "string",
            "format": "X12_AN",
            "x-edination-element-id": "1705"
          }
        },
        "x-edination-segment-id": "ST"
      },        

      "Loop_2000": {
        "type": "object",
        "properties": {
          "AK2": {
            "$ref": "#/components/schemas/AK2"
          },
          "Loop_2100": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Loop_2100"
            }
          },
          "IK5": {
            "$ref": "#/components/schemas/IK5"
          }
        },
        "x-edination-loop-id": "2000"
      },

'''      