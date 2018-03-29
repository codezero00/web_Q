import torch
from torch import nn, optim

n_word = 67077
context_size = 400       # 语句最大长度 文章长度 word为120 char为250
embedding_dim = 256      # embedding维度
content_dim = 200        # 文本的卷积核数
num_classes = 372        # 372个分类
linear_hidden_size = 373  # 全连接层隐藏元数目



###################################模型########################################

kernel_sizes = [1, 2, 3, 4]

class MultiCNNTextBNDeep(nn.Module):
    def __init__(self, vocab_size, embedding_dim, content_dim, linear_hidden_size, num_classes):
        super(MultiCNNTextBNDeep, self).__init__()
        self.model_name = 'MultiCNNTextBNDeep'
        self.encoder = nn.Embedding(vocab_size, embedding_dim)

        content_convs = [nn.Sequential(
            nn.Conv1d(in_channels=embedding_dim,
                      out_channels=content_dim,
                      kernel_size=kernel_size),
            nn.BatchNorm1d(content_dim),
            nn.ReLU(inplace=True),

            nn.Conv1d(in_channels=content_dim,
                      out_channels=content_dim,
                      kernel_size=kernel_size),
            nn.BatchNorm1d(content_dim),
            nn.ReLU(inplace=True),
            nn.MaxPool1d(kernel_size=(context_size - kernel_size * 2 + 2))
        )
            for kernel_size in kernel_sizes]

        self.content_convs = nn.ModuleList(content_convs)

        self.fc = nn.Sequential(
            nn.Linear(len(kernel_sizes) * (content_dim), linear_hidden_size),
            nn.BatchNorm1d(linear_hidden_size),
            nn.ReLU(inplace=True),
            nn.Linear(linear_hidden_size, num_classes)
        )

        # if opt.embedding_path:
        #     self.encoder.weight.data.copy_(t.from_numpy(np.load(opt.embedding_path)['vector']))

    def forward(self, content):
        content = self.encoder(content)

        content.detach()
        # if self.opt.static:
        #     content.detach()

        content_out = [content_conv(content.permute(0, 2, 1)) for content_conv in self.content_convs]
        conv_out = torch.cat((content_out), dim=1)
        reshaped = conv_out.view(conv_out.size(0), -1)
        logits = self.fc((reshaped))
        return logits