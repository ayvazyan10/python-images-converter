import os
from PIL import Image


def convert_and_resize_images(folder_path):
    for root, _, files in os.walk(folder_path):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                img_path = os.path.join(root, filename)
                with Image.open(img_path) as img:
                    if img.width > 1920:
                        new_width = 1920
                        new_height = int(new_width * img.height / img.width)
                        img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                        print(f'Resized {filename} to 1920 width')
                    else:
                        print(f'Converted {filename} without resizing (width <= 1920)')

                    new_filename = os.path.splitext(filename)[0] + '.webp'
                    new_img_path = os.path.join(root, new_filename)
                    img.save(new_img_path, 'webp')

                    print(f'Saved {filename} as {new_filename}')


if __name__ == "__main__":
    folder_path = input("Enter the folder path: ").strip()
    if os.path.isdir(folder_path):
        convert_and_resize_images(folder_path)
    else:
        print("The provided path is not a valid directory.")


// for mysql ,snippet

UPDATE static_pages SET attributes = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(attributes, '.png', '.webp'), '.jpg', '.webp'), '.jpeg', '.webp'), '.bmp', '.webp'), '.tiff', '.webp')
WHERE attributes LIKE '%.png%' OR attributes LIKE '%.jpg%' OR attributes LIKE '%.jpeg%' OR attributes LIKE '%.bmp%' OR attributes LIKE '%.tiff%';
