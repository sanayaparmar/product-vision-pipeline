import cv2
import numpy as np
from PIL import Image
import os
import time

class ImagePreprocessor:
    def __init__(self, target_width=800):
        self.target_width = target_width

    def process(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        img = cv2.imread(image_path)
        if img is None:
            raise ValueError(f"Could not read image: {image_path}")

        h, w = img.shape[:2]
        scaling_factor = self.target_width / float(w)
        new_height = int(h * scaling_factor)
        img_resized = cv2.resize(img, (self.target_width, new_height), interpolation=cv2.INTER_AREA)

        img_denoised = cv2.fastNlMeansDenoisingColored(img_resized, None, 10, 10, 7, 21)
        img_rgb = cv2.cvtColor(img_denoised, cv2.COLOR_BGR2RGB)
        
        temp_filename = f"temp_processed_{os.path.basename(image_path)}"
        Image.fromarray(img_rgb).save(temp_filename)
        
        return temp_filename

    def cleanup(self, temp_path):
        """Removes the temporary file with retries."""
        if os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except PermissionError:
                time.sleep(1) # Wait 1 second
                try:
                    os.remove(temp_path)
                except:
                    pass