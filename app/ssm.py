import boto3
from functools import lru_cache

ssm = boto3.client("ssm", region_name="ap-northeast-2")


@lru_cache()
def get_ssm_parameter(name: str, with_decryption: bool = False) -> str:
    response = ssm.get_parameter(
        Name=name,
        WithDecryption=with_decryption
    )
    return response["Parameter"]["Value"]