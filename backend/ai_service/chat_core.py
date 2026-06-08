import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
# 1. Nueva importación oficial de Chroma para evitar el warning
from langchain_chroma import Chroma 
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

DB_DIR = os.path.join(os.path.dirname(__file__), "vector_db")

def get_maternal_chatbot_response(user_query: str) -> str:
    # 2. Obtenemos el modelo del archivo .env o usamos uno por defecto
    model_name = os.getenv('GEMINI_MODEL', 'gemini-1.5-flash')
    llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

    # 3. Conectar a la base de datos vectorial local
    vectorstore = Chroma(persist_directory=DB_DIR, embedding_function=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # 4. Crear el Prompt estricto (Personalidad e instrucciones)
    system_prompt = (
        "Eres un asistente virtual experto y empático de la Mesa Nacional de Maternidad y Nacimiento Seguros en Bolivia. "
        "Usa los siguientes fragmentos de contexto para responder a la pregunta. "
        "Si no sabes la respuesta o no está en el contexto, di claramente que no tienes esa información y sugiere contactar a un representante. "
        "NO inventes información. Sé conciso y claro.\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # 5. Construir la cadena RAG y ejecutar
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    response = rag_chain.invoke({"input": user_query})
    return response["answer"]