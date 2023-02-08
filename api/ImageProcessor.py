from rembg import remove


# Create View
def remove_background(source_image_path, destination_image_path):
    try:
        print("Source: {}, Destination: {}".format(source_image_path, destination_image_path))
        with open(source_image_path, 'rb') as i, open(destination_image_path, 'wb') as o:
            # read source image in binary format
            input = i.read()
            # apply remove function to remove background
            output = remove(input)
            # save the new image in destination path
            o.write(output)
        print("Image background removed successfully")
    except Exception as e:
        print(f"There is problem while processed -> {e}")
