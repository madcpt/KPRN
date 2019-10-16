from utils.config import get_config
from utils.dataloader import DataLoader

cfg = get_config('kkbox')
dataloader = DataLoader(cfg)

dataloader.load_dicts()
