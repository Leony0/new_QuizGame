import sqlite3

quiz_question=(
    ["1",'ゲーム市場、最も売れたゲーム機は次のうちどれ？'],
    ["2",'糸井重里が企画に関わった、任天堂の看板ゲームといえば？'],
    ["3",'ファイナルファンタジーⅣの主人公の名前は？']
)

quiz_answer=(
    ["1",'スーパーファミコン',"False","1",],
    ["2",'プレイステーション',"False","1"],
    ["3",'ニンテンドースイッチ',"False","1"],
    ["4",'ニンテンドーDS',"True","1"],

    ["5",'MOTHER2',"True","2"],
    ["6",'スーパーマリオブラザーズ3',"False","2"],
    ["7",'スーパードンキーコング',"False","2"],
    ["8",'星のカービィ',"False","2"],

    ["9",'フリオニール',"False","3",],
    ["10",'クラウド',"False","3"],
    ["11",'ティーダ',"False","3",],
    ["12",'セシル',"True","3"]
)

dbFile = 'test.db'
# 1.データベースに接続
con = sqlite3.connect(dbFile)

# 2.sqliteを操作するカーソルオブジェクトを作成
cur = con.cursor()

# 3.CREATE文を実行
cur.execute("""CREATE TABLE question(question_id, q_content)""")
cur.execute("""CREATE TABLE choice(id, content, is_answer, question_id)""")

# 4.データベースに情報をコミット
con.commit()

q_sql = "INSERT INTO question VALUES(?, ?)"
a_sql = "INSERT INTO question VALUES(?, ?, ? ,?)"
cur.execute(q_sql, quiz_question)
cur.execute(a_sql, quiz_answer)


# 4.データベースの接続を切断
cur.close()
con.close()
