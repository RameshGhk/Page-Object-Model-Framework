# Page Object model Test automation framework using Selenium with python-

********Instructions to execute the test automation.************************

1) Requirements and installation to run the tests

Install Python and set up.
Install plugins for pytest, html report and ordering
Use below commands to install required plugins

**************If you are using python 3.x*****************
pip3 install pytest
pip3 install pytest-ordering
pip3 install pytest-html


**************If you are using python 2.x*****************
pip install pytest
pip install pytest-ordering
pip install pytest-html

2) How to run the test
Down load the project and navigate to project folder ie Page-Object-Model-Framework
Provide valid credentials in the TestClass.py in the place of 
parameter1
parameter2
parameter3
(Due to security reasons, credentials are not provided in the script)

Use below command to run the test and generate the report

py.test -s -v TestPackage/TestClass.py --html=Htmlreport.html
