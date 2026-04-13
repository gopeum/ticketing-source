import boto3
import time
from functools import lru_cache

REGION = "ap-northeast-2"
CACHE_TTL = 300  # 5분 캐싱

_ssm_client = boto3.client("ssm", region_name=REGION)

_cache = {}
_cache_expiry = {}


def _get_from_aws(name: str) -> str:
    response = _ssm_client.get_parameter(
        Name=name,
        WithDecryption=True
    )
    return response["Parameter"]["Value"]


def get_parameter(name: str) -> str:
    now = time.time()

    # 캐시 hit
    if name in _cache and _cache_expiry[name] > now:
        return _cache[name]

    # AWS 호출
    value = _get_from_aws(name)

    # 캐시 저장
    _cache[name] = value
    _cache_expiry[name] = now + CACHE_TTL

    return value