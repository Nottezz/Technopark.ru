import allure


def test_multiple_attachments():
    allure.attach.file('D:\\My Project\\Python\\Technopark.ru\\screenshots\\', attachment_type=allure.attachment_type.PNG)