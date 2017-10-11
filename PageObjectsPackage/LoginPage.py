from UtilityPackage.SeleniumDriver import SeleniumDriver


"""
LoginToGithub class : Page class which contains all the methods and variables. 
All the methods can be re-used by creating object of this class and calling as object.method()
to execute the test case.
Methods defined here are used in TestClass to validate the github login functionality.
"""

class LoginToGithub(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators in login page for github              #Locator types for reference
    _LoginLink = "//a[@href='/login']"              #xpath
    _EmailField = "login_field"                     #id
    _PasswordField = "password"                     #id
    _SignInButton = "commit"                        #name
    _VerifyLogin = "//p[@class='shelf-lead']"       #xpath


    def ClickLoginLink(self):
        self.elementClick(self._LoginLink, locatorType="xpath")

    def FillEmailField(self, email):
        self.sendKeys(email, self._EmailField, locatorType="id")

    def FillPasswordField(self, password):
        self.sendKeys(password, self._PasswordField, locatorType="id")

    def ClickSignInbutton(self):
        self.elementClick(self._SignInButton, locatorType="name")

    def VerifyLogin(self):
        element = self.isElementPresent(self._VerifyLogin, locatorType="xpath")
        return element

    def UserLogin(self, email, password):
        self.ClickLoginLink()
        self.FillEmailField(email)
        self.FillPasswordField(password)
        self.ClickSignInbutton()
