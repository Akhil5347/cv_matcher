# cv_matcher
## Description about files:
. `data-list of resumes downloaded from Kaggle resume dataset`.
2. `parsed_resumes` - Extracted JSON data from CV PDFs using pyPDF2 and pyreparser.<br>
3. `job_description_records` - Extracted JSON data of job descriptions from the Huggingface dataset (as prescribed).<br>
4. `res.py` - A Python script to extract details like skills and experience from PDFs.<br>
5. `data_gather.py` - A Python script used to obtain 15 job descriptions from the Huggingface dataset.<br>
6. `parsed_resume.json` - A sample JSON file describing the extracted data from a single CV PDF.<br>
7. `Embedding_and_similarity.ipynb` - An IPython Notebook file used for tokenizing, performing embeddings on the obtained JSON files, and calculating cosine similarities.<br>
