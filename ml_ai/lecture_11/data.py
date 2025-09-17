import torch
import torchvision
import os
import torchvision.transforms.functional as TF
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import lightning
import json
import zipfile
import random


class ShabbyPagesDataset(Dataset):
    def __init__(
        self,
        split="train",
        augment=False,
        crop_ratio=0.8,
        rotation_angle=90,
        flip_probability=0.5,
    ):
        super().__init__()

        self.image_size = 400
        self.image_normalization = 255.0
        self.augment = augment
        self.crop_ratio = crop_ratio
        self.rotation_angle = rotation_angle
        self.flip_probability = flip_probability

        self.folder_shabby = f"{split}/{split}/{split}_shabby/"
        self.folder_clean = f"{split}/{split}/{split}_cleaned/"

        self.image_dict = {}
        for idx, image_name in enumerate(os.listdir(self.folder_shabby)):
            self.image_dict[idx] = image_name

        with open(f"{split}_image_dict.json", "w") as f:
            json.dump(self.image_dict, f)

    def transform(self, input_img, target_img):
        # Random crop
        # Get the parameters for the random crop
        i, j, h, w = transforms.RandomCrop.get_params(
            input_img,
            output_size=(
                int(self.image_size * self.crop_ratio),
                int(self.image_size * self.crop_ratio),
            ),
        )
        # Crop the images
        # Input and target images are cropped to the same size, with the same spatial location
        # This is important to ensure that the input and target images are aligned
        input_img = TF.crop(input_img, i, j, h, w)
        target_img = TF.crop(target_img, i, j, h, w)

        # Random horizontal flipping
        if random.random() < self.flip_probability:
            input_img = TF.hflip(input_img)
            target_img = TF.hflip(target_img)

        # Random vertical flipping
        if random.random() < self.flip_probability:
            input_img = TF.vflip(input_img)
            target_img = TF.vflip(target_img)

        # Select a random rotation angle
        angle = random.randint(-self.rotation_angle, +self.rotation_angle)
        # Rotate input image and target image by the same angle
        input_img = TF.rotate(input_img, angle)
        target_img = TF.rotate(target_img, angle)

        return input_img, target_img

    def __len__(self):
        return len(self.image_dict)

    def __getitem__(self, idx):
        input_sample = (
            torchvision.io.read_image(
                os.path.join(self.folder_shabby, self.image_dict[idx])
            ).to(dtype=torch.float32)
        ) / self.image_normalization
        target_sample = (
            torchvision.io.read_image(
                os.path.join(self.folder_clean, self.image_dict[idx])
            ).to(dtype=torch.float32)
        ) / self.image_normalization

        if self.augment:
            return self.transform(input_sample, target_sample)
        else:
            return input_sample, target_sample


class ShabbyPagesDataModule(lightning.LightningDataModule):
    """
    ShabbyPagesDataModule is a PyTorch Lightning DataModule for the Shabby Pages dataset.
    It handles the loading and preprocessing of the dataset for training, validation, and testing.
    """

    def __init__(
        self,
        num_workers: int = 8,
        batch_size: int = 16,
    ):
        super().__init__()
        self.num_workers = num_workers
        self.batch_size = batch_size

    def prepare_data(self) -> None:
        # read file denoising-shabby-pages.zip and unzip it
        if not os.path.exists("train/"):
            print('prepare_data')

            with zipfile.ZipFile("denoising-shabby-pages.zip", "r") as zip_ref:
                zip_ref.extractall(".")

    def setup(self, stage: str) -> None:
        if stage == "fit":
            self.train_dataset = ShabbyPagesDataset(split="train", augment=True)
        if stage in ["fit", "validate"]:
            self.validate_dataset = ShabbyPagesDataset(split="validate")
        if stage in ["test", "predict"]:
            self.test_dataset = ShabbyPagesDataset(split="test")

    def train_dataloader(self) -> DataLoader:
        return DataLoader(
            dataset=self.train_dataset,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
            persistent_workers=True
        )

    def val_dataloader(self) -> DataLoader:
        return DataLoader(
            dataset=self.validate_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            persistent_workers=True
        )

    def test_dataloader(self) -> DataLoader:
        return DataLoader(
            dataset=self.test_dataset,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            persistent_workers=True
        )
