class DictUtil:
    @classmethod 
    def get_dict_value(cls, dictionary, key):
        """
        A utility method for finding the value of the first occurence
        of a given key in a given nested dictionary.

        :param dictionary: The nested dictionary
        :type dictionary: dict
        :param key: The key to find
        :type key: str
        :return: The value of the first occurence of key
        :rtype: str or None
        """
        for k, v in dictionary.items():
            if k == key:
                return v
            elif type(v) is dict:
                val = cls.get_dict_value(v, key)
                if val is not None:
                    return val

    @classmethod 
    def get_dict_containing(cls, dictionary, key):
        """
        A utility method for finding the first occurence of
        a dictionary that contains a given key

        :param dictionary: The nested dictionary
        :type dictionary: dict
        :param key: The key to find
        :type key: str
        :return: The dictionary containing the key
        :rtype: dict or None
        """
        for k, v in dictionary.items():
            if k == key:
                return dictionary
            elif type(v) is dict:
                val = cls.get_dict_containing(v, key)
                if val is not None:
                    return val

    @classmethod
    def get_value_by_reference_path(cls, dictionary, path):
        """
        Finds a value for a given reference path where the path
        is in the form of #/key1/key2/leaf_key where # is the
        root of the dictionary and subsequent values, separated by /,
        are sub keys. 

        This is useful for not only picking out individual values but also
        in cases where the dictionary itself references other values. OpenAPI,
        for example, defines nested schemas that comprise a specification.

        eg: "$ref": "#/components/schemas/ST"

        This utility can help 'walk down' those schemas.

        :return: The value at the provided path
        :rtype: dict, str, or None
        """
        temp = dictionary
        path_parts = path.split("/")

        # walk down the path and return the last
        # TODO: error checking
        try:
            for path_part in path_parts:
                if path_part == "#":
                    continue
                else:
                    if path_part.isnumeric():
                        # as of python 3.7 the keys are ordered :)
                        # get a list of keys so that index can be used
                        temp = temp[list(temp.keys())[int(path_part)]]
                    else:
                        temp = temp[path_part]
        except KeyError:
            return None 

        return temp 