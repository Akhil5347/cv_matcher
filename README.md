# cv_matcher
## Description about files:
1. `data/data`-list of resumes downloaded from Kaggle resume dataset.<br>
2. `parsed_resumes` - Extracted JSON data from CV PDFs using pyPDF2 and pyresparser.<br>
3. `job_description_records` - Extracted JSON data of job descriptions from the Huggingface dataset (as prescribed).<br>
4. `res.py` - A Python script to extract details like skills and experience from PDFs.<br>
5. `data_gather.py` - A Python script used to obtain 15 job descriptions from the Huggingface dataset.<br>
6. `parsed_resume.json` - A sample JSON file describing the extracted data from a single CV PDF.<br>
7. `Embedding_and_similarity.ipynb` - An IPython Notebook file used for tokenizing, performing embeddings on the obtained JSON files, and calculating cosine similarities.<be>
## Models and tools utilized:
1. `Pyresparser`- A Python library for parsing and extracting information from resumes (CVs). It can extract various details such as the candidate's name, contact information, skills, work experience, education.<br> Additionally, I added my code to extract education details concurrently since, the library coudn't extract the details required in a exact manner.<br>
2. `SentenceTransformer` - Python library to obtain embeddings for sentences or documents using pre-trained models. The pre trained model I used is `paraphrase-MiniLM-L6-v2`.


