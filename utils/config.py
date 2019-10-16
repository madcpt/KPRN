import yaml


def get_config(dataset="kkbox"):
    with open('config/'+dataset+'.yml', "r") as setting:
        config = yaml.load(setting, Loader=yaml.FullLoader)
    return config
