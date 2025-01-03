import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LATOKENParser:
    def __init__(self):
        self.BASE_URL = "https://coda.io/@latoken/latoken-talent"
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
                                     options=self.options)

    def open_menu(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "U9lQXSvT"))
            )
            
            menu_parents = self.driver.find_elements(By.CLASS_NAME, "U9lQXSvT")
            
            print(f"Найдено кнопок меню: {len(menu_parents)}")
            
            for menu_parent in menu_parents:
                try:

                    button = menu_parent.find_element(By.CLASS_NAME, "OVNGYAyZ")

                    self.driver.execute_script("arguments[0].click();", button)
                    time.sleep(3)  
                except Exception as e:
                    print(f"Ошибка при открытии одного из меню: {e}")
                    continue
                
        except Exception as e:
            print(f"Ошибка при открытии меню: {e}")

    def extract_page_content(self, url):
        try:
            self.driver.get(url)
            time.sleep(3)
            
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "UiR3cpYj"))
            )
            
            content_blocks = self.driver.find_elements(By.CLASS_NAME, "UiR3cpYj")
            content_texts = []
            seen_texts = set()  
            
            for block in content_blocks:
                text = block.text.strip()
                if text and text not in seen_texts: 
                    content_texts.append(text)
                    seen_texts.add(text)
                    
            return content_texts
            
        except Exception as e:
            print(f"Ошибка при извлечении контента страницы: {e}")
            return []

    def get_menu_items(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "vn7sffxq"))
        )
        items = []
        menu_elements = self.driver.find_elements(By.CLASS_NAME, "vn7sffxq")
        
        for item in menu_elements:
            try:
                link_element = item.find_element(By.CLASS_NAME, "b_aUTdOG")
                text_element = item.find_element(By.CLASS_NAME, "XLiPtG_S")
                
                items.append({
                    "text": text_element.text,
                    "link": link_element.get_attribute("href")
                })
            except Exception:
                continue
        
        return items

    def save_to_json(self, data, filename="data.json"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({"data": data}, f, ensure_ascii=False, indent=4)
            print(f"\nДанные успешно сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении в JSON: {e}")

    def run(self):
        try:
            print("Начинаем парсинг...")
            self.driver.get(self.BASE_URL)
            self.driver.maximize_window()
            time.sleep(5)
            
            print("Открываем меню...")
            self.open_menu()
            
            menu_items = self.get_menu_items()
            total_items = len(menu_items)
            print(f"\nВсего найдено пунктов меню: {total_items}")
            
            menu_data = []
            
            for index, item in enumerate(menu_items, 1):
                if item["text"].strip():
                    print(f"\nОбрабатываем пункт меню [{index}/{total_items}]: {item['text']}")
                    content = self.extract_page_content(item["link"])
                    menu_data.append({
                        "text": item["text"],
                        "link": item["link"],
                        "content": content
                    })
                    print(f"Обработано блоков контента: {len(content)}")
            
            print("\nСохраняем результаты...")
            self.save_to_json(menu_data)
            
            print("\nПарсинг успешно завершен!")
            
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    parser = LATOKENParser()
    parser.run()
