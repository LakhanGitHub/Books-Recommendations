from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings


# Step 1: Load and split the text
loader = TextLoader("tagged_description.txt", encoding='utf-8')
raw_documents = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=0, chunk_overlap=0, separator='\n')
documents = text_splitter.split_documents(raw_documents)

# Step 2: Use Hugging Face Embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"  # You can use other models like 'sentence-transformers/all-MiniLM-L12-v2'
)

# Step 3: Create Chroma vector store
db_books = Chroma.from_documents(documents, embedding=embedding_model)

query = 'A book to teach childer about nature'

docs = db_books.similarity_search(query,k=10)