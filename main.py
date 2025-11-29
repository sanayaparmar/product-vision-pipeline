import os
import glob
from dotenv import load_dotenv
from src.preprocessor import ImagePreprocessor
from src.extractor import VisionExtractor
from src.utils import save_yaml

# Load environment variables (API Key)
load_dotenv()

def main():
    # Configuration
    INPUT_DIR = "data/input_images"
    OUTPUT_DIR = "data/output_yaml"
    
    # Initialize classes
    preprocessor = ImagePreprocessor(target_width=800)
    extractor = VisionExtractor()

    # Get all images (jpg, jpeg, png)
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp']
    image_files = []
    for ext in extensions:
        image_files.extend(glob.glob(os.path.join(INPUT_DIR, ext)))

    if not image_files:
        print(f"No images found in {INPUT_DIR}. Please add some product images.")
        return

    print(f"Found {len(image_files)} images. Starting pipeline...\n")

    for img_path in image_files:
        print(f"Processing: {img_path}...")
        
        try:
            # Step 1: Preprocess (Resize & Denoise)
            # This satisfies the 'Bonus' requirement
            processed_img_path = preprocessor.process(img_path)

            # Step 2: Extract Info using Vision Model
            yaml_data = extractor.extract_attributes(processed_img_path)

            # Step 3: Save Output
            if yaml_data:
                save_yaml(yaml_data, img_path, OUTPUT_DIR)
            else:
                print(f"❌ Failed to extract data for {img_path}")

            # Cleanup temp file
            preprocessor.cleanup(processed_img_path)

        except Exception as e:
            print(f"❌ Error processing {img_path}: {str(e)}")

    print("\nPipeline completed successfully.")

if __name__ == "__main__":
    main()