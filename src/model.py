import torch
import torch.nn as nn


# define the CNN architecture
class MyModel(nn.Module):
    def __init__(self, num_classes: int = 1000, dropout: float = 0.7) -> None:

        super().__init__()

        self.model = nn.Sequential(
         
            nn.Conv2d(in_channels=3, out_channels=16, kernel_size=5, padding=2),
            #nn.BatchNorm2d(16),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(in_channels=16, out_channels=32, kernel_size=5, padding=2),
            #nn.BatchNorm2d(32),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=5, padding=2),
            nn.BatchNorm2d(64),  
            nn.ReLU(),
            nn.MaxPool2d(2, 2),  
            
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),
            nn.BatchNorm2d(256), 
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            
            nn.Conv2d(in_channels=256, out_channels=512, kernel_size=3, padding=1), #512*7*7
            nn.BatchNorm2d(512), 
            nn.ReLU(),
            #nn.MaxPool2d(2, 2),
            
            nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=3, padding=1), 
            nn.BatchNorm2d(1024),
            nn.ReLU(),
            #nn.MaxPool2d(2, 2),
              
            #nn.AdaptiveAvgPool2d((1, 1)),
            nn.Flatten(),
            
            nn.Linear(7 * 7 * 1024, 512),
            nn.Dropout(p=dropout),
            nn.BatchNorm1d(512),
            nn.ReLU(),    
            
            nn.Linear(512, 256),
            nn.Dropout(p=dropout),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            
            nn.Linear(256, num_classes)
        )


    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = self.model(x)
        return x


######################################################################################
#                                     TESTS
######################################################################################
import pytest


@pytest.fixture(scope="session")
def data_loaders():
    from .data import get_data_loaders

    return get_data_loaders(batch_size=2)


def test_model_construction(data_loaders):

    model = MyModel(num_classes=23, dropout=0.3)

    dataiter = iter(data_loaders["train"])
    images, labels = dataiter.next()

    out = model(images)

    assert isinstance(
        out, torch.Tensor
    ), "The output of the .forward method should be a Tensor of size ([batch_size], [n_classes])"

    assert out.shape == torch.Size(
        [2, 23]
    ), f"Expected an output tensor of size (2, 23), got {out.shape}"
