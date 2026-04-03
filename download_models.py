import os
import requests
import zipfile
import io
import shutil

# The link to your combined models ZIP file (Make sure it's the updated one!)
ZIP_URL = "https://github.com/PrekshithReddy/Real-Time-Traffic-Survelliance/releases/download/v1.0.0-weights/models.zip"

def download_and_extract():
    # If a specific large file already exists to skip download
    check_file = os.path.join("models", "vgg_model.hdf5")
    if os.path.exists(check_file):
        print("✅ Models already exist. Skipping download.")
        return

    print("📥 Downloading models.zip from GitHub Releases...")
    try:
        response = requests.get(ZIP_URL, stream=True)
        response.raise_for_status()
        
        # Extract everything into a temporary folder first
        print("📦 Extracting all models...")
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            z.extractall("tmp_models")
            
        print("📁 Moving models to correct folders...")
        
        # Move files from tmp_models/models/ to /models/
        if not os.path.exists("models"):
            os.makedirs("models")
        for item in os.listdir("tmp_models/models"):
            shutil.move(os.path.join("tmp_models/models", item), os.path.join("models", item))
            
        # Move files from tmp_models/Models/ to /Helmet/Models/
        if not os.path.exists("Helmet/Models"):
            os.makedirs("Helmet/Models")
        for item in os.listdir("tmp_models/Models"):
            shutil.move(os.path.join("tmp_models/Models", item), os.path.join("Helmet/Models", item))

        # Cleanup
        shutil.rmtree("tmp_models")
        
        print("✨ All models and helmet weights downloaded and extracted successfully!")
    except Exception as e:
        print(f"❌ Failed to download or extract models: {e}")
        print("Please ensure the ZIP_URL is correct and publicly accessible.")

if __name__ == "__main__":
    download_and_extract()
