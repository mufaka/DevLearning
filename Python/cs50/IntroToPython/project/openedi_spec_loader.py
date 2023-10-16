import json
import os
from dict_util import DictUtil 

class OpenEDISpecLoader:
    def __init__(self, root_path):
        """
        Encapsulates reading OpenEDI specifications and
        provides a mapping between the message type and standard
        to the file it is defined in.

        :param file_name: The root path to the OpenEDI specifications
        :type file_name: str
        """
        self.root_path = root_path
        self.message_map = self.get_message_file_map()

    def get_message_file_map(self):
        """
        Reads openedi rules files and returns a mapping between the
        message type and file.

        :return: A dictionary of file mappings
        :rtype: dict
        """
        message_map = {}
        files = os.listdir(self.root_path)

        for file_name in files:
            message_key = self.read_message_key(os.path.join(self.root_path, file_name))

            if message_key not in message_map.keys():
                message_map[message_key] = os.path.join(self.root_path, file_name)

        return message_map

    def read_openedi_message_def(self, file_name):
        """
        Reads the OpenEDI message definition from a file

        :param file_name: The path to the OpenEDI specification
        :type file_name: str
        :return: A dictionary containing the OpenEDI message definition
        :rtype: dict
        """
        with open(file_name, "r") as file:
            open_edi_def = json.load(file)
            file.close()

        return open_edi_def

    def read_openedi_message_by_key(self, message_key):
        """
        Reads the OpenEDI message definition using a message key

        :param message_key: The key to the path of the OpenEDI specification
        :type file_name: str
        :return: A dictionary containing the OpenEDI message definition
        :rtype: dict
        """
        # version is optional in the OpenEDI spec but always known in the 
        # EDI. OpenEDI only uses version when there are multiple implementatiosn
        # of the same message type (eg: 837P, 837I, 837D). Check for the versioned
        # key first and then the non versioned one to identify the message.
        if message_key not in self.message_map.keys():
            key_components = message_key.split(":")
            message_key = self.get_message_key(key_components[0], key_components[1], None)

        if message_key in self.message_map.keys():
            return self.read_openedi_message_def(self.message_map[message_key])
        else:
            raise ValueError(f"{message_key} not found. EDI version is not currently supported.")

    @classmethod
    def get_message_key(cls, message_type, standard, version):
        """
        A common function for determining a key to use
        for mapping a message type and standard. This is used
        for the initial loading of specifications and finding
        the appropriate specification for an edi file

        :param message_type: The type of message
        :type message_type: str
        :param standard: The standard of the message. eg: X12
        :type message_type: str
        :param standard: The optional version of the message. eg: 00501X222A1
        :type message_type: str
        :return: A dictionary containing the OpenEDI message definition
        :rtype: dict
        """
        return f"{message_type}:{standard}:{version}"


    def read_message_key(self, file_name):
        """
        Reads the message type and standard from the OpenEDI specfication
        and returns a formatted key string for use in referencing the file

        :return: A formatted key string to use when referencing the OpenEDI specification
        :rtype: str
        """
        open_edi_def = self.read_openedi_message_def(file_name)

        # looking for a key of x-edination-message-id and x-edination-message-standard
        message_type = DictUtil.get_dict_value(open_edi_def, "x-edination-message-id")
        standard = DictUtil.get_dict_value(open_edi_def, "x-edination-message-standard")
        version = DictUtil.get_dict_value(open_edi_def, "x-edination-message-version")

        return OpenEDISpecLoader.get_message_key(message_type, standard, version)
