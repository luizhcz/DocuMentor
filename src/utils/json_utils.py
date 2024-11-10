import json

class JsonUtils:
    
    @staticmethod
    def add_to_json(json_data):
        """
        Updates a JSON object with a new entry. Accepts a JSON string or a dictionary as input.

        :param json_data: JSON string or dictionary.
        :param new_obj: Dictionary with new data to be inserted into the JSON.
        :return: Updated JSON string or an error message.
        """
        try:
            # Check if the input is a string or a dictionary
            if isinstance(json_data, str):
                # Try to load the JSON
                data = JsonUtils._try_load_json(json_data)
            elif isinstance(json_data, dict):
                data = json_data
                
            # Convert back to a formatted JSON string
            updated_json = json.dumps(data, ensure_ascii=False, indent=4)

            return updated_json
        except Exception as e:
            return f"Error processing JSON: {e}"

    @staticmethod
    def is_json(obj):
        """
        Checks if the provided object is a valid JSON string.

        :param obj: Object to be validated.
        :return: True if it's a valid JSON string, False otherwise.
        """
        # First, try to directly parse the JSON to check its validity
        if JsonUtils._try_parse_json(obj):
            return True

        # If invalid, try replacing single quotes with double quotes
        if isinstance(obj, str):
            obj = obj.replace("'", '"')
            return JsonUtils._try_parse_json(obj)
        
        return False

    @staticmethod
    def _try_parse_json(obj):
        """
        Tries to parse the object as JSON, returning True if valid, False otherwise.

        :param obj: Object to be tested.
        :return: True if valid, False otherwise.
        """
        try:
            json.loads(obj)
            return True
        except (ValueError, TypeError):
            return False
        
    @staticmethod
    def _try_load_json(json_data):
        """
        Attempts to load a JSON string, and if it fails, replaces single quotes with double quotes and tries again.

        :param json_data: JSON string.
        :return: Python object (dictionary or list) if valid JSON, or None.
        """
        try:
            # First attempt to load the JSON
            return json.loads(json_data)
        except (ValueError, TypeError):
            try:
                json_data_fixed = json_data.replace("'", '"')
                return json.loads(json_data_fixed)
            except (ValueError, TypeError):
                return None