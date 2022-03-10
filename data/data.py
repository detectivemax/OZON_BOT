import sqlite3

connect = sqlite3.connect('../data_papa.db')
cursor = connect.cursor()

# User_stage
cursor.execute("""CREATE TABLE IF NOT EXISTS user_stage(
        user_id INTEGER,
        stage_one TEXT,
        stage_two TEXT,
        stage_three TEXT
    )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS post_status_info(
        post_id INTEGER,
        date TEXT,
        time TEXT,
        type TEXT
)""")