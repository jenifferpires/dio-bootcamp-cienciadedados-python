import os

"""
🌍 Desafio: Sistema de Totalização de Exportações por País
O script agrupa toneladas enviadas por país de destino, mantendo a 
ordem de inserção original conforme as regras do desafio.
"""

def gerar_relatorio_exportacao():
    caminho_input = os.path.join("data", "input", "exportacoes.csv")
    
    # Usamos um dicionário comum. No Python 3.7+, dicionários 
    # mantêm a ordem de inserção por padrão.
    exportacoes = {}
    linhas = []

    # --- 1. EXTRAÇÃO (Extract) ---
    if os.path.exists(caminho_input):
        with open(caminho_input, "r", encoding="utf-8") as f:
            linhas = f.readlines()
    else:
        try:
            n = int(input())
            for _ in range(n):
                linhas.append(input())
        except EOFError:
            pass

    # --- 2. TRANSFORMAÇÃO (Transform) ---
    for linha in linhas:
        if not linha.strip(): continue
        
        try:
            # Separa País e Toneladas (formato: Pais, Toneladas)
            partes = [p.strip() for p in linha.split(",")]
            pais = partes[0]
            toneladas = float(partes[1])
            
            # Acumula os valores preservando a ordem da primeira aparição
            if pais in exportacoes:
                exportacoes[pais] += toneladas
            else:
                exportacoes[pais] = toneladas
        except (ValueError, IndexError):
            continue

    # --- 3. CARREGAMENTO (Load) ---
    for pais, total in exportacoes.items():
        # Formata para inteiro se for .0 para seguir o padrão dos exemplos
        valor_final = int(total) if total == int(total) else total
        print(f"{pais}: {valor_final} toneladas")

if __name__ == "__main__":
    gerar_relatorio_exportacao()