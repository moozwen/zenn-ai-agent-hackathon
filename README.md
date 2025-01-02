# AI Agent Hackathon Project

このプロジェクトは、PDFファイルのセキュリティチェックを行うAIエージェントシステムのPoCです。

## 概要

- PDFファイルのアップロードと自動セキュリティ判定を行うシステム
- ルールベースの判定により「危険」「グレー」「安全」の3段階で評価
- 将来的なAIエージェントによる高度な判定機能の実装を見据えた設計

## 技術スタック

- Python 3.11
- バックエンド: FastAPI
- フロントエンド: Streamlit
- インフラ: Google Cloud Platform
  - Cloud Run
  - Vertex AI Search
  - Cloud Storage

## 主な機能

- PDFファイルのアップロード
- ルールベースのセキュリティ判定
- 判定結果の表示
- Cloud Storageへのファイル保存

## 開発環境のセットアップ

1. Google Cloud CLIのセットアップと認証
```bash
# Google Cloudプロジェクトの初期化
gcloud init

# アプリケーションデフォルト認証情報の設定
gcloud auth application-default login
```

2. Pythonのバージョン設定
```bash
python -V  # Python 3.11以上であることを確認
```

3. 依存関係のインストール
```bash
uv sync
```

4. 環境変数の設定
```bash
cp .env.example .env
# .envファイルに必要な環境変数を設定
```

## 開発用コマンド

```bash
# バックエンドの起動
make api
```

## プロジェクト構造

```
.
├── src/
│   ├── api/        # FastAPI バックエンド
│   ├── web/        # Streamlit フロントエンド
│   └── agents/     # AIエージェント関連のコード
├── docs/           # ドキュメント
└── tests/          # テストコード
```

## その他

このプロジェクトはハッカソン向けのPoCとして開発されています。
