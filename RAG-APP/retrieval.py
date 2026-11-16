from aws import retriever


def retrieve_docs(question):
    return retriever.invoke(question)