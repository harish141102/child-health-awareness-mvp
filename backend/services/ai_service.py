from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
import os

def analyze_image(image_path):
    endpoint = os.getenv("AZURE_VISION_ENDPOINT")
    key = os.getenv("AZURE_VISION_KEY")

    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    with open(image_path, "rb") as img:
        result = client.analyze(
            image_data=img.read(),
            visual_features=[VisualFeatures.TAGS]
        )

    tags = result.tags  # ✅ FIXED HERE

    risk = "Low"
    if len(tags) > 5:
        risk = "Medium"
    if len(tags) > 10:
        risk = "High"

    return {
        "risk_level": risk,
        "tags_detected": len(tags)
    }
