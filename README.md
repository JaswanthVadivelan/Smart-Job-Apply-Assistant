💼 Smart Job Apply Assistant

An AI-powered application that automates job applications by extracting information from job posters and resumes to generate professional application emails.

🎯 Features

📸 OCR Technology: Extracts text from job poster images

📧 Email Detection: Automatically finds HR email addresses

🎓 Resume Parsing: Extracts your name and skills from PDF resumes

✍️ Professional Email Generation: Creates polished application emails

✏️ Direct Editing: Edit the email manually

↩️ Undo/Reset: Revert changes anytime

📋 Easy Copy: One-click copy and download options

🚀 Fast Processing: Get results in seconds

🛠️ Installation
Prerequisites

Python 3.8 or higher

Tesseract OCR - Required for image text extraction

Installing Tesseract OCR

Windows:

Download from: https://github.com/UB-Mannheim/tesseract/wiki

Install and add to PATH

Default location:

C:\Program Files\Tesseract-OCR\tesseract.exe


Mac:

brew install tesseract


Linux:

sudo apt-get install tesseract-ocr

Setup Steps (Without Docker)

Clone or download this repository

cd Smart_Job_Apply


Create a virtual environment (recommended)

python -m venv venv


Activate virtual environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies

pip install -r requirements.txt


Configure Tesseract path (if needed)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


Run the application

streamlit run app.py

🐳 Docker Setup (Recommended)

You can run the entire app using Docker without worrying about dependencies.

1. Build Docker Image
docker build -t smart-job-apply .

2. Run Docker Container
docker run -p 8501:8501 smart-job-apply


Then open your browser and go to:

http://localhost:8501

3. Optional: Mount Local Folder (for development)
docker run -p 8501:8501 -v .:/app smart-job-apply

Example Dockerfile (already included)
# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install system dependencies for Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr libtesseract-dev && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

📁 Project Structure
Smart_Job_Apply/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── Dockerfile             # For containerized setup
├── README.md              # Project documentation
└── .gitignore             # Git ignore file

🔧 How It Works

Image Processing – Uses Tesseract OCR to extract text from job posters

Email Extraction – Regex identifies HR email addresses

Role Detection – Keyword matching finds job titles

Resume Parsing – PDFPlumber extracts name and skills

Email Generation – Predefined templates create professional emails

Output Display – Shows extracted info and final email

📝 Example Output

Extracted Information:

Name: Jaswanth Vadivelan

Job Role: Software Developer

HR Email: hr@techfirm.com

Generated Email:

Subject: Application for Software Developer Role

Dear Hiring Manager,

I am writing to express my interest in the Software Developer position at your organization. My name is Jaswanth Vadivelan, and I have experience and skills in Python, Java, and Machine Learning.

I am confident that my background and enthusiasm make me a strong candidate for this role. Please find my resume attached for your review.

Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team.

Best regards,
Jaswanth Vadivelan

🚨 Troubleshooting
Common Issues

1. Tesseract not found error

Ensure Tesseract is installed and added to PATH

Or manually set the path in app.py

2. Poor OCR results

Use clear, high-quality images

Avoid blurry or low-resolution posters

3. No email detected

Verify that the poster includes an email address

Add manually if not detected

🌟 Future Enhancements

 Multi-language support (Hindi, Tamil, etc.)

 Tone selector (Formal, Casual, Internship)

 Direct email sending via SMTP

 Batch job poster processing

 Custom email templates

 Resume summary generation

📄 License

This project is open source and available for educational purposes.

Made with ❤️ to help students land their dream jobs!