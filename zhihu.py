import os
import platform
from time import sleep

from splinter import Browser

import config

'''
动态内容的爬取
通过 browser 不停地下拉浏览器
'''


def add_chrome_webdriver():
    print(platform.system())
    working_path = os.getcwd()
    library = 'library'
    path = os.path.join(working_path, library)
    os.environ['PATH'] += '{}{}{}'.format(os.pathsep, path, os.pathsep)
    print(os.environ['PATH'])


def add_cookie(browser):
    for part in config.cookie.split('; '):
        kv = part.split('=', 1)
        d = {kv[0]: kv[1]}
        browser.cookies.add(d)
        print('d', d)
    print(browser.cookies.all())


def scroll_to_end(browser):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def start_crawler():
    # with Browser('chrome', headless=True) as browser:
    # 即可开启无头模式，不打开浏览器
    # --user-data-dir 和 --headless 不能一起使用
    with Browser('chrome') as browser:
        url = "https://www.zhihu.com"
        browser.visit(url)

        add_cookie(browser)
        browser.reload()
        print(browser.html)

        scroll_to_end(browser)

        found = False
        while not found:
            print('loop')
            found = browser.is_text_present('王者')
            if found:
                print('拿到了最近1天动态')
                sleep(50)
                break
            else:
                scroll_to_end(browser)


def main():
    add_chrome_webdriver()
    start_crawler()


if __name__ == '__main__':
    main()
