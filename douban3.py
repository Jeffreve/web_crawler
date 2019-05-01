import os
import sqlite3

import requests
from pyquery import PyQuery as pq

from model_sqlite import insert, create, select, delete, update

'''
先建立文件名，查看本地是否有该文件
有的话，本地取出
没有的话，爬虫下载保存
打印的同时，将数据保存至数据库
'''


class Model():
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    def __init__(self):
        self.name = ''
        self.other = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def get(url, filename):
    # 缓存, 避免重复下载网页浪费时间
    # 建立 cached 文件夹
    folder = 'douban3'
    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            return r.content


def movie_from_div(div):
    e = pq(div)
    m = Movie()
    m.name = e('.title').text()
    m.other = e('.other').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic').find('em').text()

    db_path = 'douban.sqlite'
    db_table = 'top250'
    connection = sqlite3.connect(db_path)
    # print("打开了数据库")

    create(connection, db_table)
    insert(connection, db_table, m.name, m.other, m.score, m.quote, m.cover_url, m.ranking)

    connection.commit()
    connection.close()
    return m


def save_cover(movies):
    for m in movies:
        filename = '{}.webp'.format(m.ranking)
        get(m.cover_url, filename)


def movies_from_url(url):
    # https://movie.douban.com/top250?start=100
    filename = '{}.html'.format(url.split('=', 1)[-1])
    page = get(url, filename)

    e = pq(page)
    items = e('.item')

    movies = [movie_from_div(i) for i in items]
    save_cover(movies)
    return movies


def main():
    for i in range(0, 250, 25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        movies = movies_from_url(url)
        print('top250 movies', movies)


def view_sql():
    db_path = 'douban.sqlite'
    db_table = 'top250'

    connection = sqlite3.connect(db_path)
    # print("打开了数据库")

    cursor = select(connection, db_table)
    for i in cursor:
        print(i)

    connection.close()


def delete_sql():
    db_path = 'douban.sqlite'
    db_table = 'top250'
    db_id = 251

    connection = sqlite3.connect(db_path)
    # print("打开了数据库")

    delete(connection, db_table, db_id)

    connection.commit()
    connection.close()


def update_sql():
    db_path = 'douban.sqlite'
    db_table = 'top250'
    db_id = 252
    db_name = 'h1'
    db_other = 'h3'

    connection = sqlite3.connect(db_path)
    # print("打开了数据库")

    update(connection, db_table, db_id, db_name, db_other)

    connection.commit()
    connection.close()


if __name__ == '__main__':
    main()
    # view_sql()
    # delete_sql()
    # update_sql()
