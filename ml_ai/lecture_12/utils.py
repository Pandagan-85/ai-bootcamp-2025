import requests


def text_to_df_filter(user_query, df):
    """
    This function is used to return a filter ot the dataframe based on a user query.
    :param user_query: str
    :param df: pd.DataFrame
    :return: str
    """
    df_columns = df.columns
    columns = " ,".join(df_columns)  #['a', 'b', 'c'] - > 'a, b, c'
    prompt = f"""
        Sei un assistente di Python. Scrivi una sola riga di codice Python valida che filtra il DataFrame pandas 'df'
        sulla base di query dell'utente:
        '{user_query}'. Il nostro DataFrame 'df' ha queste colonne: '{columns}'.
        Restituisci SOLO il filtro senza ulteriore testo di spiegazione o extra testo.
        Ad esempio:
        df[df["colonna"] == valore] oppure df[df["colonna"] < valore]
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
