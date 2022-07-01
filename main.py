import json
from flask import Flask, g, request   
import firebase_admin
from firebase_admin import firestore    

# dbpath = 'test.db' #テーブルを保存するファイル
app = Flask(__name__)

def get_db(request):#データベースのコネクションを取得
    # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
    if len(firebase_admin._apps) == 0:
        # アプリを初期化する
        default_app = firebase_admin.initialize_app()
    db = firestore.client()
    
    return db 


@app.route('/users', methods=['GET'])
def get_user(request):
    con = get_db() #コネクションを取得
    docs = con.collection('users').get()
    users_list = []
    for doc in docs:
        users_list.append(doc.to_dict())
    return_json = json.dumps({"users": users_list}, ensure_ascii=False)

    return return_json


@app.route('/users', methods=['POST'])
def create_data(request):
    con = get_db() #コネクションを取得
    
    # 新しいユーザーの追加
    user = request.json["user"] #POSTメソッド のデータを取得
    con.collection('users').add(user)

    # 既存ユーザーの情報追加
    # item = ({"name": "太郎","age": "26","sex": "Male"})
    # db.collection('users').document('CB1KCDj7CkWGv23IEt4R').set(item)
    
    # ブラウザに見せるために返す
    return f'Create User!'


@app.route('/users/<id>', methods=['PUT'])
def update_data(id):
    con = get_db() #コネクションを取得
    
    user_items = request.json["user_items"] #POSTメソッド のデータを取得
    # 既存ユーザーの情報更新
    con.collection('users').document({id}).update({user_items})
    
    # ブラウザに見せるために返す
    return f'Update Data!'


@app.route('/users/<id>', methods=['DELETE'])
def delete_data(id):
    con = get_db() #コネクションを取得
    
    # 既存ユーザーの情報更新
    con.collection('users').document({id}).delete()
    
    # ブラウザに見せるために返す
    return f'Delete Data!'


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=80)
