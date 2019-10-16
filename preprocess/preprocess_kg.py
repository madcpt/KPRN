import json

import yaml
from tqdm import tqdm

# from config import get_config

# cfg = get_config('config/kkbox.yml')

def add_l(entity_dict, item):
    entity_dict[item] = True


# song_id,song_length,genre_ids,artist_name,composer,lyricist,language
song = {}
genre_ids = {} # 2
artist_name = {}
composer = {}
lyricist = {}
language = {}
with open('data/kkbox/songs.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=2300000):
        if is_title:
            is_title = False
        else:
            info = line.split(',')
            add_l(song, info[0])
            add_l(genre_ids, info[2])
            add_l(artist_name, info[3])
            add_l(composer, info[4])
            add_l(lyricist, info[5])
            add_l(language, info[6])

users = {}
with open('data/kkbox/members.csv', 'r', encoding='utf-8') as f:
    is_title = True
    for line in tqdm(f, total=34405):
        if is_title:
            is_title = False
        else:
            info = line.split(',')
            add_l(users, info[0])


id2entity = {}
entity2id = {}
id2type = {}
id = 0
for user in users.keys():
    id2entity[id] = user
    entity2id[user] = id
    id2type[id] = 'u'
    id += 1

print(id)
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

for entity in artist_name.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 'a'
    id += 1

for entity in composer.keys():
    id2entity[id] = entity
    entity2id[entity] = id
    id2type[id] = 'c'
    id += 1

# 2961126+34403-2851220
# len(song)+len(genre_ids)+len(artist_name)+len(composer)+len(lyricist)+len(language)

# song_id,name,isrc
# with open('data/kkbox/song_extra_info.csv', 'r', encoding='utf-8') as f:
#     is_title = True
#     for line in tqdm(f, total=2296871):
#         if is_title:
#             is_title = False
#         else:
#             info = line.strip().split(',')
#             break


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
