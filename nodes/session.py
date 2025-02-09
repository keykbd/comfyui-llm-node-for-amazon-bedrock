import boto3
from botocore.config import Config

MAX_RETRY = 3

def get_client(service_name, clients={}):
    if service_name in clients:
        return clients[service_name]

    try:
        # 固定のリージョンを使用
        config = Config(
            region_name='us-east-1',  # デフォルトリージョン
            retries=dict(
                max_attempts=3
            )
        )
        
        # クライアントを初期化
        clients[service_name] = boto3.client(
            service_name=service_name,
            config=config
        )
        return clients[service_name]
        
    except Exception as e:
        print(f"クライアントの初期化エラー: {str(e)}")
        raise e
