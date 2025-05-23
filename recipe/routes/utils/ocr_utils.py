from dotenv import dotenv_values
from google import genai
from google.genai import types
from pathlib import Path
import cv2

class Gemini:
    def __init__(self, content):
        self.content = content

    def execute(self):
        if not self.initialize_gemini():
            return {"error": "Could not initialize Gemini"}
        self.run_gemini()
        return self.response.text

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
        with open(instructions_path, 'r', encoding='utf-8') as file:
            if not file:
                print("error: Could not find gemini_system_instructions.txt")
                return None
            else : 
                system_instructions=file.read()
                return system_instructions

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
            model="gemini-2.0-flash",
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
        # self.show_steps()  # (for development only)
        return self.resized

        # Aplly Canny edge filter (currently unused)
    def canny_edge(self):
        self.canny = cv2.Canny(self.img, 100, 200, apertureSize=3, L2gradient=True)

        # Gray scale image to facilitate reading
    def gray_scale(self):
        self.gray_scale_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)

    def bilateral_filter(self):
        self.bi_filtered = cv2.bilateralFilter(self.gray_scale_img, 9, 75, 75)

    def equalize_contrast(self):
        self.equalized = cv2.equalizeHist(self.bi_filtered)

        # Apply thresholding to enhance optimized contrast in black and white
    def thresholding(self):
        # _, self.thresh = cv2.threshold(self.equalized, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        self.thresh = cv2.adaptiveThreshold(
            self.equalized, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )

        # Reescale the image to make it easier to read
    def resize(self):
        self.resized = cv2.resize(self.thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

        # Pop up windows with desired steps (used for development only)
    def show_steps(self):
        cv2.namedWindow("Thresholding", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Thresholding", 800, 600)
        cv2.imshow("Thresholding", self.thresh)

        cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Original Image", 800, 600)
        cv2.imshow("Original Image", self.img)

        cv2.waitKey(0)  # Wait key press to close windows
        cv2.destroyAllWindows()


        