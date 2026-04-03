import os
import requests
import zipfile
import io
import shutil

# The link to your combined models ZIP file
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
            
        print("📁 Organizing models to correct folders...")
        
        # Helper to move files even if they're nested
        def move_contents(src_folder, dest_folder):
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            if not os.path.exists(src_folder):
                print(f"⚠️ Warning: Source {src_folder} not found in ZIP.")
                return
            for item in os.listdir(src_folder):
                s = os.path.join(src_folder, item)
                d = os.path.join(dest_folder, item)
                if os.path.isdir(s):
                    if os.path.exists(d): shutil.rmtree(d)
                    shutil.copytree(s, d)
                else:
                    shutil.move(s, d)

        # Now we match any possible zip structure:
        # 1. Main Models: Look for 'models' folder or just files in the root
        move_contents("tmp_models/models", "models")
        
        # 2. Helmet Models: Look for 'Models' folder
        move_contents("tmp_models/Models", "Helmet/Models")

        # Cleanup
        shutil.rmtree("tmp_models")
        
        print("✨ All models and helmet weights downloaded and extracted successfully!")
    except Exception as e:
        print(f"❌ Failed to download or extract models: {e}")
        print("Please ensure the ZIP_URL is correct and publicly accessible.")

if __name__ == "__main__":
    download_and_extract()
