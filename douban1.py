import requests
from pyquery import PyQuery as pq

'''
这是一个普通爬虫,下载网页并解析打印出来
'''


class Model():
    # 基类, 用来显示类的信息
    def __repr__(self):
        name = self.__class__.__name__
        properties = ('{}=({})'.format(k, v) for k, v in self.__dict__.items())
        s = '\n<{} \n  {}>'.format(name, '\n  '.join(properties))
        return s


class Movie(Model):
    # 存储电影信息
    def __init__(self):
        self.name = ''
        self.score = 0
        self.quote = ''
        self.cover_url = ''
        self.ranking = 0


def movie_from_div(div):
    # 从一个 div 里面获取到一个电影信息
    e = pq(div)
    m = Movie()
    m.name = e('.title').text()
    m.score = e('.rating_num').text()
    m.quote = e('.inq').text()
    m.cover_url = e('img').attr('src')
    m.ranking = e('.pic em').text()
    return m


def movies_from_url(url):
    # 从 url 中下载网页并解析出页面内所有的电影
    r = requests.get(url)
    page = r.content

    e = pq(page)
    items = e('.item')

    # 调用 movie_from_div
    movies = [movie_from_div(i) for i in items]
    return movies


def main():
    url = 'https://movie.douban.com/top250'
    movies = movies_from_url(url)
    print('top250 movies', movies)


if __name__ == '__main__':
    main()
