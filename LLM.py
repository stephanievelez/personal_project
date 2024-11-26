import google.generativeai as genai
from IPython.display import Markdown
from UserSecret import secret
import chromadb
#from chromadb import Documents, EmbeddingFunction, Embeddings
from google.api_core import retry

chroma_client = chromadb.Client()

GOOGLE_API_KEY = secret()["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
    if "embedContent" in m.supported_generation_methods:
        print(m.name)
documents = ["CYP2C19Rec.json", "gene_drug_pair", "CYP2C19"]

class GeminiEmbeddingFunction(EmbeddingFunction):
    # Specify whether to generate embeddings for documents, or queries
    document_mode = True

    def __call__(self, input: Documents) -> Embeddings:
        if self.document_mode:
            embedding_task = "retrieval_document"
        else:
            embedding_task = "retrieval_query"

        retry_policy = {"retry": retry.Retry(predicate=retry.if_transient_error)}

        response = genai.embed_content(
            model="models/text-embedding-004",
            content=input,
            task_type=embedding_task,
            request_options=retry_policy,
        )
        return response["embedding"]