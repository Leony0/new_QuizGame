import sqlite3

quiz_question = [
    [1, 'ゲーム市場、最も売れたゲーム機は次のうちどれ？'],
    [2, '糸井重里が企画に関わった、任天堂の看板ゲームといえば？'],
    [3, 'ファイナルファンタジーⅣの主人公の名前は？']
]

quiz_answer = [
    [1, 'スーパーファミコン', "False", 1],
    [2, 'プレイステーション', "False", 1],
    [3, 'ニンテンドースイッチ', "False", 1],
    [4, 'ニンテンドーDS', "True", 1],

    [5, 'MOTHER2', "True", 2],
    [6, 'スーパーマリオブラザーズ3', "False", 2],
    [7, 'スーパードンキーコング', "False", 2],
    [8, '星のカービィ', "False", 2],

    [9, 'フリオニール', "False", 3],
    [10, 'クラウド', "False", 3],
    [11, 'ティーダ', "False", 3],
    [12, 'セシル', "True", 3]
]

dbFile = 'test.db'

# 1. データベースに接続
con = sqlite3.connect(dbFile)

# 2. sqliteを操作するカーソルオブジェクトを作成
cur = con.cursor()

# 3. CREATE文を実行してテーブルを作成
cur.execute("""
CREATE TABLE IF NOT EXISTS question (
    question_id INTEGER PRIMARY KEY, 
    q_content TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS choice (
    id INTEGER PRIMARY KEY, 
    content TEXT, 
    is_answer TEXT, 
    question_id INTEGER,
    FOREIGN KEY (question_id) REFERENCES question(question_id)
)
""")

# 4. データの挿入（quiz_question と quiz_answer を挿入）
q_sql = "INSERT INTO question (question_id, q_content) VALUES (?, ?)"
a_sql = "INSERT INTO choice (id, content, is_answer, question_id) VALUES (?, ?, ?, ?)"

# quiz_questionのデータを挿入
cur.executemany(q_sql, quiz_question)

# quiz_answerのデータを挿入
cur.executemany(a_sql, quiz_answer)

# 5. データベースに情報をコミット
con.commit()

# 6. データベースの接続を切断
cur.close()
con.close()

print("データベースへの挿入が完了しました。")
