from PIL import Image
import numpy as np


def detect_faults(image: Image.Image):
    """
    HeritAI prototype visual fault detector.

    Uses image-processing techniques to identify
    possible crack-like edges and surface irregularities.
    """

    image = image.convert("L")
    image_array = np.array(image, dtype=np.float32)

    brightness = image_array.mean()
    contrast = image_array.std()

    # Detect strong pixel changes (edge-like regions)
    horizontal_change = np.abs(
        image_array[:, 1:] - image_array[:, :-1]
    )

    vertical_change = np.abs(
        image_array[1:, :] - image_array[:-1, :]
    )

    edge_strength = (
        horizontal_change.mean() + vertical_change.mean()
    ) / 2

    observations = []

    if edge_strength > 7:
        observations.append(
            "Possible crack-like or irregular edge patterns detected."
        )

    if contrast > 60:
        observations.append(
            "High surface variation detected."
        )

    if brightness < 70:
        observations.append(
            "Low-light or dark image conditions detected."
        )

    if brightness > 210:
        observations.append(
            "High exposure or bright image conditions detected."
        )

    if not observations:
        observations.append(
            "No prominent visual deterioration pattern detected by the prototype."
        )

    return {
        "observations": observations,
        "brightness": round(float(brightness), 2),
        "contrast": round(float(contrast), 2),
        "edge_strength": round(float(edge_strength), 2),
    }