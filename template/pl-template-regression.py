from argparse import ArgumentParser
from typing import Any, Dict, List, Tuple, Type

import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

from pytorch_lightning import LightningModule, Trainer, seed_everything
from torch import Tensor, nn
from torch.nn import functional as F
from torch.nn.functional import softmax
from torch.optim import Adam
from torch.optim.optimizer import Optimizer
import matplotlib.pyplot as plt
from pytorch_lightning import loggers as pl_loggers


class SequentialNet(LightningModule):
    @classmethod
    def init_weights(cls, m):
        if type(m) == nn.Linear:
            nn.init.xavier_uniform_(m.weight)
    def __init__(self,
        learning_rate: float = 1e-4,
        optimizer: Type[Optimizer] = Adam,
        **kwargs: Any,
        ):
        super().__init__()
        self.save_hyperparameters()

        self.optimizer = optimizer
        # self.learning_rate = learning_rate
        self.net = nn.Sequential(nn.Linear(4, 10), nn.ReLU(), nn.Linear(10, 1))
        ## Initialization
        self.net.apply(SequentialNet.init_weights)
        self.loss_fn = nn.MSELoss()


    def forward(self, x: Tensor) -> Tensor:
        x = x.view(x.size(0), -1)

        return self.net(x)
    
    def training_step(self, batch: Tuple[Tensor, Tensor], batch_idx) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)
        y_hat = self.net(x)
        loss = self.loss_fn(y_hat, y)
        loss/= x.size(0)
        tensorboard_logs = {"train_loss": loss}
        return {"loss": loss, "log": tensorboard_logs, "progress_bar": tensorboard_logs}
    
    def validation_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)

        y_hat = self.net(x)
        loss = self.loss_fn(y_hat, y)
        loss/= x.size(0)
        return {"val_loss": loss}

    def train_epoch_end(self, outputs: List[Dict[str, Tensor]]) -> Dict[str, Tensor]:
        loss = torch.stack([output['train_loss'] for output in outputs])
        return {
            'loss': loss,
            'log' : {'loss': loss},
        }
    def configure_optimizers(self) -> Optimizer:
        # return self.opti,mizer(self.parameters(), lr=self.hparams.learning_rate)
        return self.optimizer(self.parameters(), lr=0.005)

class CustomedDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self):
        
        T = 1000
        self.time = np.arange(1, T + 1)
        # self.x = torch.sin(0.01 * self.time) + torch.normal(0, 0.2, (T,))
        self.x = np.sin(0.01 * self.time) + np.random.normal(0, 0.2, (T,))
        self.tau = 4

        # self.features = torch.zeros((T - tau, tau))
        self.features = np.zeros((T - self.tau, self.tau))
        for i in range(self.tau):
            self.features[:, i] = self.x[i:T - self.tau + i]
        self.labels = self.x[self.tau:].reshape((-1, 1))
    def __len__(self):
        return len(self.labels)
    def __getitem__(self, i):
        label = self.labels[i]
        data = self.features[i]
        return {'feature': data, 'label': label}
    @staticmethod
    def collate_fn(data_list):
        features = torch.cat([torch.Tensor(item['feature']) for item in data_list], dim=0).view(len(data_list) ,-1)
        labels = torch.cat([torch.Tensor(item['label']) for item in data_list])
        return features, labels

def cli_main():
    parser = ArgumentParser()
    parser = Trainer.add_argparse_args(parser)
    args = parser.parse_args()
    model = SequentialNet(max_steps=10)
    train_dataset = CustomedDataset()
    train_dataloader=DataLoader(train_dataset, collate_fn=CustomedDataset.collate_fn, batch_size = 16)
    # train
    print('=========================== args ==============')
    
    tb_logger = pl_loggers.TensorBoardLogger(save_dir="regression_logs/")
    trainer = Trainer.from_argparse_args(args, logger=tb_logger)
    trainer.fit(model, train_dataloader=train_dataloader, val_dataloaders=train_dataloader)
    with torch.no_grad():
        pred = model(torch.Tensor(train_dataset.features))
    plt.plot(train_dataset.time[train_dataset.tau:], train_dataset.labels)
    plt.plot(train_dataset.time[train_dataset.tau:], pred)

    plt.show()

if __name__ == "__main__":
    cli_main()
