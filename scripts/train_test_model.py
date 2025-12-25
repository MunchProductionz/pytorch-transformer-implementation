import lightning as L
from torch.utils.data import DataLoader

from src.pytorch_transformer.models.test_model import TestModel
from src.pytorch_transformer.training.test_model_lightning import LitTestModel


def train():
    dataset = ""
    train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

    test_model = TestModel(input_size=784, hidden_size=256, output_size=784)
    lit_model = LitTestModel(test_model)

    trainer = L.Trainer(max_epochs=10)
    trainer.fit(lit_model, train_loader)
