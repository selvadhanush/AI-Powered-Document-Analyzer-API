FastAPI Document Text Extractor API
Overview

FastAPI Document Text Extractor is a lightweight API built with FastAPI that allows users to upload text or PDF files and extract their contents as structured JSON. This project demonstrates basic backend API development, file handling, and asynchronous programming in Python, making it ideal for document processing and information extraction tasks.

Features

Upload and extract text from .txt and .pdf files.

FastAPI-based RESTful API with automatic interactive documentation via Swagger UI.

Asynchronous file handling for efficient processing.

Returns JSON responses containing file name and extracted text.

Basic error handling for unsupported file types.

Technologies Used

Python 3.x

FastAPI – Modern web framework for building APIs

Uvicorn – ASGI server for running FastAPI

PyPDF2 – Extract text from PDF documents

Python-Multipart – Handle file uploads

Git – Version control

Installation & Setup

Clone the repository

git clone https://github.com/your-username/fastapi-doc-extractor.git
cd fastapi-doc-extractor


Create a virtual environment

python -m venv venv
# Activate it:
# Windows
venv\Scripts\activate
# Linux / Mac
source venv/bin/activate


Install dependencies

pip install fastapi uvicorn python-multipart PyPDF2


Run the API

uvicorn main:app --reload


Visit http://127.0.0.1:8000/docs
 to test API via Swagger UI.

API Endpoints
1. GET / – Welcome Route

Description: Confirms API is running.

Response:

{
  "message": "Welcome to Document Text Extractor API"
}

2. POST /extract-text/ – Extract Text from File

Description: Upload a .txt or .pdf file to extract its text.

Request: Multipart file upload

Response:

{
  "filename": "example.pdf",
  "text": "Extracted text content from the file..."
}


Error Response: Unsupported file type

{
  "error": "Unsupported file type"
}

Project Structure
fastapi-doc-extractor/
├── main.py         
├── venv/                  
└── README.md

Future Enhancements

Support additional file formats (e.g., Word, HTML, Markdown).

Limit file size to improve performance.

Return text summaries or first N characters for large files.

Add authentication and logging for production use.

Author

Your Name

GitHub: https://github.com/selvadhanush

