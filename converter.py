import os
from PIL import Image

def convert_and_resize_images(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                img_path = os.path.join(root, filename)
                with Image.open(img_path) as img:
                    img = img.resize((1980, int(1980 * img.height / img.width)), Image.Resampling.LANCZOS)

                    new_filename = os.path.splitext(filename)[0] + '.webp'
                    new_img_path = os.path.join(root, new_filename)
                    img.save(new_img_path, 'webp')

                    print(f'Converted and resized {filename} to {new_filename}')


if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    if os.path.isdir(folder_path):
        convert_and_resize_images(folder_path)
    else:
        print("The provided path is not a valid directory.")
