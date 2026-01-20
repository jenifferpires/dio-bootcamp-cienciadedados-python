import pandas as pd


def extract_users(file_path: str) -> pd.DataFrame:
    """
    Realiza a extração dos dados dos usuários a partir de um arquivo CSV.

    Parâmetros:
        file_path (str): Caminho para o arquivo CSV de entrada.

    Retorna:
        pd.DataFrame: DataFrame contendo os dados extraídos.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair dados: {e}")
