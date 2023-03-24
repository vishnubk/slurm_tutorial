from PIL import Image, ImageFilter
import sys
import os
import time
from joblib import Parallel, delayed

def process_image(image_path, output_path):
    with Image.open(image_path) as img:
        img = img.filter(ImageFilter.BLUR)
        img.save(os.path.join(output_path, os.path.basename(image_path)))
    time.sleep(30)

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]
    image_files = [os.path.join(input_dir, f) for f in os.listdir(input_dir) if os.path.isfile(os.path.join(input_dir, f))]

    num_cores = os.cpu_count()
    
    # Execute the code in parallel
    Parallel(n_jobs=num_cores)(delayed(process_image)(image_path, output_dir) for image_path in image_files)

    # Uncomment the following lines to execute the code in serial
    # for image_path in image_files:
    #     process_image(image_path, output_dir)

