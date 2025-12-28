# Worklog App（作業ログ管理アプリ）

FastAPI + SQLite を用いた、シンプルな作業ログ管理 Web アプリケーションです。  
Python による Web アプリ開発の基礎構造と、CRUD 処理を理解・説明できるようになることを目的として作成しました。

---

## 📌 概要

日々の作業内容を記録し、一覧・詳細表示・削除ができる Web アプリです。  
UI は Bootstrap を用いて最低限の実務的な見た目に整えています。

---

## ✨ 機能

- 作業ログの追加
- 作業ログの一覧表示
- 作業ログの詳細表示
- 作業ログの削除
- SQLite によるデータ永続化

---

## 🛠 使用技術

- **Python**
- **FastAPI**（Web フレームワーク）
- **Jinja2**（HTML テンプレート）
- **SQLite**（軽量データベース）
- **Bootstrap 5**（UI）
- **Git / GitHub**

---

## 📂 ディレクトリ構成

```text
worklog-app/
├─ main.py              # ルーティング・DB操作
├─ templates/
│   ├─ index.html       # 一覧画面
│   └─ detail.html      # 詳細画面
├─ .gitignore           # Git 管理除外設定
└─ README.md
🚀 起動方法
1. ライブラリのインストール
bash
コードをコピーする
pip install fastapi uvicorn jinja2
2. アプリ起動
bash
コードをコピーする
uvicorn main:app --reload
3. ブラウザでアクセス
cpp
コードをコピーする
http://127.0.0.1:8000/
※ SQLite の DB ファイルは起動時に自動生成されます。

🧠 学習ポイント
本アプリを通じて、以下の点を重点的に学習しました。

FastAPI による Web アプリの基本構成

GET / POST を分けたルーティング設計

PRG パターン（POST → Redirect → GET）の実装

SQLite を用いた永続化処理

CRUD（Create / Read / Delete）の考え方

.gitignore を用いた GitHub 運用の基本

💡 補足
データベースファイル（.db）は GitHub には含めていません

実務での拡張を想定し、構造はシンプルに保っています

📈 今後の改善予定
編集機能（UPDATE）の追加

ユーザー認証機能の実装

フォルダ構成の分割（router / service / db）

クラウドへのデプロイ

👤 Author
Shoma Yoshida

yaml
コードをコピーする

---

### 次にやること（30秒）

```powershell
git add README.md
git commit -m "Update README for portfolio"
git push
