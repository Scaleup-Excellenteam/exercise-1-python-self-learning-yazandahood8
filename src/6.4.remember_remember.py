from PIL import Image

def decode_message(image_path):
    # Open the image
    img = Image.open(image_path)
    pixels = img.load()
    
    width, height = img.size
    message = []
    
    # Iterate over each column in the image
    for x in range(width):
        # Search for the black pixel in each column
        for y in range(height):
            if pixels[x, y] == (0, 0, 0):  # If the pixel is black
                # Convert the row number to a character and add it to the message
                message.append(chr(y))
                break
    
    # Return the decoded message
    return ''.join(message)


if __name__ == "__main__":
    image_path = "path"  
    decoded_message = decode_message(image_path)
    print("Decoded message:", decoded_message)