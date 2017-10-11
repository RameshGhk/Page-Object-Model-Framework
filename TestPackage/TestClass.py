from selenium import webdriver
from PageObjectsPackage.RegistrationPage import Registration
from PageObjectsPackage.LoginPage import LoginToGithub
import unittest
import pytest
import time


class Github_Login_Functionality_validation(unittest.TestCase):
    baseURL = "https://github.com/"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)
    rp = Registration(driver)
    lp = LoginToGithub(driver)


    """
    Test case 1 : Registration test case to Github.
    Use valid user name, email and password to test the test case to register to github.
    parameter1 : is user name
    parameter2 : is email
    parameter3 : is password
    """
    @pytest.mark.run(order=1)
    def test_Registration(self):
        self.driver.get(self.baseURL)
        self.rp.UserRegistration("Rameshroppa", "ramesh.roppapvg@gmail.com", "Rameshghk@2017")
        result = self.rp.VerifyRegistration()
        assert result == True
        self.driver.quit()



    """
    Test case 2 : Login test to Github with valid credentials.
    Due to security reasons, user name and password are not provided in the script.
    Use valid user name and password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """
    @pytest.mark.run(order=4)
    def test_Login_with_valid_credentials(self):
        self.driver.get(self.baseURL)
        self.lp.UserLogin("ramesh.roppapvg@gmail.com", "Rameshghk@2017")
        time.sleep(5)
        result=self.lp.VerifyLogin()
        assert result==True
        self.driver.quit()


    """
    Test case 3 : Login test to Github with Invalid User name.
    Use Invalid user name and and valid password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """
    @pytest.mark.run(order=2)
    def test_Login_with_Invalid_UserName(self):
        self.driver.get(self.baseURL)
        self.lp.UserLogin("ramesXXXXXX@gmail.com", "ValidPassword")
        time.sleep(5)
        result=self.lp.VerifyLogin()
        assert result==True
        self.driver.quit()


    """
    Test case 4 : Login test to Github with valid user name and Invalid password.
    Use valid user name and Invalid password to test the test case to login to github.
    parameter1 : is user name or email
    parameter2 : is password
    """
    @pytest.mark.run(order=3)
    def test_Login_with_Invalid_Password(self):
        self.driver.get(self.baseURL)
        self.lp.UserLogin("ramesh.ghk2020@gmail.com", "XXXXXXX")
        time.sleep(5)
        result=self.lp.VerifyLogin()
        assert result==True
        self.driver.quit()