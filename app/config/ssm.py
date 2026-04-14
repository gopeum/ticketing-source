import boto3
from functools import lru_cache

ssm = boto3.client("ssm", region_name="ap-northeast-2")


@lru_cache
def get_parameter(name: str):
    return ssm.get_parameter(Name=name, WithDecryption=True)["Parameter"]["Value"]