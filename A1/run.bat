set browser=firefox
behave -f allure_behave.formatter:AllureFormatter -o reports\allure_result -D browser=%browser%
allure generate reports\allure_result -o reports\allure_report --clean
python C:\Users\codoid\PycharmProjects\Python-Framework\A1\Features\utils\send_mail.py %browser%
python C:\Users\codoid\PycharmProjects\Python-Framework\A1\Features\utils\slack_notifications.py %browser%