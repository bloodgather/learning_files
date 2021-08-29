import json

# 加载配置文件（函数）
def load_config(_file_name: str = "config.json"):
    with open(_file_name, 'r', encoding='utf-8') as config_file:
        config = json.load(config_file)
        return config


load_config()
