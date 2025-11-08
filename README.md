# 💼 Smart Job Apply Assistant

An AI-powered application that automates job applications by extracting information from job posters and resumes to generate professional application emails.

## 🎯 Features

- **📸 OCR Technology**: Extracts text from job poster images
- **📧 Email Detection**: Automatically finds HR email addresses
- **🎓 Resume Parsing**: Extracts your name and skills from PDF resumes
- **✍️ Professional Email Generation**: Creates polished application emails
- **💬 Interactive Chat**: Refine your email through natural conversation
- **✏️ Direct Editing**: Edit the email manually or use chat
- **↩️ Undo/Reset**: Revert changes anytime
- **📋 Easy Copy**: One-click copy and download options
- **🚀 Fast Processing**: Get results in seconds

## 🛠️ Installation

### Prerequisites

1. **Python 3.8 or higher**
2. **Tesseract OCR** - Required for image text extraction

#### Installing Tesseract OCR

**Windows:**
1. Download from: https://github.com/UB-Mannheim/tesseract/wiki
2. Install and add to PATH
3. Default location: `C:\Program Files\Tesseract-OCR\tesseract.exe`

**Mac:**
```bash
brew install tesseract
```

**Linux:**
```bash
sudo apt-get install tesseract-ocr
```

### Setup Steps

1. **Clone or download this repository**
```bash
cd Smart_Job_Apply
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv
```

3. **Activate virtual environment**

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Configure Tesseract path (if needed)**

If Tesseract is not in your PATH, add this line to `app.py` after imports:
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 🚀 Usage

1. **Start the application**
```bash
streamlit run app.py
```

2. **Open your browser** - The app will automatically open at `http://localhost:8501`

3. **Upload files**:
   - Upload a job poster image (JPG, PNG, JPEG)
   - Upload your resume (PDF)

4. **Generate email**:
   - Click "Generate Application Email"
   - Wait for AI processing
   - Copy the generated email

5. **Refine with chat (optional)**:
   - Use the chat feature to modify the email
   - Try: "Make it more formal" or "Add my internship experience"
   - Edit directly in the text area if preferred
   - Use Undo/Reset buttons as needed

6. **Send your application**:
   - Copy the final email content
   - Paste into Gmail/Outlook
   - Attach your resume
   - Send to the extracted HR email

## 📁 Project Structure

```
Smart_Job_Apply/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore            # Git ignore file
```

## 🔧 How It Works

1. **Image Processing**: Uses Tesseract OCR to extract text from job posters
2. **Email Extraction**: Regex patterns identify HR email addresses
3. **Role Detection**: Keyword matching finds job titles
4. **Resume Parsing**: PDFPlumber extracts name and skills from resume
5. **Email Generation**: Professional templates create polished application emails
6. **Output Display**: Shows extracted info and generated email with copy options

## ✍️ Email Generation

The application uses **professional email templates** for generating job applications:
- Instant generation (no AI model loading)
- Consistent, professional output
- Customizable and reliable
- Works offline

## 💬 Interactive Chat Feature

**NEW!** Refine your email through natural conversation:

### What You Can Ask:
- **"Make it more formal"** - Removes contractions, adds professional language
- **"Make it shorter"** - Creates a concise version
- **"Make it enthusiastic"** - Adds excitement and positive energy
- **"Add my internship experience"** - Mentions internships
- **"Make it longer"** - Adds more detail and context
- **Custom requests** - Add any specific content you want

### Features:
- ✏️ **Direct editing** in text area
- ↩️ **Undo** to previous versions
- 🔄 **Reset** to original email
- 🗑️ **Clear chat** history
- 📥 **Download** final version

See [CHAT_FEATURE_GUIDE.md](CHAT_FEATURE_GUIDE.md) for detailed examples!

## 📝 Example Output

**Extracted Information:**
- Name: Jaswanth Vadivelan
- Job Role: Software Developer
- HR Email: hr@techfirm.com

**Generated Email:**
```
Subject: Application for Software Developer Role

Dear Hiring Manager,

I am writing to express my interest in the Software Developer position at your organization. My name is Jaswanth Vadivelan, and I have experience and skills in Python, Java, Machine Learning.

I am confident that my background and enthusiasm make me a strong candidate for this role. Please find my resume attached for your review.

Thank you for considering my application. I look forward to the opportunity to discuss how I can contribute to your team.

Best regards,
Jaswanth Vadivelan
```

## 🚨 Troubleshooting

### Common Issues

**1. Tesseract not found error**
- Ensure Tesseract is installed
- Add Tesseract to system PATH
- Or set path manually in `app.py`

**2. App starts slowly**
- First run may take a moment to load dependencies
- Subsequent runs will be faster
- Streamlit caches resources automatically

**3. Poor OCR results**
- Use high-quality, clear images
- Ensure good contrast and lighting
- Avoid blurry or low-resolution posters

**4. No email detected**
- Verify the poster contains an email
- Check if email is clearly visible
- Manually add email if needed

## 🌟 Future Enhancements

- [ ] Multi-language support (Hindi, Tamil, etc.)
- [ ] Tone selector (Formal, Casual, Internship)
- [ ] Direct email sending via SMTP
- [ ] Batch processing for multiple jobs
- [ ] Custom email templates
- [ ] Resume summary generation

## 📄 License

This project is open source and available for educational purposes.

## 👨‍💻 Developer

Created as a solution to help students streamline their job application process.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📞 Support

If you encounter any issues or have questions, please create an issue in the repository.

---

**Made with ❤️ to help students land their dream jobs!**
