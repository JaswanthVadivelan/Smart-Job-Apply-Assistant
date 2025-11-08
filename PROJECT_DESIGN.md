# 📘 PROJECT DESIGN DOCUMENT
## Smart Job Apply Assistant

---

## 1️⃣ PROJECT OVERVIEW

### Objective
To create an AI-powered application that helps students apply for jobs more efficiently by:
- Extracting job details and HR email from a hiring poster image
- Reading personal and skill information from the student's resume
- Automatically generating a professional, human-written job application email ready to paste into Gmail or Outlook

### Target Users
- Students seeking internships and entry-level positions
- Job seekers who apply to multiple positions regularly
- Anyone who wants to streamline the job application process

---

## 2️⃣ PROBLEM STATEMENT

### Current Challenges
Many students find job openings through digital posters on LinkedIn, WhatsApp, or Telegram. These posters contain important information like the job role and HR's email address, but students struggle to:

1. **Manually extract HR emails** from images
2. **Write proper professional emails** each time
3. **Repeatedly attach resumes** and draft similar messages
4. **Maintain consistency** in application quality

### Proposed Solution
The application automates this process so that the student only needs to:
1. Upload the poster (image)
2. Upload their resume (PDF)
3. Receive a ready-to-send email with all required details already filled in

---

## 3️⃣ FUNCTIONAL REQUIREMENTS

| Feature | Description |
|---------|-------------|
| **Poster Upload** | The user can upload a job poster image in `.jpg`, `.png`, or `.jpeg` format |
| **Resume Upload** | The user uploads a resume in `.pdf` format |
| **Text Extraction** | The system extracts all readable text from the uploaded poster |
| **Email Extraction** | The system detects and extracts the HR's email address using regex |
| **Job Role Detection** | The system identifies the job role keywords from the poster |
| **Resume Parsing** | The system extracts name, skills, and education from the uploaded resume |
| **Email Generation** | An AI model generates a professional, natural-sounding email |
| **Result Display** | The application displays the HR email and the full email text for copy |

---

## 4️⃣ NON-FUNCTIONAL REQUIREMENTS

| Requirement | Description |
|-------------|-------------|
| **Simplicity** | Easy-to-use interface with minimal input |
| **Speed** | Should generate output within 10 seconds |
| **Accuracy** | Must detect valid email addresses with high precision |
| **Human Tone** | Email content should sound human-written, not robotic |
| **Privacy** | Uploaded files are not stored permanently; they are processed temporarily |
| **Portability** | Should run easily on any system using Streamlit web interface |

---

## 5️⃣ SYSTEM ARCHITECTURE OVERVIEW

### Workflow Diagram (Textual Form)

```
┌─────────────────────────────────────────────────────────────┐
│                  User Interface (Frontend)                   │
│          Student uploads job poster and resume               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      OCR Module                              │
│     Reads text from the poster image using Tesseract OCR    │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│            Email & Role Extraction Module                    │
│   Uses Regular Expressions (regex) to find HR email and     │
│                      job title                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 Resume Parsing Module                        │
│   Reads resume text using a PDF reader and extracts         │
│                  name + skills                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│              AI Text Generation Module                       │
│   Combines extracted information into a structured prompt    │
│   Sends it to a Hugging Face text generation model to        │
│            create a professional email                       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                 Output Display Module                        │
│   Displays extracted HR email and generated email message    │
│       Provides a "Copy to Clipboard" button for easy use     │
└─────────────────────────────────────────────────────────────┘
```

---

## 6️⃣ DETAILED WORKING METHODOLOGY

### Step 1: Input Collection
- The user uploads two files:
  - `job_poster.jpg/png/jpeg`
  - `resume.pdf`
- The system verifies that both files are valid formats

### Step 2: Poster Text Extraction (OCR)
- The image is passed to **Tesseract OCR** to extract visible text
- Extracted text is stored temporarily in memory
- **Technology**: Pytesseract library

### Step 3: Information Extraction from Poster
Using **Regular Expressions**, the system identifies:
- **HR's email** (pattern: `[\w\.-]+@[\w\.-]+`)
- **Job title keywords** (examples: "Engineer", "Developer", "Intern")
- The extracted text is cleaned (remove unwanted symbols or URLs)

### Step 4: Resume Information Extraction
- The uploaded PDF is processed using **pdfplumber** or **PyMuPDF**
- From the first page or top section:
  - **Name** is extracted (usually first line)
  - **Skills** are extracted (search for keywords "Skills", "Technical Skills", etc.)
- The extracted data is formatted for use in the AI prompt

### Step 5: AI-Based Email Generation
A text prompt is constructed with placeholders filled in:

```
Write a short professional job application email for the position {role}.
My name is {name}. I am skilled in {skills}.
The email should be polite, human-like, and ready to send to HR.
```

The prompt is passed to a Hugging Face model such as:
- `google/flan-t5-base` (text2text)
- or `mistralai/Mistral-7B-Instruct-v0.2`

The model outputs a natural, coherent job application email.

### Step 6: Display Output
- The generated email is shown in a text area box
- The HR email is displayed above
- A "Copy Email" button allows the user to quickly copy the email content

### Step 7: (Optional) Multiple Job Posters
- Users can upload multiple posters to generate multiple emails automatically

---

## 7️⃣ IMPLEMENTATION INSTRUCTIONS

### 🧠 Tools to Use

