# 🚀 Quick Setup Guide - Smart Job Apply Assistant

## For Windows Users

### Step 1: Install Python
1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation:
```bash
python --version
```

### Step 2: Install Tesseract OCR
1. Download Tesseract installer from: https://github.com/UB-Mannheim/tesseract/wiki
2. Run the installer (recommended path: `C:\Program Files\Tesseract-OCR`)
3. Add to system PATH:
   - Search "Environment Variables" in Windows
   - Edit "Path" variable
   - Add: `C:\Program Files\Tesseract-OCR`
4. Verify installation:
```bash
tesseract --version
```

### Step 3: Setup Project
1. Open Command Prompt or PowerShell
2. Navigate to project folder:
```bash
cd C:\Users\ASUS\Downloads\Smart_Job_Apply
```

3. Create virtual environment:
```bash
python -m venv venv
```

4. Activate virtual environment:
```bash
venv\Scripts\activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## For Mac Users

### Step 1: Install Python
```bash
# Using Homebrew
brew install python@3.11
```

### Step 2: Install Tesseract
```bash
brew install tesseract
```

### Step 3: Setup Project
```bash
cd ~/Downloads/Smart_Job_Apply
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Run
```bash
streamlit run app.py
```

---

## For Linux Users

### Step 1: Install Dependencies
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip tesseract-ocr
```

### Step 2: Setup Project
```bash
cd ~/Downloads/Smart_Job_Apply
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 3: Run
```bash
streamlit run app.py
```

---

## 🐛 Troubleshooting

### Issue: "tesseract is not recognized"
**Solution**: 
- Ensure Tesseract is installed
- Add to PATH or modify `app.py`:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### Issue: "No module named 'streamlit'"
**Solution**:
- Ensure virtual environment is activated
- Run: `pip install -r requirements.txt`

### Issue: Model download takes too long
**Solution**:
- First run downloads ~500MB AI model
- Be patient, it's a one-time download
- Subsequent runs will be fast

### Issue: Poor text extraction from poster
**Solution**:
- Use high-quality, clear images
- Ensure good contrast
- Avoid blurry or low-resolution images

---

## 📝 Usage Tips

1. **Best Image Quality**: Use clear, high-resolution job posters
2. **Resume Format**: Keep resume simple and well-structured
3. **Email Verification**: Always verify the extracted HR email before sending
4. **Personalization**: Feel free to edit the generated email before sending
5. **Attach Resume**: Don't forget to attach your actual resume when sending

---

## 🌐 Deploy to Streamlit Cloud (Optional)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy!

**Note**: Add `packages.txt` file for Tesseract on Streamlit Cloud (already included)

---

## 📞 Need Help?

- Check the main README.md for detailed documentation
- Review PROJECT_DESIGN.md for technical details
- Create an issue on GitHub

---

**Happy Job Hunting! 🎯**
