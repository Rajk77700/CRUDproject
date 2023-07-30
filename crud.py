import sqlite3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Create or connect to the database
conn = sqlite3.connect("knowledge_base.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS knowledge_base (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
""")
conn.commit()
conn.close()


def insert_data(title, description):
    conn = sqlite3.connect("knowledge_base.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO knowledge_base (title, description) VALUES (?, ?)", (title, description))

    conn.commit()
    conn.close()

# STORE DATA INTO TABLE;

insert_data("Gulab Jamun", "it is so juicy")
insert_data("Almonds", "it is so healthy ")


# UPDATE DATA
def update_data(id, title, description):
    conn = sqlite3.connect("knowledge_base.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE knowledge_base SET title=?, description=? WHERE id=?", (title, description, id))

    conn.commit()
    conn.close()
update_data(1, "Gulab Jamun", "it is jucy and soft")

# DELETE DATA 
def delete_data(id):
    conn = sqlite3.connect("knowledge_base.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM knowledge_base WHERE id=?", (id,))

    conn.commit()
    conn.close()

delete_data(1)

# FETCH DATA
class KnowledgeBaseHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            data = self.fetch_data()

            response = "<html><body><table border='1'><tr><th>ID</th><th>TITLE</th><th>DESCRIPTION</th></tr>"
            for row in data:
                response += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"
            response += "</table></body></html>"
            self.wfile.write(response.encode())

        else:
            self.send_error(404)

    def fetch_data(self):
        conn = sqlite3.connect("knowledge_base.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM knowledge_base")
        data = cursor.fetchall()

        conn.close()

        return data

def run():
    port = 7080
    server_address = ('', port)
    httpd = HTTPServer(server_address, KnowledgeBaseHandler)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()


# NOTE:-. The server will start running, and you can visit http://localhost:7080