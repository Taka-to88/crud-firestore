import json
from flask import request
import firebase_admin
from firebase_admin import firestore

# dbpath = 'test.db' #テーブルを保存するファイル


def crud_db():

    if request.method == 'GET':
        db = firestore.Client()
        docs = db.collection('company').get()
        users_list = []
        for doc in docs:
            users_list.append(doc.to_dict())
        return_json = json.dumps({"users": users_list}, ensure_ascii=False)

        return return_json

    if request.method == 'POST':
        # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
        if len(firebase_admin._apps) == 0:
            # アプリを初期化する
            default_app = firebase_admin.initialize_app()
        db = firestore.client()

        # 新しいユーザーの追加
        user = ({'name': 'ジョニオ', 'age': '89', 'birthplace': 'アメリカ'})
        db.collection('users').add(user)

        # # 既存ユーザーの情報追加
        # item = ({"name": "太郎","age": "26","sex": "Male"})
        # db.collection('users').document('CB1KCDj7CkWGv23IEt4R').set(item)

        # ブラウザに見せるために返す
        return f'Create Data!'

    if request.method == 'PUT':
        # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
        if len(firebase_admin._apps) == 0:
            # アプリを初期化する
            default_app = firebase_admin.initialize_app()
        db = firestore.client()
        # PUTメソッド のデータを取得
        user_id = request.form["id"]
        name = request.form["name"]  # PUTメソッド のデータを取得
        password = request.form["password"]
        email = request.form["email"]
        user_item = ({'name': name, 'password': password, 'email': email})
        # 既存ユーザーの情報更新
        db.collection('users').document(user_id).update(user_item)

        # ブラウザに見せるために返す
        return f'Update Data!'

    if request.method == 'DELETE':
        # 初期化済みのアプリが存在しないか確認する。※複数アプリの初期化はエラーです。的な例外に遭遇したので入れたif文
        if len(firebase_admin._apps) == 0:
            # アプリを初期化する
            default_app = firebase_admin.initialize_app()
        db = firestore.client()

        # 既存ユーザーの情報更新
        user_id = request.form["id"]  # PUTメソッド のデータを取得
        db.collection('users').document(user_id).delete()

        # ブラウザに見せるために返す
        return f'Delete Data!'
