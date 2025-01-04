import json
import os

def load_culture_deck(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

data_json = load_culture_deck("./pars_web/data.json")

def search_in_culture_deck(deck, query):
    """
    Поиск ответа в базе знаний
    """
    query = query.lower()
    
    for item in deck["data"]:
        if query in item["text"].lower():
            response = f"**{item['text']}**\n\n"
            for content in item["content"]:
                if content.strip():
                    response += f"{content}\n\n"
            return response
        
        for content in item["content"]:
            if query in content.lower():
                return f"**{item['text']}**\n\n{content}"
                
    return None


def save_unknown_question(question):
    """Сохраняет неизвестный вопрос в базу знаний."""

    if not os.path.exists(data_json):
        with open(data_json, "w", encoding="utf-8") as file:
            json.dump({"questions": []}, file, ensure_ascii=False, indent=4)

    with open(data_json, "r", encoding="utf-8") as file:
        data = json.load(file)

    if question not in data["questions"]:
        data["questions"].append(question)

        with open(data_json, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Сохранен новый вопрос: {question}")
    else:
        print(f"Вопрос уже существует: {question}")
