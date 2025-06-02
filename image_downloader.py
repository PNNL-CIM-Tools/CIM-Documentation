import os
import time
from cimgraph.utils import download_mermaid

def main():

    # Walk through the current directory and all subdirectories
    for root, dirs, files in os.walk('.'):
        # Loop through each subdirectory
        for dir_name in dirs:
            # Check if the subdirectory is named 'images'
            if dir_name == 'images':
                # Get the full path to the 'images' subdirectory
                images_dir = os.path.join(root, dir_name)
                print(f'downloading images from {images_dir}')
                # Loop through all files in the 'images' subdirectory
                for filename in os.listdir(images_dir):
                    # Check if the file has a .txt extension
                    if filename.endswith('.txt'):
                        # Get the full path to the .txt file
                        txt_file_path = os.path.join(images_dir, filename)
                        
                        # Open the .txt file in read mode
                        with open(txt_file_path, 'r') as file:
                            content = file.read()
                
                        destination = txt_file_path.replace('.txt', '.svg')
                        download_mermaid(content, destination)
                        print(f'downloaded diagram for {filename}')
                        time.sleep(5)

if __name__ == '__main__':
    main()


