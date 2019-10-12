#!/usr/bin/env python3

from PIL import Image


def flip_image(image_path, saved_location):
    """
    Flip or mirror the image

    @param image_path: The path to the image to edit
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    resized_image = image_obj.resize((80, 76))
    resized_image.save(saved_location)
    # rotated_image.show()


if __name__ == '__main__':
    for i in range(18):
        image = 'skeleton-DIE_' + str(i) + '.png'
        flip_image(image, 'skeleton-resizedDIE_' + str(i) + '.png')
        print(i)
