import streamlit as st

st.title("De acordo com a sua região, qual será seu desconto:")
st.sidebar.header("Me informe algumas coisas:")
valor = st.sidebar.number_input("Qual o valor da sua compra?")
codigo = st.sidebar.number_input("Qual é o codigo de origem do produto? (1 - Norte / 2 - Sul / 3 - Sudeste / 4 - Nordeste / 5 - Centro-Oeste)")

if codigo == 1:
    desconto = valor * 0.05
    if st.button("calcular_bottom"):
        st.write(f"O valor da sua compra é: {valor - desconto:.2f}")
elif codigo == 2:
    desconto = valor * 0.15
    if st.button("calcular_bottom"):
        st.write(f"O valor da sua compra é: {valor - desconto:.2f}")
elif codigo == 3:
    desconto = valor * 0.07
    if st.button("calcular_bottom"):
        st.write(f"O valor da sua compra é: {valor - desconto:.2f}")
elif codigo == 4:
    desconto = valor * 0.12
    if st.button("calcular_bottom"):
        st.write(f"O valor da sua compra é: {valor - desconto:.2f}")
elif codigo == 5:
    desconto = valor * 0.20
    if st.button("calcular_bottom"):
        st.write(f"O valor da sua compra é: {valor - desconto:.2f}")
