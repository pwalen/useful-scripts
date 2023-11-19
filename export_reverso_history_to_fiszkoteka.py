# The text to be processed
input_text = """

"""


def transform_text(input_text):
    # Split the input text into lines
    lines = input_text.split('\n')
    # Initialize an empty list to store the output text
    output_text = []
    # Initialize a list to group words together
    current_group = []

    for line in lines:
        # Check for 'en pl' or date line to end the current group
        if 'en pl' in line or '/' in line:
            # Process the current group if it is not empty
            if current_group:
                # Format the group into the desired string format and add to output
                if len(current_group) > 1:
                    output_text.append(f"{current_group[0]}, {' | '.join(current_group[1:])}")
                else:
                    output_text.append(current_group[0])
                # Reset the current group for the next set of words
                current_group = []
        else:
            # Add non-empty lines to the current group
            if line.strip():
                current_group.append(line.strip())

    # Add the last group if it exists
    if current_group:
        if len(current_group) > 1:
            output_text.append(f"{current_group[0]}, {' | '.join(current_group[1:])}")
        else:
            output_text.append(current_group[0])

    # Join all the formatted strings into a single text block
    return '\n'.join(output_text)


# Process the text
transformed_text = transform_text(input_text)
print(transformed_text)
