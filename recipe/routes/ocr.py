from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
import pytesseract
import recipe.routes.utils.ocr_utils as ocr
# pip install fastapi python-multipart numpy opencv-python pytesseract
# also download tesseract v5.5.0.20241111

router = APIRouter(
   prefix="/ocr",
   tags=["OCR"]
)

# Endpoint to run OCR receiving target image as POST method
@router.post("/run-ocr/")
async def run_ocr(file: UploadFile = File(...)):
    try:
        # Read file
      file_contents = await file.read()

        # Convert to NumPy array then cv2 format
      np_array = np.frombuffer(file_contents, np.uint8)
      image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
      
      if image is None:
        return {"error": "Image not found"}

      process_image = ocr.Enhance(image)  # Initialize class with target image
      processed_image = process_image.execute()  # Run execute function

        # Extract and return OCR result
      extracted_text = pytesseract.image_to_string(processed_image,
                                                    lang='por',
                                                    config='--oem 3 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
                                                  )
      
      # cut_text = extracted_text.split('\n')[0]  # Fetch only first line
      # print(cut_text.strip())  # For development only
      # process_image.show_steps()  # Show desired steps from image enhancing process (development only)

      return [extracted_text.strip()]
    
    except Exception as err:
       return {"error": f"File upload failed: {str(err)}"}
    