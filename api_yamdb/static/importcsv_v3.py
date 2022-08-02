import csv
import sqlite3

# База данных
DATABASE = 'C:/Dev/api_yamdb/api_yamdb/db.sqlite3'

# Файлы с данными
USERS = 'C:/Dev/api_yamdb/api_yamdb/static/data/users.csv'
CATEGORY = 'C:/Dev/api_yamdb/api_yamdb/static/data/category.csv'
TITLES = 'C:/Dev/api_yamdb/api_yamdb/static/data/titles.csv'
REVIEWS = 'C:/Dev/api_yamdb/api_yamdb/static/data/review.csv'
COMMENTS = 'C:/Dev/api_yamdb/api_yamdb/static/data/comments.csv'
GENRE = 'C:/Dev/api_yamdb/api_yamdb/static/data/genre.csv'
GENRE_TITLE = 'C:/Dev/api_yamdb/api_yamdb/static/data/genre_title.csv'

dbtables = {
    USERS: 'reviews_user',
    CATEGORY: 'reviews_category',
    TITLES: 'reviews_title',
    REVIEWS: 'reviews_review',
    COMMENTS: 'reviews_comment',
    GENRE: 'reviews_genre',
    GENRE_TITLE: 'reviews_genre_title'
}

# Подключение к БД
con = sqlite3.connect(DATABASE)
cur = con.cursor()


def get_query(Dict: dict, table: str) -> str:
    """Функция получает словарь и возвращает нужный sql запрос."""
    query1 = f'INSERT INTO {table} ('
    query2 = 'VALUES ('
    i = 1
    for key in Dict:
        if i == len(Dict):
            query1 += f'{key})'
            query2 += str("'" + f'{Dict[key]}' + "')")
        else:
            query1 += f'{key}, '
            query2 += str("'" + f'{Dict[key]}' + "', ")
            i += 1
    return f'{query1} {query2}'


try:
    for staticfile in dbtables:
        with open(staticfile, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sqlquery = get_query(row, dbtables[staticfile])
                cur.execute(sqlquery)
    print('Ура! Данные успешно загружены!')
except Exception as error:
    print(f'Ошибка загрузки данных! {error}')

con.commit()
con.close()
