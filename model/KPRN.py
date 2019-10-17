import torch
from torch import nn


class KPRN(nn.Module):
    def __init__(self, entity_size, relation_size, embed_dim, 
                rnn_hidden_size, rnn_num_layers, linear_hidden_size, *args):
        super(KPRN, self).__init__(*args)

        self.entity_size = entity_size
        self.relation_size = relation_size
        self.embed_dim = embed_dim
        self.rnn_hidden_size = rnn_hidden_size
        self.rnn_num_layers = rnn_num_layers
        self.linear_hidden_size = linear_hidden_size

        self.entity_embedding = nn.Embedding(entity_size, embed_dim)
        self.relation_embedding = nn.Embedding(relation_size, embed_dim)

        self.memory_layer = nn.LSTM(embed_dim*3, rnn_hidden_size, rnn_num_layers)
        
        self.project_layer = nn.Sequential(
            nn.Linear(embed_dim*3, linear_hidden_size),
            nn.ReLU(),
            nn.Linear(linear_hidden_size, 1)
        )

        # self.pooling_layer = nn.AvgPool1d()

    def forward(self, *input):
        return super().forward(*input)

if __name__ == "__main__":
    net = KPRN(entity_size=100, relation_size=10, embed_dim=20, rnn_hidden_size=10,
                rnn_num_layers=2, linear_hidden_size=5)
    print(net)
