import streamlit as st

st.title("De acordo com a sua região, qual será seu desconto:")
nome = st.text_input("Digite seu nome: ")

st.sidebar.header(f"Me informe algumas coisas {nome}:")
valor = st.sidebar.number_input("Qual o valor da sua compra?", min_value=0.1, format="%.2r")
codigo = st.sidebar.number_input("Qual é o codigo de origem do produto? (1 - Norte / 2 - Sul / 3 - Sudeste / 4 - Nordeste / 5 - Centro-Oeste)", min_value=1, max_value=5, format="%.2r")

if st.button("calcular desconto"):
  if codigo == 1:
    desconto = valor * 0.05
    st.write(f"O valor da sua compra é: {valor - desconto}")
  elif codigo == 2:
    desconto = valor * 0.15
    st.write(f"O valor da sua compra é: {valor - desconto}")
  elif codigo == 3:
    desconto = valor * 0.07
    st.write(f"O valor da sua compra é: {valor - desconto}")
  elif codigo == 4:
    desconto = valor * 0.12
    st.write(f"O valor da sua compra é: {valor - desconto}")
  elif codigo == 5:
    desconto = valor * 0.20
    st.write(f"O valor da sua compra é: {valor - desconto}")
