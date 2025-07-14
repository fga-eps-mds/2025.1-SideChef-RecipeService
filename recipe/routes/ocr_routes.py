from fastapi import APIRouter, UploadFile, File
from typing import List
import numpy as np
import cv2
import recipe.routes.utils.ocr_utils as ocr
# pip install fastapi python-multipart numpy opencv-python pytesseract dotenv google-genai pathlib
# Also download tesseract v5.3.0

# Router setup
router = APIRouter(
   prefix="/ocr",
   tags=["OCR"]
)

# Endpoint to run OCR receiving target image as POST method
@router.post("/run-ocr/")
async def run_ocr(files: List[UploadFile] = File(...)):
  all_results = [] # Store every result, including error dictionaries. Might be usefull to deal with errors in the future
  identified_products = []  # Products that are successfully read by the OCR

  for file in files:
    try:
        # Read file
      file_contents = await file.read()

        # Convert to NumPy array then cv2 format
      np_array = np.frombuffer(file_contents, np.uint8)
      image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
      
      if image is None:
        all_results.append({"filename": file.filename, "error": "Image not found"})
        continue

      process_image = ocr.Enhance(image)  # Initialize class with target image
      processed_image = process_image.execute()  # Run execute function

      # Extract OCR output
      extracted_text = ocr.run_ocr(processed_image)

      # Send OCR's results to gemini and get response
      initialize_gemini = ocr.Gemini(extracted_text)
      product = initialize_gemini.execute()

      # Check if reading failed
      if product.strip() == "reading_failed":
        processed_image = process_image.invert_image()  # Try alternative image processing  
        
        extracted_text = ocr.run_ocr(processed_image)  # Re-run ocr

        initialize_gemini = ocr.Gemini(extracted_text)  # Initialize gemini again and send new OCR output
        product = initialize_gemini.execute()

      process_image.store_process_images()  # (for development only)

      if product.strip() == "reading_failed":
        all_results.append({"error": f"reading_failed: {str(extracted_text.strip())}"})  # Note: find a way to deal with errors on ocr_utils/filter_recipes or mobile side
      else: 
        all_results.append(product.strip())
        identified_products.append(product.strip())
    
    except Exception as err:
      all_results.append({"error": f"File upload failed: {str(err)}"})
      continue
  
  recipes = ocr.filter_recipes(identified_products)
  return recipes
