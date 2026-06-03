import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# Cargar la API Key del archivo .env
load_dotenv()

# Configuración de rutas relativas para tu estructura
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__)) # /backend/ai_service/
BACKEND_DIR = os.path.dirname(CURRENT_DIR)               # /backend/
PROJECT_ROOT = os.path.dirname(BACKEND_DIR)              # Raíz del repo

# Ubicación de tus TXTs y dónde se guardará la base de datos
DOCS_DIR = os.path.join(PROJECT_ROOT, "frontend", "doc")
DB_DIR = os.path.join(CURRENT_DIR, "vector_db")

def build_vector_db():
    print("Iniciando la construcción de la base de datos vectorial...")
    
    # 1. Cargar tus documentos
    archivos = ["mesainformacion.txt", "representante.txt"]
    documentos = []
    
    for archivo in archivos:
        ruta_archivo = os.path.join(DOCS_DIR, archivo)
        if os.path.exists(ruta_archivo):
            print(f"Cargando {archivo}...")
            loader = TextLoader(ruta_archivo, encoding='utf-8')
            documentos.extend(loader.load())
        else:
            print(f"Advertencia: No se encontró {archivo} en {ruta_archivo}")

    if not documentos:
        print("No se cargó ningún documento. Verifica las rutas.")
        return

    # 2. Dividir el texto en fragmentos solapados para dar buen contexto
    print("Dividiendo documentos en fragmentos...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"Se crearon {len(chunks)} fragmentos de texto.")

    # 3. Convertir a vectores (Embeddings) y guardar localmente
    print("Generando vectores con Google Gemini...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
    
    Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=DB_DIR
    )
    
    print(f"¡Éxito! Base de datos guardada en: {DB_DIR}")

if __name__ == "__main__":
    build_vector_db()