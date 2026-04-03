import os
import requests
import zipfile
import io

# The link to your combined models ZIP file
ZIP_URL = "https://github.com/PrekshithReddy/Real-Time-Traffic-Survelliance/releases/download/v1.0.0-weights/models.zip"
MODELS_DIR = "models"

def download_and_extract():
    if not os.path.exists(MODELS_DIR):
        os.makedirs(MODELS_DIR)
        print(f"📁 Created {MODELS_DIR} directory.")

    # Check if a specific large file already exists to skip download
    check_file = os.path.join(MODELS_DIR, "vgg_model.hdf5")
    if os.path.exists(check_file):
        print("✅ Models already exist in the folder. Skipping download.")
        return

    print("📥 Downloading models.zip from GitHub Releases...")
    try:
        response = requests.get(ZIP_URL, stream=True)
        response.raise_for_status()
        
        # Use io.BytesIO to extract directly from memory for efficiency
        print("📦 Extracting models...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall(MODELS_DIR)
        
        print("✨ All models downloaded and extracted successfully!")
    except Exception as e:
        print(f"❌ Failed to download or extract models: {e}")
        print("Please ensure the ZIP_URL is correct and publicly accessible.")

if __name__ == "__main__":
    download_and_extract()
