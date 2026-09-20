import cv2

CELL_SIZE = 4


#if the pixel is whiter then it'll have a higher level
ascii_dict: dict[int, str] = {
    10: " ",   # ~0% white pixel density (empty)
    9: "'",   # ~10% density
    8: ",",   # ~20% density
    7: "~",   # ~30% density
    6: ";",   # ~40% density
    5: "+",  # ~50% density
    4: "*",  # ~60% density
    3: "x",  # ~70% density
    2: "%",  # ~80% density
    1: "#",  # ~90% density
    0: "@",  # ~100% white pixel density (highest coverage)
}


def convert_to_grayscale(img_path): 
    image = cv2.imread(img_path)
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("grayscaled_img.jpg", gray_img)
    return gray_img

#brightness formula:
# 299R + 587G + 114B

# y*width + x
def main():
    img_path = "./lion.jpg"

    grayscale_img = convert_to_grayscale(img_path)
    
    ascii_file = open("./ascii_file", "w")

    height, width = grayscale_img.shape
    for col in range(0, height, CELL_SIZE):
        for row in range(0, width, CELL_SIZE):
            cell = grayscale_img[col : col +CELL_SIZE, row : row + CELL_SIZE]

            avg_brightness = cell.mean()
            dict_key = int((avg_brightness / 255) * 10) #converts the 255 to 10 format
            ascii_file.write(ascii_dict[dict_key])
        ascii_file.write("\n")

    ascii_file.close()


if __name__ == "__main__":
    main()





