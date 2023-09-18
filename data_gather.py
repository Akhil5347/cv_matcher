from datasets import load_dataset
import random
import json
# Load the dataset
dataset = load_dataset("jacob-hugging-face/job-descriptions")

# Define the number of job descriptions to extract (e.g., 10-15)
num_descriptions_to_extract = random.randint(10, 15)

# Get a random subset of job descriptions
random_indices = random.sample(range(len(dataset["train"])), num_descriptions_to_extract)
random_job_descriptions = [dataset["train"][idx] for idx in random_indices]
job_data=[]
output_directory = "job_description_records"

# Create the directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)
# Print and comprehend the job descriptions
for i, job_description in enumerate(random_job_descriptions):
    title = job_description["position_title"]
    description = job_description["job_description"]
    resp=job_description['model_response']
    try:
        parsed_response = json.loads(resp)
    except json.JSONDecodeError:
        parsed_response = {}

    # Extract individual columns
    core_responsibilities = parsed_response.get("Core Responsibilities", "")
    required_skills = parsed_response.get("Required Skills", "")
    educational_requirements = parsed_response.get("Educational Requirements", "")
    experience_level = parsed_response.get("Experience Level", "")
    preferred_qualifications = parsed_response.get("Preferred Qualifications", "")
    compensation_and_benefits = parsed_response.get("Compensation and Benefits", "")

    job_data.append({
        "Job Title": title,
        "Job Description": description,
        "Core Responsibilities": core_responsibilities,
        "Required Skills": required_skills,
        "Educational Requirements": educational_requirements,
        "Experience Level": experience_level,
        "Preferred Qualifications": preferred_qualifications,
        "Compensation and Benefits": compensation_and_benefits})

    # Define the filename for this job description
    json_file_path = os.path.join(output_directory, f"job_description_{i + 1}.json")

    # Save the job data to a separate JSON file
    with open(json_file_path, "w") as json_file:
        json.dump(job_data, json_file, indent=4)
    job_data.pop()
    print(f"Job Description {i + 1} saved to {json_file_path}")