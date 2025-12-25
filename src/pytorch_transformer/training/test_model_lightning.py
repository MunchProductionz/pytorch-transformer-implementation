import lightning as L
import torch
import torch.nn as nn
from torch.nn import functional as F


class LitTestModel(L.LightningModule):
    def __init__(self, test_model):
        super().__init__()
        self.model = test_model
        self.criterion = F.mse_loss()

    def training_step(self, batch, batch_idx):
        # defines the training loop
        x, _ = batch
        x = x.view(x.size(0), -1)  # flatten the input
        x_hat = self.model.forward(x)
        loss = F.mse_loss(x_hat, x)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.model.parameters(), lr=1e-3)
        return optimizer
