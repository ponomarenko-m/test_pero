import pytest
from playwright.sync_api import sync_playwright

def test_vk_message_button():
    with sync_playwright() as p:
        # Запуск браузера
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Открытие страницы
        page.goto("https://vk.com/club225299895?w=product-225299895_10044406")

        # Клик по кнопке "Написать"
        page.click("span.MarketServiceButton__text")

        # Ожидание диалога
        page.wait_for_selector("div.WriteLayout", timeout=5000)

        # Проверка, что диалог открылся
        dialog = page.query_selector("div.WriteLayout")
        assert dialog is not None, "Диалоговое окно не открылось"

        # Клик по кнопке "Отправить"
        page.click('button[id^="mail_box_send"]')

        # Закрытие браузера
        browser.close()

if __name__ == "__main__":
    pytest.main([__file__])