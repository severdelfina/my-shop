from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    # 1. Открыть сайт
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Нажать на вкладку "My Account"
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    # 3. В разделе "Register", введите email для регистрации
    email_field = driver.find_element(By.ID, "reg_email")
    email = "test" + str(int(time.time())) + "@example.com"  # Уникальный email
    email_field.send_keys(email)
    print(f"📧 Email: {email}")

    # 4. В разделе "Register", введите пароль для регистрации
    password_field = driver.find_element(By.ID, "reg_password")
    password = "StrongPassword123!"  # Пароль который даст Medium/Strong
    password_field.send_keys(password)
    print(f"🔑 Password: {password}")

    # Ждем пока пароль не станет Medium/Strong
    time.sleep(3)

    # Проверяем индикатор пароля
    password_strength = driver.find_element(By.CLASS_NAME, "woocommerce-password-strength")
    strength_text = password_strength.text
    print(f"📊 Password strength: {strength_text}")

    # 5. Нажмите на кнопку "Register"
    register_btn = driver.find_element(By.NAME, "register")
    register_btn.click()

    time.sleep(3)
    print("✅ Регистрация выполнена успешно!")

    # Сохраняем данные для следующего теста
    with open("registration_data.txt", "w") as f:
        f.write(f"Email: {email}\n")
        f.write(f"Password: {password}\n")

except Exception as e:
    print(f"❌ Ошибка: {e}")

finally:
    driver.quit()

#3. Registration_login: логин в систему

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Используем предыдущие данные
email = "test1764460650@example.com"
password = "StrongPassword123!"

print(f"Используем email: {email}")
print(f"Используем пароль: {password}")

try:
    # ТЕСТ ЛОГИНА
    print("\n=== ТЕСТ ЛОГИНА ===")

    # 1. Открыть сайт
    driver.get("https://practice.automationtesting.in/")
    time.sleep(3)

    # 2. Нажать на вкладку "My Account"
    my_account = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
    my_account.click()
    time.sleep(2)

    # 3. В разделе "Login", введите email для логина
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(email)

    # 4. В разделе "Login", введите пароль для логина
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    # 5. Нажмите на кнопку "Login"
    login_btn = driver.find_element(By.NAME, "login")
    login_btn.click()

    # Ждем загрузки страницы после логина
    time.sleep(5)

    # 6. Проверка, что на странице есть элемент "Logout" с явным ожиданием
    wait = WebDriverWait(driver, 10)
    logout_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(@href, 'customer-logout')]"))
    )

    if logout_element.is_displayed():
        print("Логин выполнен успешно! Элемент Logout найден.")
    else:
        print("Логин не удался. Элемент Logout не найден.")

except Exception as e:
    print(f"Ошибка: {e}")
    # Сделаем скриншот чтобы увидеть что на странице
    driver.save_screenshot("error_screenshot.png")
    print("Скриншот ошибки сохранен как 'error_screenshot.png'")

finally:
    driver.quit()