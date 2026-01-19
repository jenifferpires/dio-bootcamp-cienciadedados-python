import os

def gerar_relatorio_exportacao():
    # Tenta ler do arquivo de entrada primeiro (para seu ambiente local)
    caminho_input = os.path.join("data", "input", "exportacoes.csv")
    linhas = []

    if os.path.exists(caminho_input):
        with open(caminho_input, "r", encoding="utf-8") as f:
            # Pula a primeira linha se ela for o número N
            conteudo = f.readlines()
            if conteudo:
                linhas = conteudo[1:] if conteudo[0].strip().isdigit() else conteudo
    else:
        # Modo de entrada padrão (para o console do desafio)
        try:
            n = int(input())
            for _ in range(n):
                linhas.append(input())
        except (EOFError, ValueError):
            pass

    exportacoes = {}

    for linha in linhas:
        linha = linha.strip()
        if not linha:
            continue
        
        try:
            # Separa por vírgula e remove espaços em branco das pontas
            partes = linha.split(",")
            pais = partes[0].strip()
            toneladas = float(partes[1].strip())
            
            # Soma mantendo a ordem da primeira aparição
            if pais in exportacoes:
                exportacoes[pais] += toneladas
            else:
                exportacoes[pais] = toneladas
        except (ValueError, IndexError):
            continue

    # Exibe o resultado no formato exato: "Pais: X toneladas"
    for pais, total in exportacoes.items():
        # Converte para int se não houver casas decimais (ex: 15.0 -> 15)
        valor_formatado = int(total) if total == int(total) else total
        print(f"{pais}: {valor_formatado} toneladas")

if __name__ == "__main__":
    gerar_relatorio_exportacao()