import json
import os
from datetime import datetime

SCORES_FILE = "scores.json"

class Chart:
    def __init__(self):
        self.players = []
        self.load_scores()

    def add(self, player):
        """Aggiunge un giocatore alla classifica e aggiorna il file JSON."""
        self.players.append(player)
        self.save_scores()

    def get_best_player(self):
        """Restituisce il giocatore con il miglior punteggio o None se la classifica è vuota."""
        if not self.players:
            return None
        best_player = self.players[0]
        for player in self.players:
            if player.p_attempts < best_player.p_attempts:
                best_player = player
            elif player.p_attempts == best_player.p_attempts and player.time_elapsed < best_player.time_elapsed:
                best_player = player
        return best_player

    def sort_players(self):
        """Ordina i giocatori per numero di tentativi e, a parità, per tempo trascorso."""
        """
        lamba è una funzione anonima sostituisce questo
        def sort_key(p):
            return (p.p_attempts, p.time_elapsed)
        """
        self.players.sort(key=lambda p: (p.p_attempts, p.time_elapsed))
        return self.players

    def print_ranking(self):
        """Stampa la classifica ordinata per punteggio."""
        print("\n🏆 CLASSIFICA FINALE 🏆")
        sorted_players = self.sort_players()
        for i, player in enumerate(sorted_players, 1):
            print(f"{i}. {player.name}: {player.p_attempts} tentativi, {player.time_elapsed} secondi")
        print()

    def save_scores(self):
        """Salva i punteggi su un file JSON."""
        with open(SCORES_FILE, "w") as f:
            json.dump([player.to_dict() for player in self.players], f)

    def load_scores(self):
        """Carica i punteggi salvati da un file JSON."""
        if os.path.exists(SCORES_FILE):
            try:
                with open(SCORES_FILE, "r") as f:
                    data = json.load(f)
                    self.players = [Player(**entry) for entry in data]
            except json.JSONDecodeError:
                print("Errore nel caricamento del file JSON, potrebbe essere corrotto.")

class Player:
    def __init__(self, name, p_attempts, time_elapsed, date=None):
        self.name = name
        self.p_attempts = p_attempts
        self.time_elapsed = time_elapsed
        # print(datetime.now()) >> 2025-02-03 16:58:05.211644
        # la rendo leggibile troncando i millisecondi
        self.date = date if date else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        """Restituisce un dizionario con i dati del giocatore."""
        return {
            "name": self.name,
            "p_attempts": self.p_attempts,
            "time_elapsed": self.time_elapsed,
            "date": self.date,
        }

    def __repr__(self):
        return f"Player(name='{self.name}', attempts='{self.p_attempts}', time_elapsed='{self.time_elapsed}')"
