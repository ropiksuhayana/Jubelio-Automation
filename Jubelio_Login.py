from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from __init__ import*
import pytest
import time


class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def verify_title_login(self):
        main_title = driver.title
        # Verifikasi judul utama dengan yang diharapkan
        expected_title = "Jubelio"
        assert expected_title in main_title, f"Judul utama tidak sesuai. Diharapkan: '{expected_title}', Tampil: '{main_title}'"
        print("Judul utama terverifikasi: ", main_title)

    def logout(self):
        driver.get("https://app.jubelio.com/")

    def input_form_login(self):
        time.sleep(2)
        input_username = driver.find_element(By.NAME, 'email')
        input_username.send_keys(self.username)
        input_password = driver.find_element(By.NAME, 'password')
        input_password.send_keys(self.password)

    def click_login(self):
        click_login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div[2]/div/form/button')
        click_login.click()

    def wait_for_login_success(self):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="page-wrapper"]/div[2]/div/div/div[1]/h1')))

    def wait_for_toast_error(self):
        return WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[1]/li')))
        # Tunggu hingga toast muncul
    def wait_for_message_error(self):
        return WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.CLASS_NAME, 'help-block')))

    def verify_login_success(self):
        toast_element = self.wait_for_login_success()
        # Ambil teks toast
        toast_text = toast_element.text
        expected_text = "Selamat Datang"
        assert expected_text in toast_text, f"Toast message tidak sesuai. Diharapkan: '{expected_text}', Tampil: '{toast_text}'"
        print("Toast message terverifikasi: ", toast_text)

    def verify_toast_error(self):
        toast_element = self.wait_for_toast_error()
        # Ambil teks toast
        toast_text = toast_element.text
        expected_text = "Password atau email anda salah."
        assert expected_text in toast_text, f"Toast message tidak sesuai. Diharapkan: '{expected_text}', Tampil: '{toast_text}'"
        print("Toast message terverifikasi: ", toast_text)

    def verify_message_error(self):
        error_element = self.wait_for_message_error()
        # Ambil teks pesan error
        error_message = error_element.text
        # Verifikasi teks pesan error dengan yang diharapkan
        expected_error_message = "Password harus diisi."
        assert expected_error_message in error_message, f"Pesan error tidak sesuai. Diharapkan: '{expected_error_message}', Tampil: '{error_message}'"
        print("Pesan error terverifikasi: ", error_message)
      

def valid_login(login):
    open_browser()
    login.verify_title_login()
    login.input_form_login()
    login.click_login()
    time.sleep(2)
    login.wait_for_login_success()
    login.verify_login_success()
    
   

def invalid_login(login):
    open_browser()
    login.verify_title_login()
    login.input_form_login()
    login.click_login()
    login.wait_for_toast_error()
    login.verify_toast_error()
    
   
def login_with_blank_field(login):
    open_browser()
    login.verify_title_login()
    login.input_form_login()
    login.click_login()
    login.verify_message_error()
    
      
def main():
    username = "qa.rakamin.jubelio@gmail.com"
    password = "Jubelio123!" 
    invalid_username = ""
    invalid_password = "passwordsalah"
    blank_username = ""
    blank_password = ""
    login = Login(username, password)
    invalidLogin = Login(invalid_username, invalid_password)
    loginWithBlankField = Login(blank_username, blank_password)
    valid_login(login)
    login.logout()
    invalid_login(invalidLogin)
    login_with_blank_field(loginWithBlankField)
    close_browser()

if __name__ == "__main__":
    main()

  

