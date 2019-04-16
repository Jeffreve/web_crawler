import platform
import os
from time import sleep
from splinter import Browser

'''
python 使用 splinter 通过 api 来控制 chrome，需要Chromedriver
https://splinter.readthedocs.io/en/latest/
splinter chrome api
'''


def add_chrome_webdriver():
    print(platform.system())
    working_path = os.getcwd()
    library = 'chromedriver'
    path = os.path.join(working_path, library)
    os.environ['PATH'] += '{}{}{}'.format(os.pathsep, path, os.pathsep)
    print(os.environ['PATH'])


def find_website():
    with Browser('chrome') as browser:
        url = "http://www.baidu.com"
        browser.visit(url)

        # find search and input
        input = browser.find_by_css('#kw')
        input.fill('hou')

        # find and click the 'search' button
        button = browser.find_by_css('#su')
        button.click()

        if browser.is_text_present('fanyi.baidu.com'):
            print("Yes, the official website was found!")
            sleep(50)
        else:
            print("No, it wasn't found... We need to improve our SEO techniques")


def main():
    # Chromedriver 添加到环境变量
    add_chrome_webdriver()
    # API 控制浏览器
    find_website()


if __name__ == '__main__':
    main()
