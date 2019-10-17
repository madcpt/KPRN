import json

from tqdm import tqdm


class DataLoader(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def load_dicts(self):
        # TODO
        with open('data/kkbox/filtered/id2entity.dict', 'r', encoding='utf-8') as f:
            id2entity = json.loads(f.read())
            self.id2entity = {int(k):v for k,v in id2entity.items()}
        with open('data/kkbox/filtered/entity2id.dict', 'r', encoding='utf-8') as f:
            entity2id = json.loads(f.read())
            self.entity2id = {k:int(v) for k,v in entity2id.items()}
        with open('data/kkbox/filtered/id2type.dict', 'r', encoding='utf-8') as f:
            id2type = json.loads(f.read())
            self.id2type = {int(k):v for k,v in id2type.items()}
        # with open('data/kkbox/preprocessed/id2user.dict', 'r', encoding='utf-8') as f:
        #     self.id2user = json.loads(f.read())
        # with open('data/kkbox/preprocessed/user2id.dict', 'r', encoding='utf-8') as f:
        #     self.user2id = json.loads(f.read())
    
    def load_interactions_directed(self):
        with open('data/kkbox/filtered/interactions.txt', 'r', encoding='utf-8') as f:
            self.interactions = []
            for line in tqdm(f, total=7377420):
                t = line.split()
                self.interactions.append((int(t[0]), int(t[1]), int(float(t[2]))))

    def load_kg_triples_directed(self):
        with open('data/kkbox/filtered/kg_triples.txt', 'r', encoding='utf-8') as f:
            self.kg_triples = []
            for line in tqdm(f, total=4593666):
                t = line.split()
                self.kg_triples.append((int(t[0]), t[1], int(t[2])))

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
