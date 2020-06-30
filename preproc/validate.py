from config_.input_schema import _args_bound, _args_type


class Validate:
    """Validate the input data for datatypes and range.
    """    
    def __init__(self):
        pass

    def _validate_args(self, data):
        """Vaildate if input arguments match the expected datatypes.

        Args:
            data (dict): input data to be validated

        Raises:
            ValueError: Raises value error in case when any of the
            input data does not match expected data type.
        """        
        for _key in _args_type.keys():
            if not isinstance(data[_key], _args_type[_key]):
                raise ValueError(
                    f"Expected {_key} to be of type {_args_type[_key]} but {type(data[_key])} found"
                )

    def _validate_bounds(self):
        pass
