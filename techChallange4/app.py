import streamlit as st
from techChallange4.mlBackEnd import recebeDados


st.set_page_config(page_title="Teste de Paciente")

st.title("🧑‍⚕️ Avaliação de Paciente")

gender = st.selectbox("Gênero", ["Feminino", "Masculino"])
gender = 0 if gender == "Feminino" else 1
age = st.number_input("Idade", min_value=0, max_value=120)
height = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70)
weight = st.number_input("Peso (kg)", min_value=30, max_value=300, value=70)
family_history = st.selectbox("Histórico familiar de obesidade?", ["Não", "Sim"])
family_history = 1 if family_history == "Sim" else 0
favc = st.selectbox("Consome alimentos calóricos com frequência?", ["Não", "Sim"])
favc = 1 if favc == "Sim" else 0
fcvc = st.slider("Consumo de vegetais (0 a 3)", 0, 3, 1)
ncp = st.slider("Número de refeições principais por dia (1 a 4)", 1, 4, 3)
caec = st.selectbox("Come entre refeições?", ["Não", "Às vezes", "Frequentemente", "Sempre"])
caec = ["Não", "Às vezes", "Frequentemente", "Sempre"].index(caec)
smoke = st.selectbox("Fuma?", ["Não", "Sim"])
smoke = 1 if smoke == "Sim" else 0
ch2o = st.slider("Consumo de água por dia (1=baixo, 2=médio, 3=alto)", 1, 3, 2)
scc = st.selectbox("Monitora calorias?", ["Não", "Sim"])
scc = 1 if scc == "Sim" else 0
faf = st.slider("Atividade física semanal (0 a 3)", 0, 3, 1)
tue = st.slider("Tempo usando tecnologia por dia (0 a 2)", 0, 2, 1)
calc = st.slider("Consumo de álcool (0=Não, 1=Às vezes, 2=Freq., 3=Sempre)", 0, 3, 0)
mtrans = st.selectbox(
    "Meio de transporte",
    ["Carro", "Moto", "Bicicleta", "Transporte Público", "Caminhada"]
)
mtrans = ["Carro", "Moto", "Bicicleta", "Transporte Público", "Caminhada"].index(mtrans)

# Botão
if st.button("Testar paciente"):
    classe, imc = recebeDados(
        height=height,
        weight=weight,
        gender=gender,
        age=age,
        family_history=family_history,
        favc=favc,
        fcvc=fcvc,
        ncp=ncp,
        caec=caec,
        smoke=smoke,
        ch2o=ch2o,
        scc=scc,
        faf=faf,
        tue=tue,
        calc=calc,
        mtrans=mtrans
    )

    st.subheader("Resultado")
    st.success(f"Classe de peso prevista: {classe}, IMC calculado: {imc:.2f}")