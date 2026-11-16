import boto3
import streamlit as st
from botocore.config import Config
from langchain_aws import ChatBedrockConverse, AmazonKnowledgeBasesRetriever
from config import KNOWLEDGE_BASE_ID, REGION_NAME


@st.cache_resource(show_spinner=False)
def get_session():
    return boto3.Session(profile_name="Bedrock-admin", region_name=REGION_NAME)


session = get_session()


@st.cache_resource(show_spinner=False)
def get_model():
    return ChatBedrockConverse(
        model="apac.amazon.nova-lite-v1:0",
        max_tokens=2048,
        temperature=0.0,
        top_p=1,
        region_name=REGION_NAME,
        client=session.client("bedrock-runtime"),
        config=Config(
            connect_timeout=3600,
            read_timeout=3600,
            retries={"max_attempts": 1},
        ),
    )


model = get_model()


@st.cache_resource(show_spinner=False)
def get_retriever():
    return AmazonKnowledgeBasesRetriever(
        knowledge_base_id=KNOWLEDGE_BASE_ID,
        region_name=REGION_NAME,
        client=session.client("bedrock-agent-runtime"),
        retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
    )


retriever = get_retriever()