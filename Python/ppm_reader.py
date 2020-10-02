"""
Open an manipulate PPM images
    http://netpbm.sourceforge.net/doc/ppm.html

Gil Echeverria
25/09/2020
"""


def load_image(filename_in):
    """ Open an image file and store its contents in a matrix """
    image_data = []
    with open(filename_in) as file:
        # Read the image header
        magic_number = file.readline().strip()
        size = file.readline().split()
        max_value = int(file.readline())
        # Read the pixel data
        for line in file:
            row = line.split()
            for i in range(len(row)):
                row[i] = int(row[i])
            image_data.append(row)
    return image_data, max_value


def image_negative(image_data, max_value):
    """ Convert an image to its negative """
    for r, row in enumerate(image_data):
        for c, value in enumerate(row):
            image_data[r][c] = max_value - value


def write_image(image_data, max_value, filename_out):
    """ Write the contents of the matrix into a new file """
    with open(filename_out, "w") as file:
        # Write the header for the PPM
        file.write("P3\n")
        file.write(f"{len(image_data[0]) // 3} {len(image_data)}\n")
        file.write(f"{max_value}\n")
        # Write the contents of the data matrix
        for row in image_data:
            for value in row:
                file.write(f"{value:3} ")
            file.write("\n")


def print_image_data(image_data):
    """ Print information about the image """
    print(f"Image width: {len(image_data[0])//3}")
    print(f"Image height: {len(image_data)}")


def main():
    """ Program starting point """
    filename_in = "tester-a.ppm"
    filename_out = "tester-a-n.ppm"
    image_data, max_value = load_image(filename_in)
    print_image_data(image_data)
    image_negative(image_data, max_value)
    write_image(image_data, max_value, filename_out)
    

main()
