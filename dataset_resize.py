from PIL import Image
import os

# Function to rotate and resize images
def process_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the image
        image = Image.open(input_path)

        # Rotate the image 90° counter-clockwise
        # rotated_image = image.transpose(Image.ROTATE_270)

        # Resize the image (adjust the size as needed)
        new_size = (640, 640)  # New size: 640x640 pixels
        resized_image = image.resize(new_size)

        # Save the processed image
        resized_image.save(output_path)

if __name__ == "__main__":
    input_folder = "D:\Wallpaper\dataset"  # Update with the path to the folder containing the wrong images
    output_folder = "D:\Wallpaper\output_dataset"  # Update with the path to the folder where processed images will be saved

    process_images(input_folder, output_folder)