| Category | Tool | Purpose |
|----------|------|---------|
| **Language** | Python | Main programming language |
| **Framework** | Streamlit | To create web UI |
| **OCR** | Pytesseract | To extract text from image |
| **Text Processing** | Regex | To detect email and keywords |
| **Resume Parsing** | pdfplumber | To read PDF content |
| **AI Model** | Hugging Face Transformers | For generating human-like email |
| **Hosting** | Streamlit Cloud / GitHub | To make it accessible online |

### ⚙️ Logical Steps to Implement

1. **Create Streamlit App**
   - Build UI with two upload boxes and one "Generate Email" button

2. **Implement OCR Module**
   - Convert uploaded poster image to text

3. **Extract HR Email + Role**
   - Use regex to find email
   - Detect job title using keyword search

4. **Parse Resume**
   - Extract name and skills from the first few lines of the resume

5. **Generate AI Email**
   - Combine all extracted data into a natural-language prompt
   - Send prompt to a Hugging Face text generation model

6. **Display Results**
   - Show HR email and generated email body
   - Add a button to copy the email

7. **(Optional)**
   - Store generated emails locally
   - Allow users to download the email in `.txt` format

---

## 8️⃣ OUTPUT EXAMPLE

### Extracted from Poster:
- **Role**: Software Developer
- **HR Email**: hr@techfirm.com

### Extracted from Resume:
- **Name**: Jaswanth Vadivelan
- **Skills**: Python, Java, Machine Learning

### Generated Email (Final Output):

```
Subject: Application for Software Developer Role

Dear Hiring Manager,

I came across your job posting for the Software Developer position. 
I'm Jaswanth Vadivelan, an AI & Data Science student skilled in Python and Java. 
Please find my resume attached for your review.

Thank you for your time and consideration.

Best regards,  
Jaswanth Vadivelan
```

---

## 9️⃣ DEPLOYMENT PLAN

### Steps to Deploy

1. **Create a GitHub repository** with:
   - `app.py`
   - `requirements.txt`
   - `README.md`

2. **Push code to GitHub**

3. **Deploy on Streamlit Cloud** using the repository link

4. **Test** using different job posters and resumes

5. **Share link** with students to use it as a free web tool

### Deployment Platforms

| Platform | Pros | Cons |
|----------|------|------|
| **Streamlit Cloud** | Free, easy setup, auto-updates | Limited resources |
| **Heroku** | Good for production | Requires configuration |
| **AWS/GCP** | Scalable | More complex, costs money |

---

## 🔟 FUTURE ENHANCEMENTS

| Feature | Description |
|---------|-------------|
| **Language Options** | Support for multiple languages (English, Hindi, Tamil) |
| **Tone Selector** | Choose between "Formal", "Casual", "Internship" tone |
| **Resume Summary** | Generate 2-line profile summary from resume |
| **Auto-Attach Resume** | Enable sending email directly from the app via SMTP |
| **AI Role Detection** | Train a custom classifier to detect job title from text more accurately |
| **Batch Processing** | Upload multiple posters and generate emails for all |
| **Email Templates** | Pre-built templates for different job types |
| **Analytics Dashboard** | Track applications sent and responses received |

---

## 📊 TECHNICAL SPECIFICATIONS

### Dependencies

```
streamlit==1.28.0
pytesseract==0.3.10
Pillow==10.1.0
pdfplumber==0.10.3
transformers==4.35.0
torch==2.1.0
```

### System Requirements

- **Python**: 3.8 or higher
- **RAM**: Minimum 4GB (8GB recommended for AI model)
- **Storage**: 2GB for model cache
- **Tesseract OCR**: Must be installed separately

### File Structure

```
Smart_Job_Apply/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Setup and usage instructions
├── PROJECT_DESIGN.md     # This document
├── .gitignore            # Git ignore file
└── venv/                 # Virtual environment (not in repo)
```

---

## 🔒 SECURITY & PRIVACY

### Data Handling
- Files are processed in-memory only
- No data is stored on servers
- Uploaded files are deleted after processing
- No external API calls (except Hugging Face model download)

### Best Practices
- Use HTTPS for deployment
- Don't log sensitive information
- Validate file types before processing
- Limit file sizes to prevent abuse

---

## 🧪 TESTING STRATEGY

### Test Cases

1. **Valid Inputs**
   - Clear job poster with visible email
   - Well-formatted PDF resume
   - Expected: Successful email generation

2. **Edge Cases**
   - Poster without email
   - Resume without skills section
   - Expected: Graceful fallback

3. **Invalid Inputs**
   - Non-image file as poster
   - Corrupted PDF
   - Expected: Error message

4. **Performance**
   - Large image files
   - Multi-page resumes
   - Expected: Complete within 10 seconds

---

## 📈 SUCCESS METRICS

- **Accuracy**: 90%+ email detection rate
- **Speed**: <10 seconds processing time
- **User Satisfaction**: Positive feedback on email quality
- **Adoption**: Number of students using the tool

---

## ✅ CONCLUSION

This project design document provides a complete blueprint for building the Smart Job Apply Assistant. Any AI tool or developer can follow this document to implement the application from scratch, understanding both the "what" and the "how" of the system.

The application solves a real problem faced by students and job seekers, making the job application process faster, easier, and more professional.

---

**Document Version**: 1.0  
**Last Updated**: November 2025  
**Status**: Ready for Implementation ✅
