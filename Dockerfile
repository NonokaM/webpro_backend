# FastAPIアプリケーション用のベースイメージ
FROM tiangolo/uvicorn-gunicorn:python3.11-slim

# 必要な依存関係のインストール
# Google Cloud Vision APIクライアントライブラリ
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN pip install google-cloud-vision

# アプリケーションコードのコピー
COPY ./app /app

# デフォルトコマンドの設定
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "3000"]
