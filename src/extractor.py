import os
import google.generativeai as genai
from PIL import Image

class VisionExtractor:
    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        
        # Updated to the model found in your list
        self.model_name = "models/gemini-2.0-flash" 
        self.model = genai.GenerativeModel(self.model_name)

    def extract_attributes(self, image_path):
        prompt = """
        Analyze this product image and extract the following details into a structured YAML format.
        
        Required Fields:
        - Brand Name
        - Size or Quantity
        - Detected Text
        - Dominant Colors
        - Packaging Type
        - Key Features

        OUTPUT FORMAT:
        Return ONLY valid YAML. Do not include markdown backticks.
        """

        try:
            # FIX FOR WINERROR 32: Open, load, and CLOSE the file properly
            with Image.open(image_path) as img:
                img.load()  # Force load data into memory
                
                # Send to API while file is open
                response = self.model.generate_content([prompt, img])
            
            # The file is now automatically closed here
            
            text_output = response.text.replace("```yaml", "").replace("```", "").strip()
            return text_output

        except Exception as e:
            print(f"Error during Gemini API call ({self.model_name}): {e}")
            return None