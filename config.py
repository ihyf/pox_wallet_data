# coding:utf-8
DEBUG = False

# develop
SQLALCHEMY_DATABASE_URI_SETTINGS = {
    "default": {
        'master': [
            'mysql+pymysql://root:123456@127.0.0.1/pox_wallet?charset=utf8',
        ],
    },

}

REDIS_URL = "redis://:@127.0.0.1:6379/0?charset=utf8&decode_responses=true"


# 服务器上用
SQLALCHEMY_DATABASE_URI_SETTINGS_bak = {
    "default": {
        'master': [
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
        ],
        'slave': [
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
            'mysql+pymysql://root:reinforcement_1000more_needed@47.244.167.66/eth?charset=utf8',
        ]
    },
    # "other": {
    #     'master': [],
    #     'slave': []
    # }
}

REDIS_URL_bak = "redis://:@47.244.167.66:6379/0?charset=utf8&decode_responses=true"


API_TRUST_DOMAIN = ""

# 创建server_db
"create database pox_wallet default character set utf8mb4;"

axe_livenet = "https://insight.axerunners.com/api"
# redis过期时间
redis_expire_time = 60*60*10
# 定时任务间隔
seconds = 60


