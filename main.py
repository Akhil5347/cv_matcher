path = r"C://Users//91939//OneDrive//Desktop//assignment//data//data//ACCOUNTANT//10554236.pdf"
#Using PyPDF2
#importing required modules
import PyPDF2
from PyPDF2 import PdfReader
import re
pdf_reader = PdfReader(path)

# Initialize an empty string to store the extracted text
extracted_text = ''

# Iterate through each page in the PDF
for page in pdf_reader.pages:
    # Extract text from the current page
    extracted_text += page.extract_text()

# Print or process the extracted text
# print(extracted_text)

# # Print or process the extracted text
# print(extracted_text)
def extract_key_details(text):
    category_pattern = r"Category: (.*?)\n"
    skills_pattern = r"Skills: (.*?)\n"
    education_pattern = r"Education: (.*?)\n"

    category_match = re.search(category_pattern, text)
    skills_match = re.search(skills_pattern, text)
    education_match = re.search(education_pattern, text)

    category = category_match.group(1).strip() if category_match else None
    skills = skills_match.group(1).strip() if skills_match else None
    education = education_match.group(1).strip() if education_match else None

    return {
        "Category": category,
        "Skills": skills,
        "Education": education
    }

# Open the PDF file in read-binary mode
with open(path, 'rb') as pdf_file:
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize an empty string to store the extracted text
    extracted_text = ''

    # Iterate through each page in the PDF
    for page in pdf_reader.pages:
        # Extract text from the current page
        extracted_text += page.extract_text()
# Extract key details from the text
key_details = extract_key_details(extracted_text)

def extract_education(text):
    education_list = []

    # Define regular expression patterns to match degree and institution
    degree_pattern = r"(?i)(?:Bachelor(?:'s)?|Master(?:'s)?|Ph\.?D\.?|M\.?B\.?A\.?)(?:\s+[A-Za-z\.,]*)?"
    institution_pattern = r"((?<=\n)|(?<=\t)|(?<=\s))([A-Z][A-Za-z\s&,'()0-9]*[A-Za-z0-9])\s*((?=\n)|(?=\t)|(?=\s)|(?=,)|(?=$))"
    
    # Find all matches of degree and institution patterns in the text
    degree_matches = re.finditer(degree_pattern, text)
    institution_matches = re.finditer(institution_pattern, text)

    # Iterate through matches and combine degree and institution
    for degree_match, institution_match in zip(degree_matches, institution_matches):
        degree = degree_match.group().strip()
        institution = institution_match.group().strip()
        education_list.append({"Degree": degree, "Institution": institution})
    
    return education_list

# Example usage:

education_info = extract_education(extracted_text)
print(education_info)
# Print the extracted key details
print("Category:", key_details["Category"])
print("Skills:", key_details["Skills"])
print("Education:", key_details["Education"])




