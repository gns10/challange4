# backend/modelo.py

def testar_imc(altura: float, peso: float) -> str:
    """
    Recebe dados do paciente e retorna o resultado da análise
    """
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"