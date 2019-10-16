import json

import yaml
from tqdm import tqdm

# from config import get_config

# cfg = get_config('config/kkbox.yml')

def add_l(entity_dict, item):
    entity_dict[item] = True

############################ load raw-data ##############################

# song_id,song_length,genre_ids,artist_names,composers,lyricist,language
song = {}
genre_ids = {} # 2
artist_names = {}
composers = {}
# lyricist = {}
# language = {}
kg_triples = set()
with open('data/kkbox/songs.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=2300000):
        if is_title:
            is_title = False
        else:
            info = line.split(',')
            add_l(song, info[0])
            add_l(genre_ids, info[2])
            add_l(artist_names, info[3])
            add_l(composers, info[4])
            kg_triples.add((info[0], info[2], info[3], info[4]))
            # add_l(lyricist, info[5])
            # add_l(language, info[6])

users = {}
with open('data/kkbox/members.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=34405):
        if is_title:
            is_title = False
        else:
            info = line.split(',')
            add_l(users, info[0])

# msno,song_id,source_system_tab,source_screen_name,source_type,target
interactions = set()
with open('data/kkbox/train.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=7377420):
        if is_title:
            is_title = False
        else:
            info = line.strip().split(',')
            interactions.add((info[0], info[1], info[-1]))




id2entity = {}
entity2id = {}
id2type = {}
id = 0
for user in users.keys():
    id2entity[id] = user
    entity2id[user] = id
    id2type[id] = 'u'
    id += 1

for entity in song.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 's'
    id += 1

for entity in genre_ids.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 'g'
    id += 1

for entity in artist_names.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 'a'
    id += 1

for entity in composers.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 'c'
    id += 1


############################ save dataset ############################

is_simple = False
if is_simple:
    # save kg_triples
    with open('data/kkbox/kg_triples_simple.txt', 'w', encoding='utf-8') as f:
        for kg_triple in tqdm(kg_triples, total=len(kg_triples)):
            song = str(entity2id[kg_triple[0]])
            genre_id = str(entity2id[kg_triple[1]])
            artist = str(entity2id[kg_triple[2]])
            composer = str(entity2id[kg_triple[3]])
            f.write(song+'\t'+genre_id+'\t'+artist+'\t'+composer+'\n')
else:
    # save kg_triples
    with open('data/kkbox/kg_triples.txt', 'w', encoding='utf-8') as f:
        for kg_triple in tqdm(kg_triples, total=len(kg_triples)):
            song = str(entity2id[kg_triple[0]])
            genre_id = str(entity2id[kg_triple[1]])
            artist = str(entity2id[kg_triple[2]])
            composer = str(entity2id[kg_triple[3]])
            f.write(song+'\t'+genre_id+'\n')
            f.write(song+'\t'+artist+'\n')
            f.write(song+'\t'+composer+'\n')

# save interactions():
with open('data/kkbox/interactions.txt', 'w', encoding='utf-8') as f:
    for triple in tqdm(interactions, total=len(interactions)):
        try:
            user = str(entity2id[triple[0]])
            item = str(entity2id[triple[1]])
            score = triple[2]
            f.write(user+'\t'+item+'\t'+score+'\n')
        except:
            print('Error')

# save_dict():
with open('data/kkbox/id2entity.dict', 'w', encoding='utf-8') as f:
    f.write(json.dumps(id2entity))
with open('data/kkbox/entity2id.dict', 'w', encoding='utf-8') as f:
    f.write(json.dumps(entity2id))
with open('data/kkbox/id2type.dict', 'w', encoding='utf-8') as f:
    f.write(json.dumps(id2type))



# load_dict()
# with open('data/kkbox/id2entity.dict', 'r', encoding='utf-8') as f:
#     id2entity = json.loads(f.read())
# with open('data/kkbox/entity2id.dict', 'r', encoding='utf-8') as f:
#     entity2id = json.loads(f.read())
# with open('data/kkbox/id2type.dict', 'r', encoding='utf-8') as f:
#     id2type = json.loads(f.read())
