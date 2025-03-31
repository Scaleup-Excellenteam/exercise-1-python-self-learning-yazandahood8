def extract_secret_messages(file_path):
    # List to store secret messages
    messages = []
    
    try:
        # Open the file in binary read mode
        with open(file_path, 'rb') as file:
            while chunk := file.read(1024):  # Read 1024 bytes at a time
                # Decode the binary chunk to a text string
                chunk_text = chunk.decode('utf-8', errors='ignore')
                
                # Split the text into words
                words = chunk_text.split()

                # Check each word for the conditions: length >= 5 and ends with '!'
                for word in words:
                    if len(word) >= 5 and word.endswith('!'):
                        # If conditions are met, add the word to messages
                        messages.append(word)
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None  # Return None if the file is not found
    
    return messages


if __name__ == "__main__":
    file_path = "secret_message_file.txt"  # Replace with the actual path to your file
    secret_messages = extract_secret_messages(file_path)
    
    if secret_messages:
        print("Secret messages found:", secret_messages)
    else:
        print("No secret messages found.")