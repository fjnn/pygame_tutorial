
# !/usr/bin/env python3


from PIL import Image


def colored_image(image_path, saved_location):
    """
    Flip or mirror the image

    @param image_path: The path to the image to edit
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    width, height = image_obj.size
    print("width: {0}, height: {1}".format(width, height))
    # r, g, b, v = image_obj.getpixel((20, 48))
    # print("Red: {0}, Green: {1}, Blue: {2}, v: {3}".format(r, g, b, v))

    # Process every pixel
    for x in range(width):
        for y in range(height):
            r, g, b, v = image_obj.getpixel((x, y))
            if g == 127:
                print("Red: {0}, Green: {1}, Blue: {2}, v: {3}, pixel = x:{4}, y:{5}".format(r, g, b, v, x, y))
                image_obj.putpixel((x, y), (238, 0, 0, 255))
                image_obj.save(saved_location)
            elif g == 221:
                print("Red: {0}, Green: {1}, Blue: {2}, v: {3}, pixel = x:{4}, y:{5}".format(r, g, b, v, x, y))
                image_obj.putpixel((x, y), (208, 0, 150, 255))
                image_obj.save(saved_location)


if __name__ == '__main__':
    for i in range(18):
        image = 'skeleton-resizedWALK_' + str(i) + '.png'
        colored_image(image, 'skeleton-coloredWALK_' + str(i) + '.png')
        print(i)
