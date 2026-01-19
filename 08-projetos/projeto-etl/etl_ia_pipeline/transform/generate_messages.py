def generate_marketing_message(nome: str) -> str:
    """
    Gera uma mensagem de marketing personalizada simulando o uso de IA Generativa.

    Parâmetros:
        nome (str): Nome do cliente.

    Retorna:
        str: Mensagem personalizada.
    """
    return (
        f"Olá {nome}, investir é uma excelente forma de planejar o seu futuro financeiro. "
        f"Conte com o Santander para te apoiar nessa jornada!"
    )


def transform_users(df):
    """
    Aplica a etapa de transformação nos dados dos usuários, gerando mensagens personalizadas.

    Parâmetros:
        df (DataFrame): DataFrame com os dados extraídos.

    Retorna:
        DataFrame: DataFrame enriquecido com a coluna de mensagens.
    """
    df["mensagem"] = df["nome"].apply(generate_marketing_message)
    return df
