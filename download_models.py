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
        
        # 1. Open the zip file in memory
        with zipfile.ZipFile(io.BytesIO(response.content)) as z:
            print("📦 Analyzing ZIP contents...")
            
            # 2. Iterate through every file in the ZIP
            for file_info in z.infolist():
                filename = os.path.basename(file_info.filename)
                if not filename: continue # Skip directories
                
                # 3. Rules for where each file goes
                dest_path = None
                
                # Rule A: Helmet Detection models
                if filename in ['yolov5-obj_2400.weights', 'yolov5-obj.cfg', 'obj.names', 'yolov5-scooter.cfg']:
                    dest_path = os.path.join("Helmet", "Models", filename)
                
                # Rule B: Everything else goes to the main models folder
                else:
                    dest_path = os.path.join("models", filename)

                # 4. Extract and Move
                if dest_path:
                    # Create directory if it doesn't exist
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    
                    # Extract the file
                    with z.open(file_info) as source, open(dest_path, "wb") as target:
                        shutil.copyfileobj(source, target)
                        print(f"✔️ Extracted: {filename} -> {dest_path}")

        print("✨ All models and helmet weights are now in their correct locations!")
    except Exception as e:
        print(f"❌ Failed to download or extract models: {e}")
        print("Please ensure the ZIP_URL is correct and publicly accessible.")

if __name__ == "__main__":
    download_and_extract()
