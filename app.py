# -*- coding: utf-8 -*-
"""yck.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uNZkLH9gB8t7BXhmCyA5rr33MsTgpQPt
"""

# !pip install langchain_google_genai

# !pip install langchain

import urllib
import warnings
from pathlib import Path as p
from pprint import pprint

import pandas as pd
from langchain import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain

# !pip install -q -U google-generativeai

import pathlib
import textwrap

import google.generativeai as genai

# Used to securely store your API key
from google.colab import userdata

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

genai.configure(api_key="AIzaSyBRra0iamlfkvsn3dm5sjKUFJKSTmWueC0")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)

model = genai.GenerativeModel('gemini-pro')

# Commented out IPython magic to ensure Python compatibility.
# %%time
# response = model.generate_content("What is the meaning of life?")

from langchain.llms import OpenAI

# from langchain.llms import LLM

class GeminiProAdapter():
    def __init__(self, models):
        self.model = models

    def generate_text(self, prompt: str) -> str:
        return self.model.generate_text(prompt=prompt)

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate(
    template="Answer the following question in a comprehensive and informative way, even if it is open ended, challenging, or strange: {question}",
    input_variables=["what is the shape of earth"]
)

import vertexai
from vertexai.language_models import TextGenerationModel

content = "i have built a semantic search model using Pinecone and FAISS model"
response = model.generate_content(f"{content}. Provide the Sentences in the How was the project created, what has been used and what was the impact created due to the project without including the questions, use numbers where ever it is possible")

import gradio as gr

def response(message, history):
    response = model.generate_content(f"{message}. Provide the Sentences in the How was the project created, what has been used and what was the impact created due to the project without including the questions, use numbers where ever it is possible")
    return response.candidates


demo = gr.ChatInterface(response)
demo.launch()

# !pip install gradio