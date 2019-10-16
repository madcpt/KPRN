import yaml


def get_config(config_path="config/kkbox.yml"):
    with open(config_path, "r") as setting:
        config = yaml.load(setting, Loader=yaml.FullLoader)
    return config

cfg = get_config()
