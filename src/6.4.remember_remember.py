from PIL import Image
import os

def remember_remember(image_path):
    """
    Decodes a hidden message in a PNG image based on black pixel row indices.
    Returns the message, or None if the image can't be opened.
    """
    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        return None

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Failed to open image: {e}")
        return None

    pixels = img.load()
    width, height = img.size
    message = []

    for x in range(width):
        for y in range(height):
            if pixels[x, y][:3] == (0, 0, 0):  # Support for RGB or RGBA
                message.append(chr(y))
                break

    return ''.join(message)


if __name__ == "__main__":
    path = "src/code.png"
    decoded = remember_remember(path)
    if decoded:
        print("Decoded message:", decoded)
    else:
        print("No message decoded.")
