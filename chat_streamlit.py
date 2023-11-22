#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 07:34:27 2023

@author: diegofernandez
"""

import streamlit as st
from llama_cpp import Llama

# Cargar el modelo de lenguaje grande
LLM = Llama(model_path="/Users/diegofernandez/Downloads/llama-2-7b-chat.Q4_K_M.gguf", n_ctx=2048)

# Inicializar un lugar para guardar las preguntas y respuestas
qa_pairs = []

# Función para guardar las preguntas y respuestas en un archivo HTML
def save_to_html(qa_list):
    with open('qa_output.html', 'w') as file:
        for qa in qa_list:
            question, answer = qa
            file.write(f"<p><b>Question:</b> {question}</p>\n")
            file.write(f"<p><b>Answer:</b> {answer}</p>\n<hr>\n")

# Streamlit app
def run_app():
    st.title("LLM Question Answering App")

    # Entrada de la pregunta
    question = st.text_input("Enter your question:")

    if st.button("Ask LLM"):
        if question:
            # Generar respuesta
            output = LLM(question, max_tokens=0)
            answer = output["choices"][0]["text"]
            
            # Mostrar respuesta
            st.write("Answer:", answer)

            # Guardar la pregunta y respuesta
            qa_pairs.append((question, answer))

    if st.button("Exit and Save"):
        save_to_html(qa_pairs)
        st.success("Questions and answers saved to qa_output.html")
        st.stop()

# Ejecutar la aplicación
if __name__ == "__main__":
    run_app()
