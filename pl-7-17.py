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
        print('input')
        print(x)
        return self.net(x)
    
    def training_step(self, batch: Tuple[Tensor, Tensor]) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)

        y_hat = self.net(x)
        loss = self.loss_fn(y_hat, y)
        loss/= x.size(0)
        tensorboard_logs = {"mse": loss}
    
        return {"loss": loss, "log": tensorboard_logs, "progress_bar": tensorboard_logs}
    
    def validation_step(self, batch: Tuple[Tensor, Tensor], batch_idx: int) -> Dict[str, Tensor]:
        x, y = batch
        x = x.view(x.size(0), -1)

        y_hat = self.net(x)
        loss = self.loss_fn(y_hat, y)
        loss/= x.size(0)
        return {"val_loss": loss}

    def configure_optimizers(self) -> Optimizer:
        return self.optimizer(self.parameters(), lr=self.hparams.learning_rate)

class CustomedDataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self):
        
        T = 1000
        self.time = np.arange(1, T + 1)
        # self.x = torch.sin(0.01 * self.time) + torch.normal(0, 0.2, (T,))
        self.x = np.sin(0.01 * self.time) + np.random.normal(0, 0.2, (T,))
        tau = 4

        # self.features = torch.zeros((T - tau, tau))
        self.features = np.zeros((T - tau, tau))
        for i in range(tau):
            self.features[:, i] = self.x[i:T - tau + i]
        self.labels = self.x[tau:].reshape((-1, 1))
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
    train_dataloader=DataLoader(train_dataset, collate_fn=CustomedDataset.collate_fn)
    # train
    print('=========================== args ==============')
    trainer = Trainer.from_argparse_args(args)
    trainer.fit(model, train_dataloader=train_dataloader, val_dataloaders=train_dataloader)
    # print(train_dataset.time)
    pred = model(torch.cat([torch.Tensor(feature) for feature in train_dataset.features]))
    print(pred)
if __name__ == "__main__":
    cli_main()
