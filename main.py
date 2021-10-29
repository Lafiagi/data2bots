import sys
import json
from json.decoder import JSONDecodeError
from constants import DATA_TYPES

def get_data(data_path: str) -> dict:
    '''
    Extracts JSON data and converts it to a dictionary
    the  returns the dictionary
    '''
    try:
        with open(data_path) as raw_json_data:
            try:
                python_data = json.load(raw_json_data)
                python_data = python_data.get('message', None)
            except JSONDecodeError:
                raise JSONDecodeError(
                    "The JSON file is not properly formatted", str(raw_json_data), 1)

    except FileNotFoundError:
        raise FileNotFoundError("Specified file was not found!")

    return python_data


def output_data(output_data_path: str, data: dict) -> bool:
    '''
    Takes path to the outputfile and a dictionary
    then dumps the dictionary into the output file
    '''
    try:
        with open(output_data_path, 'w+') as result:
            result.write(json.dumps(data))

    except Exception as e:
        raise(e)

    return True


def extract_schema(python_data: dict) -> dict:
    '''
    Extract the expected schema and returns a dictionary
    of the schema.
    '''
    counter = 1
    schema = {}

    for _, value in python_data.items():
        data_obj = {}
        val = DATA_TYPES.get(type(value))
        data_obj['type'] = val
        data_obj["tag"] = ""
        data_obj["description"] = ""
        data_obj["required"] = False
        schema['key_' + str(counter)] = data_obj
        counter += 1

    return schema


def main() -> None:
    if len(sys.argv) < 3:
        print("In and Out File arguments must be supplied!")
        return

    input_json = sys.argv[1]
    output_json = sys.argv[2]
    data = get_data(input_json)
    output_schema = extract_schema(data)
    is_successful = output_data(output_json, output_schema)
    message = '\nSuccessfully Extracted the schema!' if is_successful\
              else '\nFailed to Extract the schema. Error during outputing'

    print(message)


if __name__ == '__main__':
    main()
