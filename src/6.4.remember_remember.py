from PIL import Image
import os

def decode_message(image_path):
    # Check if path exists
    if not os.path.exists(image_path):
        print("Error: Image path does not exist.")
        return ""

    try:
        img = Image.open(image_path)
        pixels = img.load()
        width, height = img.size

        # Build message using list comprehension
        message = [
            chr(next(y for y in range(height) if pixels[x, y] == (0, 0, 0)))
            for x in range(width)
            if any(pixels[x, y] == (0, 0, 0) for y in range(height))
        ]

        return ''.join(message)

    except FileNotFoundError:
        print("Error: File not found.")
        return ""
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""

if __name__ == "__main__":
    image_path = input("Enter image path: ").strip()
    decoded_message = decode_message(image_path)
    if decoded_message:
        print("Decoded message:", decoded_message)
    else:
        print("No message could be decoded.")
