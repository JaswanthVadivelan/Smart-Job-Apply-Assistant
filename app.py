import streamlit as st
import pytesseract
from PIL import Image
import pdfplumber
import re
import io
import os

# Configure Tesseract path for Windows
# If Tesseract is installed in a different location, update this path
if os.name == 'nt':  # Windows
    # Try multiple possible Tesseract locations
    possible_paths = [
        r'F:\Tesseract\tesseract.exe',
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Users\ASUS\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
    ]
    
    for tesseract_path in possible_paths:
        if os.path.exists(tesseract_path):
            pytesseract.pytesseract.tesseract_cmd = tesseract_path
            break

# Configure page
st.set_page_config(
    page_title="Smart Job Apply Assistant",
    page_icon="💼",
    layout="wide"
)

def extract_text_from_image(image):
    """Extract text from uploaded job poster using OCR"""
    try:
        # Convert to PIL Image if needed
        if not isinstance(image, Image.Image):
            image = Image.open(image)
        
        # Perform OCR
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        st.error(f"Error extracting text from image: {e}")
        return ""

def extract_email_from_text(text):
    """Extract email address from text using regex"""
    # Regex pattern for email
    email_pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    emails = re.findall(email_pattern, text)
    
    if emails:
        return emails[0]  # Return first email found
    return None

def extract_job_role(text):
    """Extract job role/title from poster text"""
    # Common job keywords
    job_keywords = [
        'developer', 'engineer', 'intern', 'analyst', 'designer',
        'manager', 'consultant', 'specialist', 'associate', 'coordinator',
        'software', 'data', 'web', 'frontend', 'backend', 'fullstack',
        'machine learning', 'ai', 'devops', 'qa', 'tester'
    ]
    
    text_lower = text.lower()
    
    # Look for job titles in the text
    for keyword in job_keywords:
        if keyword in text_lower:
            # Try to extract the full job title (context around keyword)
            lines = text.split('\n')
            for line in lines:
                if keyword in line.lower() and len(line.strip()) < 100:
                    return line.strip()
    
    return "the position"

def extract_resume_info(pdf_file):
    """Extract name and skills from resume PDF"""
    try:
        name = ""
        skills = ""
        
        with pdfplumber.open(pdf_file) as pdf:
            # Extract text from first page
            first_page = pdf.pages[0]
            text = first_page.extract_text()
            
            if text:
                lines = text.split('\n')
                
                # Extract name (usually first non-empty line)
                for line in lines:
                    if line.strip() and len(line.strip()) > 2:
                        name = line.strip()
                        break
                
                # Extract skills section
                text_lower = text.lower()
                skill_indicators = ['skills', 'technical skills', 'expertise', 'technologies']
                
                for indicator in skill_indicators:
                    if indicator in text_lower:
                        # Find the section with skills
                        idx = text_lower.find(indicator)
                        skill_section = text[idx:idx+500]  # Get next 500 chars
                        
                        # Extract skills (usually comma-separated or line-separated)
                        skill_lines = skill_section.split('\n')[1:4]  # Get next 3 lines
                        skills = ', '.join([line.strip() for line in skill_lines if line.strip()])
                        break
        
        return name, skills
    except Exception as e:
        st.error(f"Error parsing resume: {e}")
        return "", ""

def generate_email(name, skills, job_role, hr_email):
    """Generate professional job application email"""
    
    # Clean up the job role (remove extra text)
    job_role_clean = job_role.split('\n')[0].strip()
    if len(job_role_clean) > 50:
        job_role_clean = "the position"
    
    # Clean up skills
    skills_clean = skills[:200] if skills else "relevant technical and professional skills"
    
    # Generate professional email using template
    email_template = f"""Subject: Application for {job_role_clean}

Dear Hiring Manager,

I am writing to express my interest in the {job_role_clean} at your esteemed organization. I came across your job posting and believe my skills and background align well with the requirements.

My name is {name}, and I have expertise in {skills_clean}. I am confident that my technical abilities and enthusiasm make me a strong candidate for this role.

I have attached my resume for your review, which provides detailed information about my qualifications and experience. I would welcome the opportunity to discuss how I can contribute to your team.

Thank you for considering my application. I look forward to hearing from you.

Best regards,
{name}"""
    
    return email_template

