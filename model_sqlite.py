"""
将清洗后的数据，通过下列函数写入、读取、删除和修改到数据库
"""


def create(conn, table):
    sql_create = '''
    CREATE TABLE IF NOT EXISTS {}(
        `id`        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        `name`      TEXT NOT NULL UNIQUE,
        `other`     TEXT NOT NULL,
        `score`     INTEGER NOT NULL,
        `quote`     TEXT NOT NULL,
        `cover_url` TEXT NOT NULL,
        `ranking`   INTEGER NOT NULL
    )
    '''.format(table)
    conn.execute(sql_create)
    # print('创建成功')


def insert(conn, table, name, other, score, quote, cover_url, ranking):
    sql_insert = '''
    INSERT INTO
        {}(`name`,`other`,`score`, `quote`, `cover_url`, `ranking`)
    VALUES
        (?, ?, ?, ?, ?, ?);
    '''.format(table)
    conn.execute(sql_insert, (name, other, score, quote, cover_url, ranking))
    # print('插入数据成功')


def select(conn, table):
    sql = '''
    SELECT
        `name`, other, score, quote, cover_url, ranking
    FROM
        {}
    '''.format(table)
    cursor = conn.execute(sql)
    # print('读取数据')
    return cursor


def delete(conn, table, user_id):
    sql_delete = '''
    DELETE FROM
        {}
    WHERE
        id=?
    '''.format(table)
    conn.execute(sql_delete, (user_id,))
    # print('删除数据')


def update(conn, table, user_id, name, other):
    sql_update = '''
    UPDATE
        {}
    SET
        `name`=?, other=? 
    WHERE
        `id`=?
    '''.format(table)
    conn.execute(sql_update, (name, other, user_id))
    # print('修改数据')
