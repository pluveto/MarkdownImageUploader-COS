import sys


# 1. get input file
if(len(sys.argv)!=2):
    print("No file inputed.")
    exit()

# 2. try to read file
   
try:
    f = open(sys.argv[1],'rt')
except Exception as e:    
    print(e)
    exit()

contents = f.read()
dictImage = {}

import re
regex = r"!\[.*?]\((\w:\\.*?\.(png|jpg|jpeg|gif|webp))\)"
matches = re.finditer(regex, contents, re.MULTILINE)
local = []
for match in matches:
    print("found: " + match.group(1))
    local.append([match.group(1),match.group(2)])

from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
import os
import logging

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

secret_id = ''      # 替换为用户的 secretId
secret_key = ''      # 替换为用户的 secretKey
region = 'ap-chengdu'     # 替换为用户的 Region
token = None                # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'https'            # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
bucket = 'pluvet-1251765364'
baseUrl = 'https://pluvet-1251765364.cos.ap-chengdu.myqcloud.com/'

config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
client = CosS3Client(config)
import datetime
dateFoler = datetime.date.today().strftime('%Y/%m/')
import uuid
unique_filename = str(uuid.uuid4())
for item in local:
    try:
        with open(item[0], 'rb') as fp:
            filename = "IMAGES/"+dateFoler + unique_filename + "." + item[1];
            response = client.put_object(
                Bucket=bucket,
                Body=fp,
                Key=filename,
                StorageClass='STANDARD',
                EnableMD5=False
            )
            url = baseUrl + filename
            contents=contents.replace(item[0], url)
    except EnvironmentError:
        print("failed with " + item)

filename,type= os.path.splitext(sys.argv[1]) 

newpath = filename + '.out' + type
with open(newpath, "w") as fp:
    fp.write(contents)
    print("OK: " + newpath)
