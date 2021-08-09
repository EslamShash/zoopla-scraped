# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class ZooplaPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('zoopla.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS zoopla""")
        self.curr.execute("""CREATE TABLE zoopla(
            title text,
            address text,
            price text,
            seller text,
            phone text,
            bedrooms text,
            toilets text,
            chairs text,
            date_listed text,
            url text
        )""")
    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""INSERT INTO zoopla VALUES(?,?,?,?,?,?,?,?,?,?)""",(
            item['title'],
            item['address'],
            item['price'],
            item['seller'],
            item['phone'],
            item['bedrooms'],
            item['toilets'],
            item['chairs'],
            item['date_listed'],
            item['url']
        ))
        self.conn.commit()
