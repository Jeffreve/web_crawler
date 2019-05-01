![img](https://github.com/Jeffreve/web_crawler/blob/master/crawler.gif)

## douban1.py
通过 python 的 requests、pyquery库 实现页面 信息的清洗和处理
将处理过的数据，通过类实例化，再打印出来


## douban2.py
在douban1的基础上，先将页面信息进行保存，再进行处理，以便下次使用

## douban3.py
在douban2的基础上，对清洗后的数据，通过数据库对数据进行操作

## browser.py
python 使用 splinter 通过 api 来控制 chrome
实例为控制浏览器搜索，并检索页面信息


## zhihu.py
通过配置 cookie，访问用户的知乎首页；
并不断的进行下拉，来检索页面信息
