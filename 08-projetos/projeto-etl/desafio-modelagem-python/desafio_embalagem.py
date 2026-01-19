import os

"""
📦 Desafio: Gerador de Relatório de Pedidos de Embalagens (Versão Automatizada)
Este script agora possui a capacidade de ler automaticamente de um arquivo CSV
localizado em data/input ou receber entradas manuais via terminal.
"""

def processar_pedidos():
    # Caminho para o arquivo de entrada
    caminho_input = os.path.join("data", "input", "pedidos.csv")
    
    # Inicialização do dicionário com os tipos obrigatórios
    totais = {
        "saco": 0.0,
        "papelao ondulado": 0.0,
        "papel kraft": 0.0
    }

    linhas = []

    # --- 1. EXTRAÇÃO (Extract) ---
    if os.path.exists(caminho_input):
        print(f"--- Lendo dados de: {caminho_input} ---")
        with open(caminho_input, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    else:
        # Fallback para entrada manual se o arquivo não existir
        print("--- Arquivo não encontrado. Aguardando entrada manual ---")
        try:
            n_pedidos = int(input("Digite o número de pedidos: "))
            for _ in range(n_pedidos):
                linhas.append(input())
        except ValueError:
            pass

    # --- 2. TRANSFORMAÇÃO (Transform) ---
    for linha in linhas:
        try:
            if not linha.strip(): continue
            
            partes = [p.strip() for p in linha.split(",")]
            if len(partes) >= 3:
                embalagem = partes[1].lower()
                quantidade = float(partes[2])
                
                if embalagem in totais:
                    totais[embalagem] += quantidade
        except (ValueError, IndexError):
            continue

    # --- 3. CARREGAMENTO/SAÍDA (Load) ---
    print("\n--- Resultado do Relatório ---")
    for tipo in ["saco", "papelao ondulado", "papel kraft"]:
        valor = totais[tipo]
        resultado = int(valor) if valor == int(valor) else valor
        print(f"{tipo}: {resultado}")

if __name__ == "__main__":
    processar_pedidos()