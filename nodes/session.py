import requests
from retry import retry
import boto3
from botocore.config import Config


MAX_RETRY = 3


@retry(tries=MAX_RETRY)
def get_client(service_name, clients={}):
    if service_name in clients:
        return clients[service_name]

    try:
        # ECS タスク実行ロールを使用するための設定
        config = Config(
            retries = dict(
                max_attempts = 3
            )
        )
        
        # コンテナの認証情報を自動的に取得
        clients[service_name] = boto3.client(
            service_name=service_name,
            config=config
        )
        return clients[service_name]
    
    except Exception as e:
        print(f"クライアントの初期化エラー: {str(e)}")
        raise e
