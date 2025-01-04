import json
import os


def format_response(item, specific_content=None):
    """
    Форматирует ответ из базы знаний.
    Args:
        item (dict): Элемент базы знаний
        specific_content (str): Конкретный контент для ответа
    Returns:
        str: Отформатированный ответ
    """
    if specific_content:
        return f"**{item['text']}**\n\n{specific_content}"
    return f"**{item['text']}**\n\n" + "\n".join(item['content'])


def load_data_json(filename="./pars_web/data.json"):
    """
    Загружает базу знаний из JSON файла.
    Args:
        filename (str): Путь к файлу базы знаний
    Returns:
        dict: Загруженные данные
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_in_data_json(data, query):
    """
    Поиск ответа в базе знаний.
    Args:
        data (dict): База знаний
        query (str): Поисковый запрос
    Returns:
        str: Найденный ответ или None
    """
    query = query.lower()
    for item in data:
        if "text" in item and "content" in item:
            if query in item["text"].lower():
                return format_response(item)
            for content in item["content"]:
                if query in content.lower():
                    return format_response(item, content)
    return None
