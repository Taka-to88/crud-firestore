import json
from flask import Flask, g, request   
import firebase_admin
from firebase_admin import firestore    

# dbpath = 'test.db' #テーブルを保存するファイル

def crud_db(request):
    app = Flask(__name__)

    # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
    if len(firebase_admin._apps) == 0:
        # アプリを初期化する
        default_app = firebase_admin.initialize_app()
    db = firestore.client()
        

    @app.route('/', methods=['GET'])
    def get_user():        
        docs = con.collection('users').get()
        users_list = []
        for doc in docs:
            users_list.append(doc.to_dict())
        return_json = json.dumps({"users": users_list}, ensure_ascii=False)

        return return_json


    @app.route('/', methods=['POST'])
    def create_data():
        # 新しいユーザーの追加
        name = request.form["name"] #POSTメソッド のデータを取得
        password = request.form["password"]
        email = request.form["email"]
        user = ({'name': name, 'password': password, 'email':email})
        db.collection('users').add({user})

        # 既存ユーザーの情報追加
        # item = ({"name": "太郎","age": "26","sex": "Male"})
        # db.collection('users').document('CB1KCDj7CkWGv23IEt4R').set(item)
        
        # ブラウザに見せるために返す
        return f'Create User!'


    @app.route('/<id>', methods=['PUT'])
    def update_data(id):
        #PUTメソッド のデータを取得
        name = request.form["name"] #PUTメソッド のデータを取得
        password = request.form["password"]
        email = request.form["email"]
        user_item = ({'name': name, 'password': password, 'email':email})
        # 既存ユーザーの情報更新
        db.collection('users').document({id}).update({user_items})
        
        # ブラウザに見せるために返す
        return f'Update Data!'


    @app.route('/<id>', methods=['DELETE'])
    def delete_data(id):
        # 既存ユーザーの情報更新
        db.collection('users').document({id}).delete()
        
        # ブラウザに見せるために返す
        return f'Delete Data!'

