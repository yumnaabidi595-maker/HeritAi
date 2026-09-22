from PIL import Image


def get_image_info(image: Image.Image):
    """
    Returns basic information about an uploaded image.
    """

    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
    }