# Main App UI
def main():
    st.title("💼 Smart Job Apply Assistant")
    st.markdown("### Automate your job applications with AI")
    st.markdown("Upload a job poster and your resume to generate a professional application email instantly!")
    
    st.divider()
    
    # Create two columns for file uploads
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📄 Upload Job Poster")
        poster_file = st.file_uploader(
            "Upload the job poster image",
            type=['jpg', 'jpeg', 'png'],
            help="Upload a clear image of the job posting"
        )
        
        if poster_file:
            st.image(poster_file, caption="Uploaded Job Poster", use_column_width=True)
    
    with col2:
        st.subheader("📋 Upload Your Resume")
        resume_file = st.file_uploader(
            "Upload your resume (PDF)",
            type=['pdf'],
            help="Upload your latest resume in PDF format"
        )
        
        if resume_file:
            st.success("✅ Resume uploaded successfully!")
    
    st.divider()
    
    # Generate button
    if st.button("🚀 Generate Application Email", type="primary"):
        if not poster_file or not resume_file:
            st.error("⚠️ Please upload both job poster and resume!")
            return
        
        with st.spinner("🔍 Processing your files..."):
            # Step 1: Extract text from poster
            st.info("📸 Extracting text from job poster...")
            poster_text = extract_text_from_image(poster_file)
            
            if not poster_text.strip():
                st.error("❌ Could not extract text from poster. Please upload a clearer image.")
                return
            
            # Step 2: Extract HR email and job role
            st.info("📧 Detecting HR email and job role...")
            hr_email = extract_email_from_text(poster_text)
            job_role = extract_job_role(poster_text)
            
            # Step 3: Extract resume information
            st.info("📄 Parsing your resume...")
            name, skills = extract_resume_info(resume_file)
            
            if not name:
                name = "Applicant"
            if not skills:
                skills = "relevant technical skills"
            
            # Step 4: Generate email
            st.info("✍️ Generating professional email...")
            email_content = generate_email(name, skills, job_role, hr_email)
        
        # Display results
        st.success("✅ Email generated successfully!")
        st.divider()
        
        # Show extracted information
        st.subheader("📊 Extracted Information")
        info_col1, info_col2, info_col3 = st.columns(3)
        
        with info_col1:
            st.metric("Your Name", name)
        with info_col2:
            st.metric("Job Role", job_role)
        with info_col3:
            if hr_email:
                st.metric("HR Email", hr_email)
            else:
                st.warning("No email found in poster")
        
        st.divider()
        
        # Display generated email
        st.subheader("📧 Generated Application Email")
        
        if hr_email:
            st.info(f"**Send to:** {hr_email}")
        
        # Store email in session state for editing
        if 'current_email' not in st.session_state:
            st.session_state.current_email = email_content
        if 'email_history' not in st.session_state:
            st.session_state.email_history = [email_content]
        
        # Email content in editable text area
        edited_email = st.text_area(
            "Email Content",
            value=st.session_state.current_email,
            height=300,
            key="email_editor",
            help="Edit the email directly before copying or downloading"
        )
        
        # Update session state if manually edited
        if edited_email != st.session_state.current_email:
            st.session_state.current_email = edited_email
        
        # Copy button (using markdown with code block for easy copying)
        st.markdown("**Quick Copy:**")
        st.code(st.session_state.current_email, language=None)
        
        # Download option
        col_download, col_reset = st.columns([3, 1])
        with col_download:
            st.download_button(
                label="📥 Download Email as Text File",
                data=st.session_state.current_email,
                file_name=f"job_application_{job_role.replace(' ', '_')}.txt",
                mime="text/plain"
            )
        with col_reset:
            if st.button("🔄 Reset to Original"):
                st.session_state.current_email = st.session_state.email_history[0]
                st.rerun()
        
        # End of output section

if __name__ == "__main__":
    main()
