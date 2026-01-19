"""
📦 Desafio: Gerador de Relatório de Pedidos de Embalagens
Este script processa pedidos de exportação e sumariza o total de toneladas 
solicitadas por tipo de embalagem, garantindo a integridade dos dados 
mesmo para categorias sem pedidos.
"""

# -------------------------------------------------------------------------
# 1. ENTRADA DE DADOS (Extract)
# -------------------------------------------------------------------------
try:
    N = int(input())
except ValueError:
    N = 0

# Inicialização do dicionário com os tipos obrigatórios (Schema fixo)
totais = {
    "saco": 0.0,
    "papelao ondulado": 0.0,
    "papel kraft": 0.0
}

# -------------------------------------------------------------------------
# 2. PROCESSAMENTO (Transform)
# -------------------------------------------------------------------------
for _ in range(N):
    try:
        linha = input()
        # Parsing da linha: Cliente, Tipo, Quantidade
        partes = [p.strip() for p in linha.split(",")]
        
        if len(partes) >= 3:
            embalagem = partes[1].lower() # Padronização para evitar erros de case
            quantidade = float(partes[2])
            
            # Acumulação dos valores
            if embalagem in totais:
                totais[embalagem] += quantidade
    except (ValueError, IndexError):
        continue

# -------------------------------------------------------------------------
# 3. SAÍDA FORMATADA (Load/Display)
# -------------------------------------------------------------------------
ordem_saida = ["saco", "papelao ondulado", "papel kraft"]

for tipo in ordem_saida:
    valor = totais[tipo]
    # Formatação: exibe como inteiro se não houver casas decimais significativas
    resultado = int(valor) if valor == int(valor) else valor
    print(f"{tipo}: {resultado}")