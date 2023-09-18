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
1. `Pyresparser`- A Python library for parsing and extracting information from resumes (CVs). It's a powerful tool designed to efficiently extract essential details from resumes, including:<br>

Candidate's name<br>
Contact information<br>
Skills<br>
Work experience<br>
Educational background<br>
In some cases, Pyresparser may not extract education details as accurately as required. To address this limitation, we've included custom code to concurrently extract education details in the desired format.

2. `SentenceTransformer` - A versatile Python library that allows you to obtain embeddings for sentences or entire documents. It leverages pre-trained models to represent text data as dense vectors. One of the models I've used is `paraphrase-MiniLM-L6-v2`, which is particularly effective for various natural language processing tasks.







