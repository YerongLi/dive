import os
from PIL import Image

def crop_images_in_batch(input_folder, output_folder, crop_box):
    """
    Crop all images in a folder with the same bounding box and save them, 
    while printing their original dimensions.
    
    Args:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to save cropped images.
        crop_box (tuple): Bounding box to crop the images. Format: (x, y, width, height).
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        if not os.path.isfile(input_path):
            print(f"Skipping {filename}, not a valid file.")
            continue
        
        try:
            # Open the image
            with Image.open(input_path) as img:
                # Get the original size
                original_size = img.size  # (width, height)
                print(f"Processing {filename}: Original Size = {original_size}")
                
                # Crop the image
                x, y, w, h = crop_box
                cropped_img = img.crop((x, y, x + w, y + h))
                
                # Save the cropped image
                cropped_img.save(output_path)
                print(f"Saved cropped image: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Example usage
input_folder = "TET"  # Replace with your input folder path
output_folder = "cropTET"  # Replace with your output folder path
crop_box = (0, 180, 1400, 680)  # Specify the bounding box (x, y, width, height)

crop_images_in_batch(input_folder, output_folder, crop_box)
