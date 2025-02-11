import pandas as pd 
import pytest
from movies_analysis import group_movies_by_year_genre

def test_group_movies_by_year_genre():

    # data frame test
    data = {
        "Year": [2000, 2000, 2001, 2001, 2001, 2002],
        "Genre": ["Action", "Comedy", "Action", "Drama", "Drama", "Comedy"],
    }
    df_test = pd.DataFrame(data)

    result = group_movies_by_year_genre(df_test)

    # Verifichiamo che le colonne siano corrette
    assert list(result.columns) == ["Year", "Genre", "Count"]

    # Verifichiamo che il numero di righe sia corretto (5 combinazioni uniche)
    assert len(result) == 5

    # Controlliamo che il conteggio sia corretto
    assert result[(result["Year"] == 2001) & (result["Genre"] == "Drama")]["Count"].values[0] == 2
    assert result[(result["Year"] == 2000) & (result["Genre"] == "Action")]["Count"].values[0] == 1

    # Verifica che i valori di Count siano numeri interi
    assert result["Count"].dtype == "int64"