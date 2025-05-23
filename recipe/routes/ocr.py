from fastapi import APIRouter, UploadFile, File
import numpy as np
import cv2
import recipe.routes.utils.ocr_utils as ocr
# pip install fastapi python-multipart numpy opencv-python pytesseract dotenv google-genai pathlib
# also download tesseract v5.5.0.20241111

# Router setup
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

    if product.strip() == "reading_failed":
      return [f"reading_failed: {str(extracted_text.strip())}"]  
    else: return [product.strip()]
  
  except Exception as err:
    return {"error": f"File upload failed: {str(err)}"}
  