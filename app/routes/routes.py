from fastapi import File, UploadFile
from app import app
import logging
from app.controllers.generate_report import handle_pdf_parse
import asyncio
logger = logging.getLogger(__name__)  # get a logger instance

@app.get("/server-check")
def read_root():
    logger.info("Server check endpoint accessed")
    return {
        "status": "ok", 
        "service": "Pdf-Parser",
        "version": "1.0.0",
        "last-update": "25-03-2025",
        "provider": "zoom-polyAI-intg"
    }


@app.post("/parse_pdf")
async def parse_pdf(file: UploadFile = File(...)):
    pdf_content = await file.read()
    report_data = await handle_pdf_parse(pdf_content)
    return report_data