import zipfile
import os
import shutil

def extract_images_from_office_file(filepath, output_dir, prefix):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        with zipfile.ZipFile(filepath, 'r') as z:
            # Look for images in the standard media folders for Office documents
            media_files = [f for f in z.namelist() if f.startswith('word/media/') or f.startswith('xl/media/')]
            
            print(f"Found {len(media_files)} images in {filepath}")
            
            for file in media_files:
                # Extract the file
                filename = os.path.basename(file)
                # Create a new name to avoid collisions and identify source
                new_filename = f"{prefix}_{filename}"
                target_path = os.path.join(output_dir, new_filename)
                
                with z.open(file) as source, open(target_path, "wb") as target:
                    shutil.copyfileobj(source, target)
                print(f"Extracted: {new_filename}")
                
    except zipfile.BadZipFile:
        print(f"Error: {filepath} is not a valid zip/office file.")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Define source files
excel_file = 'DOC-20251029-WA0305..xlsx'
word_file = 'LISTADO DE REPUESTO DE EQUIPOS DEL AREA ESTSTICA.docx'
output_directory = 'images'

# Clean and recreate output directory
if os.path.exists(output_directory):
    shutil.rmtree(output_directory)
os.makedirs(output_directory)

# Extract
print("Extracting from Excel...")
extract_images_from_office_file(excel_file, output_directory, "excel")

print("\nExtracting from Word...")
extract_images_from_office_file(word_file, output_directory, "word")

print("\nDone.")