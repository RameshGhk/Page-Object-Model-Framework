from UtilityPackage.SeleniumDriver import SeleniumDriver


"""
Registration class : Page class which contains all the methods and variables
to locate the elements of the registration page in github.
These methods can be re-used to validate the registration to github by 
creating instance or object of this class and calling (like object.method())
to validate the registration test case with any given user name, email and password
"""

class Registration(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators in registration page to github    #Locator types for reference
    _UserNameField = "user[login]"              #id
    _EmailField = "user[email]"                 #id
    _PasswordField = "user[password]"           #id
    _SignUpButton = "//button[@type='submit']"  #xpath
    _VerifyRegistration = "//p[@class='shelf-lead']"


    def FillUserNameField(self, username):
        self.sendKeys(username, self._UserNameField, locatorType="id")

    def FillEmailField(self, email):
        self.sendKeys(email, self._EmailField, locatorType="id")

    def FillPasswordField(self, password):
        self.sendKeys(password, self._PasswordField, locatorType="id")

    def ClickSignUpbutton(self):
        self.elementClick(self._SignUpButton, locatorType="xpath")

    def UserRegistration(self, username, email, password):
        self.FillUserNameField(username)
        self.FillEmailField(email)
        self.FillPasswordField(password)
        self.ClickSignUpbutton()

    def VerifyRegistration(self):
        element = self.isElementPresent(self._VerifyRegistration, locatorType="xpath")
        return element

