from extract.extract_users import extract_users
from transform.generate_messages import transform_users
from load.save_results import load_data

INPUT_PATH = "data/input/users.csv"
OUTPUT_PATH = "data/output/mensagens_marketing.csv"


def main():
    """
    Orquestra a execução completa do pipeline ETL:
    - Extração dos dados
    - Transformação com IA Generativa (simulada)
    - Carregamento dos dados transformados
    """
    print("Iniciando pipeline ETL...")

    # Etapa Extract
    df_users = extract_users(INPUT_PATH)
    print("Etapa Extract concluída.")

    # Etapa Transform
    df_transformed = transform_users(df_users)
    print("Etapa Transform concluída.")

    # Etapa Load
    load_data(df_transformed, OUTPUT_PATH)
    print("Etapa Load concluída.")

    print("Pipeline ETL executado com sucesso!")


if __name__ == "__main__":
    main()
