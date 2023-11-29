# FastAPIアプリケーション用のベースイメージ
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

# 必要な依存関係のインストール
# Google Cloud Vision APIクライアントライブラリ
RUN pip install google-cloud-vision

# アプリケーションコードのコピー
COPY ./app /app

# デフォルトコマンドの設定
CMD ["uvicorn", "main:app", "--reload", "--host", "127.0.0.0", "--port", "3000"]
