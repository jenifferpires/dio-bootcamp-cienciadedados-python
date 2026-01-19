def load_data(df, output_path: str):
    """
    Realiza o carregamento dos dados transformados em um arquivo CSV.

    Parâmetros:
        df (DataFrame): DataFrame com os dados transformados.
        output_path (str): Caminho para o arquivo CSV de saída.
    """
    try:
        df.to_csv(output_path, index=False)
    except Exception as e:
        raise RuntimeError(f"Erro ao carregar os dados: {e}")
