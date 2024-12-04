from datasets import load_dataset
from path_helper import get_absolute_path
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import CharacterTextSplitter

def test_split_text(data_files):
    """load a dataset and split the text for embedding. Returns a text object."""
    df = load_dataset(path = get_absolute_path(), data_files = data_files, split='train')
    df = df.to_pandas()
    df_loader = DataFrameLoader(df, page_content_column= "completion")
    df_document = df_loader.load()


    text_splitter = CharacterTextSplitter(chunk_size=1250,
                                      separator="\n",
                                      chunk_overlap=100)
    texts = text_splitter.split_documents(df_document)

    return texts
