import os
import streamlit as st
import google.generativeai as genai

api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash")

def minhafuncao(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar resposta: {str(e)}"

st.title("Gerador de Receitas Culinárias Personalizadas com IA 🧑‍🍳")

ingredientes = st.text_area(
    "Liste os Ingredientes que você tem:",
    placeholder="Exemplo: frango, tomate, cebola, arroz"
)

tipo_culinaria = st.selectbox(
    "Escolha o Tipo de Culinária:",
    ["Italiana", "Brasileira", "Asiática", "Mexicana", "Qualquer uma"]
)

nivel_dificuldade = st.slider(
    "Escolha o Nível de Dificuldade:", 1, 5, 1
)

possui_restricao = st.checkbox("Tem alguma Restrição Alimentar?")
restricao_str = ""
if possui_restricao:
    restricao_str = st.text_input(
        "Especifique a Restrição Alimentar:",
        placeholder="Exemplo: sem glúten, vegetariana, sem lactose"
    )

if st.button("Sugerir Receita"):
    if ingredientes:
        with st.spinner("Gerando receita..."):
            prompt = (
                f"Sugira uma receita {tipo_culinaria} com nível de dificuldade {nivel_dificuldade} "
                f"(sendo 1 muito fácil e 5 desafiador). Deve usar principalmente os seguintes ingredientes: '{ingredientes}'. "
                f"{f'Considere a seguinte restrição alimentar: {restricao_str}.' if possui_restricao else ''} "
                f"Apresente o nome da receita, uma lista de ingredientes adicionais se necessário, e um breve passo a passo."
            )
            resposta = minhafuncao(prompt)
        st.subheader("Sugestão de Receita:")
        st.write(resposta)
    else:
        st.warning("Por favor, liste os ingredientes principais.")