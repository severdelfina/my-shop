from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Данные для логина
email = "test1764460650@example.com"
password = "StrongPassword123!"

try:
    # 1. Откройте https://practice.automationtesting.in/
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Залогиньтесь
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    time.sleep(3)

    print("Логин выполнен успешно!")

    # 3. Нажмите на вкладку "Shop"
    shop_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]")
    shop_tab.click()
    time.sleep(3)

    # 4. Откройте книгу "HTML 5 Forms"
    html5_book = driver.find_element(By.XPATH, "//img[@alt='Mastering HTML5 Forms']")
    html5_book.click()
    time.sleep(3)

    # 5. Добавьте тест, что заголовок книги называется: "HTML5 Forms"
    book_title = driver.find_element(By.CLASS_NAME, "product_title")
    actual_title = book_title.text

    expected_title = "HTML5 Forms"

    if actual_title == expected_title:
        print(f"Тест пройден! Заголовок книги: '{actual_title}'")
    else:
        print(f"Тест не пройден! Ожидалось: '{expected_title}', но получили: '{actual_title}'")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()

    #5. Shop: количество товаров в категории

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Данные для логина
email = "test1764460650@example.com"
password = "StrongPassword123!"

try:
    # 1. Откройте https://practice.automationtesting.in/
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Залогиньтесь
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    time.sleep(3)

    print("✅ Логин выполнен успешно!")

    # 3. Нажмите на вкладку "Shop"
    shop_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]")
    shop_tab.click()
    time.sleep(3)

    # 4. Откройте категорию "HTML"
    html_category = driver.find_element(By.XPATH, "//a[contains(@href, 'product-category/html')]")
    html_category.click()
    time.sleep(3)

    # 5. Добавьте тест, что отображается три товара
    # Находим все карточки товаров по общему классу изображений
    products = driver.find_elements(By.XPATH, "//img[contains(@class, 'attachment-shop_catalog')]")

    product_count = len(products)
    expected_count = 3

    if product_count == expected_count:
        print(f"✅ Тест пройден! Отображается {product_count} товара")
    else:
        print(f"❌ Тест не пройден! Ожидалось {expected_count} товара, но отображается {product_count}")

    # Выводим названия товаров для проверки
    print("📚 Найденные товары:")
    for i, product in enumerate(products, 1):
        alt_text = product.get_attribute("alt")
        print(f"  {i}. {alt_text}")

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()

#6. Shop: сортировка товаров

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Данные для логина
email = "test1764460650@example.com"
password = "StrongPassword123!"

try:
    # 1. Откройте https://practice.automationtesting.in/
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Залогиньтесь
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    time.sleep(3)

    print("✅ Логин выполнен успешно!")

    # 3. Нажмите на вкладку "Shop"
    shop_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]")
    shop_tab.click()
    time.sleep(3)

    # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
    sort_select = Select(driver.find_element(By.CLASS_NAME, "orderby"))
    selected_option = sort_select.first_selected_option
    default_value = selected_option.get_attribute("value")

    if default_value == "menu_order":
        print("✅ Сортировка по умолчанию выбрана (menu_order)")
    else:
        print(f"❌ Ожидалась сортировка menu_order, но выбрана: {default_value}")

    # 5. Отсортируйте товары по цене от большей к меньшей
    sort_select.select_by_value("price-desc")
    time.sleep(3)

    # 6. Снова объявите переменную с локатором основного селектора сортировки
    sort_select = Select(driver.find_element(By.CLASS_NAME, "orderby"))

    # 7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
    selected_option = sort_select.first_selected_option
    current_value = selected_option.get_attribute("value")

    if current_value == "price-desc":
        print("✅ Сортировка по цене от большей к меньшей выбрана (price-desc)")
    else:
        print(f"❌ Ожидалась сортировка price-desc, но выбрана: {current_value}")

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()

#7. Shop: отображение, скидка товара

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Данные для логина
email = "test1764460650@example.com"
password = "StrongPassword123!"

try:
    # 1. Откройте https://practice.automationtesting.in/
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Залогиньтесь
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(email)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()
    time.sleep(3)

    print("✅ Логин выполнен успешно!")

    # 3. Нажмите на вкладку "Shop"
    shop_tab = driver.find_element(By.XPATH, "//a[contains(text(),'Shop')]")
    shop_tab.click()
    time.sleep(3)

    # 4. Откройте книгу "Android Quick Start Guide"
    android_book = driver.find_element(By.XPATH, "//img[@alt='Android Quick Start Guide']")
    android_book.click()
    time.sleep(3)

    # 5. Добавьте тест, что содержимое старой цены = "₹600.00"
    old_price = driver.find_element(By.XPATH, "//del//span[@class='woocommerce-Price-amount amount']")
    old_price_text = old_price.text
    assert old_price_text == "₹600.00", f"Старая цена: {old_price_text}, ожидалось: ₹600.00"
    print("✅ Старая цена верная: ₹600.00")

    # 6. Добавьте тест, что содержимое новой цены = "₹450.00"
    new_price = driver.find_element(By.XPATH, "//ins//span[@class='woocommerce-Price-amount amount']")
    new_price_text = new_price.text
    assert new_price_text == "₹450.00", f"Новая цена: {new_price_text}, ожидалось: ₹450.00"
    print("✅ Новая цена верная: ₹450.00")

    # 7. Добавьте явное ожидание и нажмите на обложку книги
    book_cover = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']"))
    )
    book_cover.click()
    time.sleep(2)

    # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик
    close_preview = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
    )
    close_preview.click()
    time.sleep(2)

    print("✅ Предпросмотр открыт и закрыт успешно!")

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()

