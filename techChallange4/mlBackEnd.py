import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "Obesity.csv")

df = pd.read_csv(csv_path, sep=",")
# # Featuring engineering
# ## Arredondamento dos dados numéricos
def featuringEngineering():
    df = pd.read_csv(csv_path, sep=",")
    df.head(25)
    df.info()
    cols = ['Age','Weight','FCVC','NCP','CH2O','FAF','TUE']
    df[cols] = df[cols].round().astype(int)
    df

    # ## Criando coluna IMC

    df['IMC'] = df['Weight']/(df['Height'] ** 2)
    df['IMC'] = df['IMC'].round().astype(int)
    df['Obesity'].unique()

    df.columns


    df_num = df.copy()

    #Mapeamentos
    map_gender = {'Female': 0, 'Male':1}
    map_family_history = {'yes':1, 'no':0}
    map_FAVC = {'yes':1, 'no':0}
    map_CAEC = {'no':0,'Sometimes':1, 'Frequently':2 ,'Always':3}
    map_smoke = {'yes':1, 'no':0}
    map_SCC = {'yes':1, 'no':0}
    map_CALC = {'no':0,'Sometimes':1, 'Frequently':2 ,'Always':3}
    map_METRANS = {'Automobile': 0, "Motorbike": 1, 'Bike':2, 'Public_Transportation': 3, 'Walking': 4}

    df_num['Gender'] = df_num['Gender'].map(map_gender)
    df_num['family_history'] = df_num['family_history'].map(map_family_history)
    df_num['FAVC'] = df_num['FAVC'].map(map_FAVC)
    df_num['CAEC'] = df_num['CAEC'].map(map_CAEC)
    df_num['SMOKE'] = df_num['SMOKE'].map(map_smoke)
    df_num['SCC'] = df_num['SCC'].map(map_SCC)
    df_num['CALC'] = df_num['CALC'].map(map_CALC)
    df_num['MTRANS'] = df_num['MTRANS'].map(map_METRANS)

    return df_num


def createModel(df_num):
    # # Criando o modelo


    # Target
    y = df_num['Obesity']

    # Ajustando a string (ex.: 'Obese', 'Normal', etc.) para classes [0, 1, 2, 3, 4, 5, 6]
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Features (incluindo IMC e demais colunas)
    X = df_num.drop(columns=['Obesity'])


    #Divisão treino e teste
    # Teste com 30%
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.3, random_state=42, stratify=y_encoded
    )


    # Escolhendo o random forest
    from sklearn.ensemble import RandomForestClassifier

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

DE_PARA_OBESITY = {
    "normal_weight": "peso normal",
    "overweight_level_i": "sobrepeso I",
    "overweight_level_ii": "sobrepeso II",
    "obesity_type_i": "obesidade I",
    "obesity_type_ii": "obesidade II",
    "obesity_type_iii": "obesidade III",
}

def classes(df_num):
    le = LabelEncoder()
    df_num['Obesity'] = le.fit_transform(df_num['Obesity'])
    return le

# # Teste


# Função interativa para input de dados
def recebeDados(gender, age, height, weight, family_history, favc, fcvc, ncp, caec, smoke, ch2o, scc, faf, tue, calc, mtrans):
    df = featuringEngineering()
    model = createModel(df)
    le = classes(df)
    dados = {
        'Gender': gender,
        'Age': age,
        'Height': height,
        'Weight': weight,
        'family_history': family_history,
        'FAVC': favc,
        'FCVC': fcvc,
        'NCP': ncp,
        'CAEC': caec,
        'SMOKE': smoke,
        'CH2O': ch2o,
        'SCC': scc,
        'FAF': faf,
        'TUE': tue,
        'CALC': calc,
        'MTRANS': mtrans,
        'IMC': weight / (height ** 2)
    }
    classe, imc = testar_paciente(dados,model,le)
    return [classe, imc]

def testar_paciente(dados, model, le):
    print("=== Teste de Predição de Obesidade ===")

    # Calcula IMC automaticamente
    imc = dados['IMC']

    df_paciente = pd.DataFrame([dados])

    pred = model.predict(df_paciente)[0]
    # classe em inglês
    classe_en = le.inverse_transform([pred])[0]

    # de–para para português
    classe_pt = DE_PARA_OBESITY.get(classe_en, classe_en)

    return [classe_pt, imc]



