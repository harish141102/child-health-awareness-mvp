import os

def analyze_image(image_path):
    """
    Analyzes the uploaded image and returns a simple risk result.
    This is MVP logic and can later be replaced with full Azure AI.
    """

    if not os.path.exists(image_path):
        raise ValueError("Image file not found")

    # 🔹 MVP logic (dummy but valid for demo)
    # Later you can replace this with Azure AI Vision code
    result = {
        "message": "Image analyzed successfully",
        "note": "This is early awareness, not diagnosis",
        "risk_level": "Medium",
        "status": "success"
    }

    return result
