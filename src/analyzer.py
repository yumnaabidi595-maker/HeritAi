def analyze_result(result):
    """
    Converts the detector output into a simple
    preliminary condition assessment.
    """

    edge_strength = result["edge_strength"]
    contrast = result["contrast"]

    if edge_strength > 20 or contrast > 70:
        severity = "High"
        summary = (
            "The image shows significant visual irregularities. "
            "Further inspection is recommended."
        )

    elif edge_strength > 7 or contrast > 40:
        severity = "Moderate"
        summary = (
            "The image shows some surface irregularities "
            "that may require visual inspection."
        )

    else:
        severity = "Low"
        summary = (
            "No prominent visual irregularities were detected "
            "by the current prototype."
        )

    return {
        "severity": severity,
        "summary": summary
    }