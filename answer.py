import json

def load_culture_deck(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

def search_in_culture_deck(deck, query):
    """
    Поиск ответа в списке объектов json
    """
    query = query.lower()
    for item in deck:
        if query in item["title"].lower() or query in item["content"].lower():
            return f"**{item['title']}**\n\n{item['content']}"
    return None
