import json
import os

class DBProxy:
    def __init__(self, db_file="DBScore.json"):
        self.db_file = db_file
        if not os.path.exists(self.db_file):
            with open(self.db_file, 'w') as file:
                json.dump([], file)  # Cria o arquivo com uma lista vazia

    def save(self, entry: dict): #Salva uma nova entrada no banco de dados (arquivo JSON).
        data = self._load_data()
        data.append(entry)
        self._save_data(data)

    def retrieve_top5(self): #Recupera as 5 maiores pontuações ordenadas de forma decrescente.
        data = self._load_data()
        return sorted(data, key=lambda x: x['score'], reverse=True)[:5]

    def cleanup_top_scores(self, max_scores: int): #Limita o número de pontuações salvas para
        # `max_scores` no máximo.
        data = self._load_data()
        data = sorted(data, key=lambda x: x['score'], reverse=True)[:max_scores]
        self._save_data(data)

    def _load_data(self): #Carrega os dados do arquivo JSON.
        with open(self.db_file, 'r') as file:
            return json.load(file)

    def _save_data(self, data): #Salva os dados no arquivo JSON.
        with open(self.db_file, 'w') as file:
            json.dump(data, file, indent=4)
