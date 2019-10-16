source_system_tab = []
source_type = []
with open('data/kkbox/train.csv') as f:
    for i in range(10):
        line = f.readline().strip().split(',')
        if line[3] not in source_system_tab:
            source_system_tab.append(line[3])
        if line[4] not in source_type:
            source_type.append(line[4])

# with open('data/kkbox/test.csv') as f:
#     cnt2 = f.readlines()

song_extra_info = {}
with open('data/kkbox/song_extra_info.csv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        info = line.split(',')
        song_extra_info[info[0]] = info[1]

with open('data/kkbox/members.csv') as f:
    for i in range(10):
        line = f.readline().strip().split(',')
        print(line)

with open('data/kkbox/train.csv') as f:
    for i in range(10):
        line = f.readline().strip().split(',')
        print(line[1] in song_extra_info.keys())


def add_l(entity_dict, item):
    entity_dict[item] = True

from tqdm import tqdm

genre_ids = {} # 2
artist_name = {}
composer = {}
lyricist = {}
with open('data/kkbox/songs.csv', 'r', encoding='utf-8') as f:
    for line in tqdm(f, total=2300000):
        info = line.split(',')
        add_l(genre_ids, info[2])
        add_l(artist_name, info[3])
        add_l(composer, info[4])
        add_l(lyricist, info[5])

len(genre_ids) + len(artist_name) + len(composer) + len(lyricist) + 2296833

len(genre_ids) + len(artist_name) + len(composer) + len(lyricist) + 2296833

2851220-2296833
