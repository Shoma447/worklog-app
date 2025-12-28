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
