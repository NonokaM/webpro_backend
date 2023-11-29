# FastAPIアプリケーション用のベースイメージ
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

# 必要な依存関係のインストール
# Google Cloud Vision APIクライアントライブラリ
RUN pip install google-cloud-vision

# OpenAI のパッケージをインストール
RUN pip install openai

# アプリケーションコードのコピー
COPY ./app /app

# デフォルトコマンドの設定
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]
