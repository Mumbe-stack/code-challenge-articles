class Author:
     def __init__(self, name, id=None):
        self.id = id
        self.name = name
        
     def save(self):
         conn = get_connection()
         cursor = conn.cursor()
         if self.id:
             cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (self.name, self.id))
         else:
             cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
             cursor.execute("SELECT last_insert_rowid()")
             self.id = cursor.fetchone()[0]
             conn.commit()
             conn.close()
        
    
   