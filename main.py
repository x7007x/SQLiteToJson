import sqlite3
import json

def convert_db_to_json(db_path, json_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    data = {}
    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f"SELECT * FROM {table_name}")
        
        columns = [description[0] for description in cursor.description]
        
        rows = cursor.fetchall()
        
        data[table_name] = [dict(zip(columns, row)) for row in rows]
    
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    conn.close()
    print(f"تم تحويل قاعدة البيانات بنجاح إلى {json_path}")

convert_db_to_json("database.db", "output.json")
