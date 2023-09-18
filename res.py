from pyresparser import ResumeParser
import json
import os
import PyPDF2
from PyPDF2 import PdfReader
import re

# Path to the folder containing resume files
li=["BPO","BANKING","AVIATION","AUTOMOBILE","ARTS","APPAREL","AGRICULTIRE","ADVOCATE","ACCOUNTANT","CHEF","CONSTRUCTION","CONSULTANT","DESIGNER","DIGITAL-MEDIA","FINANCE","FITNESS","HEALTHCARE","HR","PUBLIC-RELATIONS","SALES","TEACHER"]
for i in li:
    resume_folder = "/data//data//"+i

    # Define the output folder for JSON files
    output_folder = "parsed_resumes"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    #Function to extract education details 
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
    # Iterate through each resume file in the folder
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):  # Assuming resume files are in PDF format
            resume_path = os.path.join(resume_folder, filename)
            pdf_reader = PdfReader(resume_path)
            extracted_text = ''

    # Iterate through each page in the PDF
            for page in pdf_reader.pages:
                # Extract text from the current page
                extracted_text += page.extract_text()
            

            
            # Parse the resume and extract data
            data = ResumeParser(resume_path).get_extracted_data()
            education_info = extract_education(extracted_text)
            
            # Add education information to the data
            data["education"] = education_info
            
            # Perform data processing (similar to your existing code)
            if "name" in data:
                data["category"] = data.pop("name")
            if "category" in data and "Summary" in data["category"].lower():
                data["category"] = data["category"].replace("Summary", "")
            columns_to_remove = ["college_name", "degree", "designation", "email", "mobile_number", "no_of_pages"]
            for column in columns_to_remove:
                if column in data:
                    data.pop(column)
            
            # Define the JSON file path within the output folder
            json_filename = os.path.splitext(filename)[0] + ".json"
            json_file_path = os.path.join(output_folder, json_filename)
            
            # Convert the data to JSON and save it
            json_data = json.dumps(data, indent=4)
            with open(json_file_path, "w") as json_file:
                json_file.write(json_data)
            
            print(f"Resume data from '{filename}' saved to '{json_file_path}'")
