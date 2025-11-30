from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Открыть сайт
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Проскроллить страницу вниз на 600 пикселей
    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(2)

    # 3. Нажать на название книги "Selenium Ruby"
    book = driver.find_element(By.XPATH, "//img[@alt='Selenium Ruby']")
    book.click()
    time.sleep(2)

    # 4. Нажать на вкладку "REVIEWS"
    reviews_tab = driver.find_element(By.XPATH, "//a[@href='#tab-reviews']")
    reviews_tab.click()
    time.sleep(1)

    # 5. Поставить 5 звёзд
    five_stars = driver.find_element(By.CLASS_NAME, "star-5")
    five_stars.click()
    time.sleep(1)

    # 6. Заполнить поле "Review" сообщением: "Nice book!"
    review_field = driver.find_element(By.ID, "comment")
    review_field.send_keys("Nice book!")

    # 7. Заполнить поле "Name"
    name_field = driver.find_element(By.ID, "author")
    name_field.send_keys("Test User")

    # 8. Заполнить "Email"
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("test@example.com")

    # 9. Нажать на кнопку "SUBMIT"
    submit_btn = driver.find_element(By.ID, "submit")
    submit_btn.click()

    time.sleep(3)
    print("Тест выполнен успешно! Комментарий отправлен.")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()