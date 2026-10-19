"""Submit and poll a FLUX 3 Klein generation or edit task through Muapi."""

import os
import sys
import time

import requests


API_BASE = "https://api.muapi.ai/api/v1"
API_KEY = os.environ["MUAPI_API_KEY"]
HEADERS = {"x-api-key": API_KEY, "Content-Type": "application/json"}


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "generate"
    if mode == "edit":
        endpoint = "flux-3-klein-edit-image"
        payload = {
            "prompt": "Replace the plain background with a warm studio setting, preserving the product shape.",
            "images_list": ["https://example.com/product.jpg"],
            "resolution": "2K",
            "aspect_ratio": "auto",
            "num_images": 1,
        }
    else:
        endpoint = "flux-3-klein-text-to-image"
        payload = {
            "prompt": "A sculptural glass perfume bottle on a warm limestone plinth, soft editorial light.",
            "resolution": "2K",
            "aspect_ratio": "4:3",
            "num_images": 2,
        }

    submitted = requests.post(f"{API_BASE}/{endpoint}", headers=HEADERS, json=payload, timeout=60)
    submitted.raise_for_status()
    request_id = submitted.json()["request_id"]
    print(f"Submitted {endpoint}: {request_id}")

    while True:
        response = requests.get(
            f"{API_BASE}/predictions/{request_id}/result",
            headers={"x-api-key": API_KEY},
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
        status = result.get("status")
        if status == "completed":
            print("Image URLs:", result.get("outputs", []))
            return
        if status == "failed":
            raise RuntimeError(result.get("error", "Image generation failed"))
        time.sleep(2)


if __name__ == "__main__":
    main()
