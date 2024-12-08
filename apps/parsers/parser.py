from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from .models import Exploit
from datetime import datetime
import time

def run_parser():
    chrome_driver_path = 'chromedriver.exe'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Фоновый режим
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1920,1080')

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True)

    try:
        driver.get('https://sploitus.com/?query=PoC#exploits')
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'panel')))

        sort_by_date_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-id='date']"))
        )
        sort_by_date_button.click()
        time.sleep(3)

        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        panels = soup.find_all('div', class_='panel')

        for panel in panels[:10]:
            try:
                title = panel.find('div', class_='accordion-header').text.strip()
                date_text = panel.find('div', class_='tile-subtitle').text.strip()
                date = datetime.strptime(date_text, '%Y-%m-%d').date()

                input_tag = panel.find('input', {'id': True})
                vuln_id = input_tag['id'] if input_tag else 'Unknown ID'

                source_button = panel.find('button', {'data-action': 'origin'})
                source_url = f"https://sploitus.com/exploit?id={source_button['data-id']}" if source_button else ''

                exploit_links = []
                for btn in panel.find_all('button', {'data-action': 'goto'}):
                    exploit_id = btn.get('data-id')
                    if exploit_id:
                        exploit_links.append(f"https://sploitus.com/exploit?id={exploit_id}")

                # Сохраняем данные в базу
                exploit, created = Exploit.objects.update_or_create(
                    vuln_id=vuln_id,
                    defaults={
                        'title': title,
                        'date': date,
                        'source_url': source_url,
                        'exploit_links': ', '.join(exploit_links)
                    }
                )
                if created:
                    print(f"Добавлена уязвимость: {title}")
            except Exception as e:
                print(f"Ошибка при обработке панели: {e}")
    finally:
        driver.quit()
