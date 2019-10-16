import json

from tqdm import tqdm


class DataLoader(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def load_dicts(self):
        # TODO
        with open('data/kkbox/preprocessed/id2entity.dict', 'r', encoding='utf-8') as f:
            self.id2entity = json.loads(f.read())
        with open('data/kkbox/preprocessed/entity2id.dict', 'r', encoding='utf-8') as f:
            self.entity2id = json.loads(f.read())
        with open('data/kkbox/preprocessed/id2type.dict', 'r', encoding='utf-8') as f:
            self.id2type = json.loads(f.read())
        # with open('data/kkbox/preprocessed/id2user.dict', 'r', encoding='utf-8') as f:
        #     self.id2user = json.loads(f.read())
        # with open('data/kkbox/preprocessed/user2id.dict', 'r', encoding='utf-8') as f:
        #     self.user2id = json.loads(f.read())
    
    def load_interactions_directed(self):
        with open('data/kkbox/preprocessed/interactions.txt', 'r', encoding='utf-8') as f:
            self.interactions = set()
            for line in tqdm(f, total=7377420):
                t = line.split()
                self.interactions.add(t)

    def load_kg_triples_directed(self):
        with open('data/kkbox/preprocessed/kg_triples.txt', 'r', encoding='utf-8') as f:
            self.kg_triples = set()
            for line in tqdm(f, total=7377420):
                t = line.split()
                self.kg_triples.add(t)

    def get(self, target_dict:str, item):
        try:
            if (target_dict == 'id2entity'):
                return self.id2entity[str(item)]
            elif (target_dict == 'entity2id'):
                return self.entity2id[str(item)]
            elif (target_dict == 'id2type'):
                return self.id2type[str(item)]
            # elif (target_dict == 'id2user'):
            #     return self.id2user[str(item)]
            # elif (target_dict == 'user2id'):
            #     return self.user2id[str(item)]
            else:
                raise NotImplementedError
        except:
            raise KeyError
