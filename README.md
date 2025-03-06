# KRA-Image-Extractor
KRA-Image-Extractor is a Python script that automatically extracts mergedimage.png from .kra (Krita project) files and saves them as thumbnails. This is useful for quickly generating previews without opening Krita or for recovering your latest saved work if you forget to export.


## 🔹 Features

✅ **Batch Processing** – Scans all .kra files in the folder where the script is run.
✅ **Automated Thumbnail Extraction** – Saves _mergedimage.png_ as a PNG thumbnail alongside the original file.
✅ **Error Handling** – Detects missing _mergedimage.png_ files and invalid ZIP archives.
✅ **Customizable Output** – Modify the script to adjust thumbnail size or format with Pillow.


## 🔹 How It Works

1. The script scans the current folder for .kra files.
2. If a .kra file is found, it extracts _mergedimage.png_.
3. The image is saved as "[filename] thumbnail.png" in the same folder.
4. ⚠️ If a file with the same name already exists, it will be overwritten.
5. Any errors (e.g., missing files, corrupt ZIP archives) are handled gracefully.


## 🔹 Usage

_Requirements_
- Python 3.x
- Pillow (pip install pillow)


_Running the Script_

1. Place the script in the folder containing your **.kra** files.
2. Run the script in a terminal or command prompt:
   ``` bash
   python kra_image_extractor.py
   ```
2. Alternatively, you can double-click on the script to run it. 
3. The script will generate PNG thumbnails alongside your .kra files.


## 🔹 Important Notes

⚠️ The script will overwrite existing thumbnail files with the same name.
⚠️ Thumbnails are saved in the same folder as the original .kra files.
⚠️ If you need custom thumbnail sizes, modify the Pillow processing step.
⚠️ Always test on backup copies before running on important files.

## 🔹 Resources  

For more details on **mergedimage.png** and the **.kra** file format, check out the Krita documentation:  
🔗 [Krita File Format Documentation](https://docs.krita.org/en/general_concepts/file_formats/file_kra.html)  


## 🔹 Credits  

This script was developed with the assistance of **Gemini AI** as a foundation.  
I reviewed, modified, and tested the code to ensure it works as intended,  
tailoring it to meet the needs of artists who forget to export their work.  
