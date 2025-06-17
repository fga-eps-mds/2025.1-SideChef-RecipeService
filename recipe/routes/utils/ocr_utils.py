from dotenv import dotenv_values
from google import genai
from google.genai import types
from pathlib import Path
from typing import List
from ..filters_routes import all_ingredients
import pytesseract
import cv2
import shutil

# -- Independent functions --

    # Extract and return OCR result
def run_ocr(image):
    custom_config = '--oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    output = pytesseract.image_to_string(image, lang='por', config=custom_config)
    return output

    # Filter recipes through gemini response and return compatible recipes
def filter_recipes(extracted_texts: List[str]):
    ingredients = []

    for item in extracted_texts:
        item = item.lower()

        ingredients.append(item)

    recipes = all_ingredients(ingredients)

    return recipes


# -- Classes --

class Gemini:
    def __init__(self, content):
        self.content = content

    def execute(self):
        if not self.initialize_gemini():
            return {"error": "Could not initialize Gemini"}
        self.run_gemini()
        if self.response and hasattr(self.response, 'text') and self.response.text is not None:
            return self.response.text
        return {"error": "Gemini execution returned invalid response"}

        # Returns .env file's values
    def get_dotenv(self):
        dotenv_path = Path(__file__).parent.parent.parent.parent / ".env"  # Gets script relative path to the .env file
        if not dotenv_path.exists():
            print("error: Could not find .env file")
            return None
        else: return dotenv_values(dotenv_path)

        # Returns string with gemini's system instructions from gemini_system_instructions.txt
    def get_system_instructions(self):
        instructions_path = Path(__file__).parent / "gemini_system_instructions.txt"  # Gets script relative path
        try:
            with open(instructions_path, 'r', encoding='utf-8') as file:
                system_instructions=file.read()
                return system_instructions
        except:
            print("error: Could not find gemini_system_instructions.txt")
            return None

        # Setup gemini 
    def initialize_gemini(self):
        dotenv = self.get_dotenv()
        if not dotenv:
            return False
        api_key = dotenv.get("GEMINI_API_KEY")
        if not api_key:
            return False
        
        try:
            self.client = genai.Client(api_key=api_key)
            return True
        except:
            return False

        # Configure and Run gemini model
    def run_gemini(self):
        system_instructions = self.get_system_instructions()
        self.response = self.client.models.generate_content(
            model="gemini-2.0-flash",  # Only runs up to 15 requests per minute (RPM)
            config=types.GenerateContentConfig(
                system_instruction=system_instructions
            ),
            contents=self.content
        )

class Enhance:

    def __init__(self, img):
        self.img = img

    def execute(self):
        # self.canny_edge()
        self.gray_scale()
        self.bilateral_filter()
        self.equalize_contrast()
        self.thresholding()
        self.resize()
        return self.resized

        # Aplly Canny edge filter (currently unused)
    def canny_edge(self):
        self.canny = cv2.Canny(self.img, 100, 200, apertureSize=3, L2gradient=True)

        # Gray scale image to facilitate reading
    def gray_scale(self):
        self.gray_scale_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

        # Apply bilateral filtering to diminish the difference between areas with similar colors
    def bilateral_filter(self):
        self.bi_filtered = cv2.bilateralFilter(self.gray_scale_img, 9, 75, 75)

        # Equalize contrast to avoid either too bright or too dark areas
    def equalize_contrast(self):
        self.equalized = cv2.equalizeHist(self.bi_filtered)

        # Apply thresholding to enhance optimized contrast in black and white
    def thresholding(self):
        self.thresh = cv2.adaptiveThreshold(
            self.equalized, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )

        # Reescale the image to make it easier to read
    def resize(self):
        self.resized = cv2.resize(self.thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Invert image to read products with dark background
    def invert_image(self):
        self.inverted_image = cv2.bitwise_not(self.resized)
        return self.inverted_image

        # Saves images from desired steps (used for development only)
    def store_process_images(self):
        try:
            folder = Path(__file__).parent / "ocr_image_logs"

            if folder.exists():
                shutil.rmtree(folder)  # Deletes folder and its content
            
              # Creates new empty folder
            folder.mkdir(parents=True, exist_ok=True)

              # Writes every desired step into the folder
            cv2.imwrite(str(folder / "original_img.png"), self.img)
            cv2.imwrite(str(folder / "thresholding.png"), self.thresh)
            cv2.imwrite(str(folder / "equalized.png"), self.equalized)
            if self.inverted_image is not None:
                cv2.imwrite(str(folder / "inverted_img.png"), self.inverted_image)
            
        
        except Exception as err:
            return {"error": f"Image log folder preparation failed: {str(err)}"}
