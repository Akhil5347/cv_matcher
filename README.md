# cv_matcher
## Description about files:
data/data-list of resumes downloaded from kaggle resume dataset
parsed_resumes- extracted json data from cv pdf's using pyPDF2 and pyreparser.
job_description_records- extracted json data of job descriptions from Huggingface dataset(prescribed).
res.py-python script to extract the details like skills, experience from pdfs.
data_gather.py- python script to obtain 15 jobdescriptions from huggingface dataset.
parsed_resume.json- sample json file describing about extraccted data of a single cv pdf.
Embedding_and_similarity.ipynb- ipynb file that used for Tokenizing and performing embeddings on the json files obtained and the cosine similarities too.

