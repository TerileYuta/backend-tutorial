# Karynos-Backend-Tutorial

このリポジトリは下記のツールの使い方を簡単に理解するために、学校の生徒情報をデータベースで管理するAPIを開発するチュートリアル教材です。

- docker-compose
- GitHub 
- FastAPI
- SQLAlchemy

## ツール概要

### docker-compose

Docker Compose は、複数の Docker コンテナをまとめて構成・管理するツールです。今回は`API (FastAPI)`と`DB (PostgreSQL)`の2つのDokcerファイルをdocker-composeで起動させます。

### GitHub

GitHub は、ソースコードを保存・共有・管理できるWebサービスです。

### FastAPI

FastAPI は、Python で API（サーバーの入り口）を作るためのフレームワークです。

### SQLAlchemy

SQLAlchemy は、Python から データベース（PostgreSQLなど）を操作するためのライブラリです。

## 目標

- `docker-compose`でDockerを起動できるようになる
- `GitHub`で`push`,`pull request`などが送れるようになる
- `FastAPI`でAPIのルーティング処理などができるようになる
- `SQLAlchemy`でCURD操作を行えるようになる

## フォルダ構成

```
Backend-tutorial/          
│
│  *.env                     # 環境変数を定義するファイル（DBのURLや秘密鍵などを格納）
│  *.gitignore               # Gitで追跡しないファイルやフォルダの一覧
│  *docker-compose.yml       
│  *Dockerfile               
│  *README.md                
│  *requirements.txt         # 必要なPythonパッケージ一覧
│
└─app/                      
    │  *config.py            # 設定情報の読み込み
    │  crud.py              # DB操作（Create, Read, Update, Delete）をまとめた処理
    │  *db.py                # DB接続とSession管理（SQLAlchemyの設定）
    │  *init_db.py           # 初期データ投入やテーブル作成など、初期化処理
    │  main.py              # アプリのエントリーポイント（FastAPIのルーティングや起動処理）
    │  *model.py             # SQLAlchemyのORMモデル（テーブル定義）を記述するファイル
    │
    └─schemas/              
            StudentsSchema.py  # スキーマを管理
```

## 環境構築方法

```
git clone 
cd 
docker-compose up -d --build
docker-compose exec app bash
python init_db.py
```

## Dockerの起動方法
```
docker-compose up -d
```

## システム設計

### APIルーティング

| Method / Path | Explaining | Parameter | Return |
|---------------|------------|---------|--------|
| `GET /student` | すべての生徒の情報を取得する | `None` | `{ <id> : {"name": <name>, "grade" : <grade>}, ・・・}` | 
| `POST /student` | 新しく生徒の情報を追加する | `{ "name": <name>, "grade" : <grade>}` | `None` | 
| `PUT /student/{id}` | `{id}`の生徒の情報を更新する | `{ "name": <name>, "grade" : <grade>}`| `None` | 
| `DELETE /student/{id}` | `{id}`の生徒の情報を削除する | `None`| `None` | 



## タスク

本チュートリアルでは学生の情報をDBで管理しAPIを用いて操作ができるようなサービスを開発します。
本チュートリアルでは大きく下記の項目の実装を行う必要があります。

- APIのルーティング
- CRUD機能の実装
- APIルーティングとCRUDの接続

## 開発手順

### 1. 用意されているものの把握

docker-composeでコンテナを立ち上げると下記の２つコンテナが立ち上がります。

- app：このコンテナはFastAPIが自動で作動しているコンテナでAPIサーバーの役割を果たします。
- db：データベースサーバーの役割を果たします。コンテナが立ち上がるとPotgreSQLが自動で起動します。

事前に`app`ディレクトリ内には開発で使用するファイルがいくつか用意されています。それぞれの役割についてはディレクトリ構成を見てください。なお、`*`がついているファイルについては内容を変更しないでください。
　　
### 2. APIのルーティング設定

タスクの１つ目「APIのルーティング」を行う前に、下記２つの動画を確認してAPIとFastAPIについて把握してください。

- [APIとは](https://www.youtube.com/watch?v=HqvcmkFjVnw)

- [FastAPI入門](https://www.youtube.com/watch?v=kZHdC-_yPgI)


動画を見たら、早速APIのルーティングの実装に移ります。
APIのルーティングは`main.py`に記載します。ルーティングの設計については`システム設計`を確認してください。

### 3. CRUDの設定

APIの実装が終わったらCRUDの実装に移ります。CRUDとSQLALchemyの知識を得るために下記の動画見てください。

- [CRUDとは](https://www.youtube.com/watch?v=RBkygFVkaos)
- [SQLAlchemy](https://www.youtube.com/watch?v=6aD024WZfCs)

動画を見たら、CRUD機能の実装に移ります。CRUD機能は`crud.py`に記載します。なお、`engine`などの定義は事前に用意されたコードでされているので、`init_db.py`を参考にして作成してください。

### 4. CRUDとAPIの接続

エンドポイントに対してリクエストを送った際にシステム設計通りの挙動をするようにしてください。