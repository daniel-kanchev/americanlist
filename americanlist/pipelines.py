from itemadapter import ItemAdapter
import sqlite3


class DatabasePipeline:
    # Database setup
    conn = sqlite3.connect('banks.db')
    c = conn.cursor()

    def open_spider(self, spider):
        self.c.execute(""" CREATE TABLE IF NOT EXISTS banks (
        name text, 
        locations text, 
        hq text, 
        website text
        ) """)

    def process_item(self, item, spider):
        print(f"Bank Added: {item['name']}")

        # Insert values
        self.c.execute("INSERT INTO banks ("
                       "name, "
                       "locations, "
                       "hq, "
                       "website)"
                       " VALUES (?,?,?,?)",
                       (item.get('name'),
                        item.get('locations'),
                        item.get('hq'),
                        item.get('website')
                        ))
        self.conn.commit()  # commit after every entry

        return item

    def close_spider(self, spider):
        self.conn.commit()
        self.conn.close()

