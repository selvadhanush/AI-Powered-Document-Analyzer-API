from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import PyPDF2

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Document Text Extractor API"}

@app.post("/extract-text/")
async def extract_text(file: UploadFile = File(...)):
    # Only allow txt and pdf
    if file.filename.endswith(".txt"):
        content = await file.read()
        text = content.decode("utf-8")
    elif file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file.file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    else:
        return JSONResponse(content={"error": "Unsupported file type"}, status_code=400)
    
    return {"filename": file.filename, "text": text}
