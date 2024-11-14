import sqlite3


# データベースファイルに接続
conn = sqlite3.connect('test.db')

# カーソルを取得してクエリを実行
cursor = conn.cursor()
cursor.execute("SELECT * FROM question;")

# 結果を取得して表示
rows = cursor.fetchall()
for row in rows:
    print(row)
    
# 接続を閉じる
conn.close()
