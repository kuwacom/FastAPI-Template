from fastapi import APIRouter
from .hello import helloRouter

# v1ルーターを作成
v1Router = APIRouter()
# プレフィックスを設定
prefix = '/v1'

v1Router.include_router(helloRouter, prefix=prefix)