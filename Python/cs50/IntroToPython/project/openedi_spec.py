from dict_util import DictUtil

class OpenEDISpec:
    def __init__(self, spec):
        """
        A wrapper for a dictionary that is in the OpenEDI specification
        format.

        :param spec: A dictionary in the OpenEDI specification format.
        :type spec: dict
        """
        self._spec = spec

    def get_root_schema(self):
        return DictUtil.get_dict_containing(self._spec, "x-edination-message-id")

    @property
    def spec(self):
        return self._spec

    """
    The OpenAPI spec contains definitions of elements that comprise an EDI message. These
    definitions are individual schemas with one being designated as the root. OpenEDI tags
    the root with extension attributs that define the message type. A schema with
    x-edination-message-id designates it as the root.

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

    The properties of the schemas can either be references to other
    schemas or an element definition.

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

      "Loop_2110": {
        "type": "object",
        "properties": {
          "IK4": {
            "$ref": "#/components/schemas/IK4"
          },
          "CTX_Ele": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CTX_Ele"
            }
          }
        },
        "x-edination-loop-id": "2110"
      },      
    """
