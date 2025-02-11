import pandas as pd

def group_movies_by_year_genre(df):
    """ Raggruppa i film per Anno e Genere e conta quanti ce ne sono """
    return df.groupby(["Year", "Genre"]).size().reset_index(name="Count")