import json

from tqdm import tqdm


def add_l(entity_dict, item):
    entity_dict[item] = True


# msno,song_id,source_system_tab,source_screen_name,source_type,target

triples = []
with open('data/kkbox/train.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=7377420):
        if is_title:
            is_title = False
        else:
            info = line.strip().split(',')
            triples.append((info[0], info[1], info[-1]))

# save triples():
with open('data/kkbox/interactions.txt', 'w', encoding='utf-8') as f:
    for triple in tqdm(triples, total=7377420):
        f.write(triple[0]+'\t'+triple[1]+'\t'+triple[2]+'\n')


# load_dict()
# with open('data/kkbox/id2user.dict', 'r', encoding='utf-8') as f:
#     id2user = json.loads(f.read())
# with open('data/kkbox/user2id.dict', 'r', encoding='utf-8') as f:
#     user2id = json.loads(f.read())
