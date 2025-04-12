def extract_json_data(json_string):
    # Remove curly braces, quotes, and whitespace
    clean_str = json_string.strip().strip('{}').strip()
    
    # Split by commas and process each key-value pair
    result = {}
    for item in clean_str.split(','):
        if ':' in item:
            key, value = item.split(':', 1)
            # Clean up key and value
            key = key.strip().strip('"\'')
            value = value.strip().strip('"\'')
            # Convert numeric values
            if value.isdigit():
                value = int(value)
            result[key] = value
    
    return result