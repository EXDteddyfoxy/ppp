import sqlite3
import requests
from bs4 import BeautifulSoup


class Database:
    def init(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS data (title TEXT, content TEXT)')
        self.connection.commit()

    def insert_data(self, title, content):
        self.cursor.execute("INSERT INTO data (title, content) VALUES (?, ?)", (title, content))
        self.connection.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


class WebParser:
    def fetch_page(self, url):
        response = requests.get(url)
        return response.text

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'No Title'
        content = soup.get_text()
        return title, content


class UserInterface:
    def get_url(self):
        return input("Enter URL: ")

    def display(self, data):
        for row in data:
            print(f"Title: {row[0]}\nContent: {row[1]}\n")


def run():
    db = Database('data.db')
    ui = UserInterface()
    parser = WebParser()

    url = ui.get_url()
    html = parser.fetch_page(url)
    title, content = parser.parse(html)

    db.insert_data(title, content)

    print("\nStored data:")
    data = db.fetch_all()
    ui.display(data)

    db.close()

if name == "main":
    run()