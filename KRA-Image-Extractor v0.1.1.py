import os
import zipfile
from PIL import Image

print("Process started, please wait....") 
def extract_kra_thumbnails(folder_path):
    """
    Extracts mergedimage.png from .kra files and saves them as thumbnails.

    Args:
        folder_path (str): The path to the folder containing .kra files.
    """
    for filename in os.listdir(folder_path):
        if filename.endswith(".kra"):
            kra_filepath = os.path.join(folder_path, filename)
            thumbnail_filename = os.path.splitext(filename)[0] + " thumbnail.png"
            thumbnail_filepath = os.path.join(folder_path, thumbnail_filename)

            try:
                with zipfile.ZipFile(kra_filepath, 'r') as kra_zip:
                    with kra_zip.open('mergedimage.png') as merged_image_file:
                        img = Image.open(merged_image_file)
                        img.save(thumbnail_filepath)
                        print(f"Thumbnail created: {thumbnail_filename}")

            except FileNotFoundError:
                print(f"mergedimage.png not found in {filename}")
            except zipfile.BadZipFile:
                print(f"Error: {filename} is not a valid zip file")
            except Exception as e:
                print(f"An error occurred with {filename}: {e}")

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Run the thumbnail extraction
extract_kra_thumbnails(script_directory)

print("Batch processing complete.")

""" 
To-do
- Show the total number of thumbnails created, skipped or that had an error. 



Change log
v0.1    - Inital release (March 5, 2025)
v0.1.1  - Added "Process started, please wait...." clarification text.
        - Also added changelog and To-do

"""
