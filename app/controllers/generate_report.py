import io
import json

from PyPDF2 import PdfReader
from app.models.schema import ApiResponse
from app.utils import extract_json_data
from app.utils.openai import get_gemini


async def handle_pdf_parse(pdf_content):
    try:
        # Create a file-like object from the PDF content
        pdf_file = io.BytesIO(pdf_content)
        pdf_reader = PdfReader(pdf_file)
        
        full_text = ""
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            full_text += page.extract_text() + " "

        
        # If this is an async function, await it
        system_prompt = f"""
        Extract the following information from this property document text:
        1. Property Name
        2. Address
        3. Total Rentable Square Footage (as a number)

        Return the information in JSON format with the keys: property_name, address, total_rentable_sqft.
        If you cannot find certain information, use null for that value.

        Document text:
        {full_text}
        """
        extracted_text =get_gemini(system_prompt)
        print(extracted_text)
        extracted_data = json.loads(extracted_text[8:len(extracted_text)-3])
        

        property_data = {
            "property_name": extracted_data.get("property_name", None),
            "address": extracted_data.get("address", None),
            "total_rentable_sqft": extracted_data.get("total_rentable_sqft", None)
        }

        print(property_data)
        
        # # Return the response object directly (no await)
        return ApiResponse(
            status_code=200,
            message="Property information extracted successfully",
            data=property_data
        )

    except Exception as e:
        # Log the error and return a failure response
        print(f"An error occurred during PDF parsing: {e}")
        return ApiResponse(
            status_code=500,
            message=f"An error occurred during PDF parsing: {str(e)}",
            data=[]
        )