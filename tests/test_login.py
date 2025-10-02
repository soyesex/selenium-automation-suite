from selenium import webdriver
from page_objects.login_page import LoginPage
from page_objects.dashboard_page import DashboardPage

def test_successful_login(driver):
    
    driver.get("https://app.staging.datascend.net/auth/login")
    
    login_page = LoginPage(driver)
    login_page.login("administrator@multiplied.com", "daUser1test")

    print("Login action performed successfully.")

    dashboard_page = DashboardPage(driver)
    profile_name = dashboard_page.get_user_profile_name()
    assert profile_name == "Global Administrator"