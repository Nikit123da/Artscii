import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

# 1. Your 1-20 ASCII density dictionary
ascii_dict: dict[int, str] = {
    20: " ",
    19: "`",
    18: "'",
    17: ".",
    16: ",",
    15: "-",
    14: "~",
    13: ":",
    12: ";",
    11: "!",
    10: "+",
    9: "=",
    8: "*",
    7: "o",
    6: "x",
    5: "X",
    4: "%",
    3: "&",
    2: "#",
    1: "@",
}

img_path = "./simple-black-and-white-owl-illustration-perched-on-branch-minimalist-isolated-against-white-background-vector.jpg"

# 2. Load original image and get dimensions
orig_img = cv2.imread(img_path)
height, width, _ = orig_img.shape
gray_img = cv2.cvtColor(orig_img, cv2.COLOR_BGR2GRAY)

# 3. Choose character font size & setup grid
FONT_SIZE = 12
# Load a monospaced font so characters align evenly
try:
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
except OSError:
    font = ImageFont.load_default()

# Get dimensions of a single character box
bbox = font.getbbox("A")
char_w = bbox[2] - bbox[0]
char_h = bbox[3] - bbox[1]

# Avoid division by zero if font bounding box is invalid
char_w = max(char_w, 6)
char_h = max(char_h, 12)

# 4. Create a blank image with original dimensions
ascii_canvas = Image.new("RGB", (width, height), color="white")
draw = ImageDraw.Draw(ascii_canvas)

# 5. Process image grid and draw characters
for y in range(0, height, int(char_h)):
    for x in range(0, width, int(char_w)):

        # Extract pixel cell corresponding to character box
        cell = gray_img[y : y + char_h, x : x + char_w]
        if cell.size == 0:
            continue

        # Calculate brightness and map to 1-20 key
        avg_brightness = cell.mean()
        dict_key = int((avg_brightness / 255) * 19) + 1
        char = ascii_dict[dict_key]

        # Draw ASCII character on canvas (using black text)
        draw.text((x, y), char, fill="black", font=font)

# 6. Save the output image with identical dimensions
ascii_canvas.save("ascii_owl_output.jpg")
print(f"Saved image with dimensions: {ascii_canvas.size} (Width x Height)")




