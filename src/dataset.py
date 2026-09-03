import os
import pandas as pd
from PIL import Image
from torch.utils.data import Dataset


class AOIDataset(Dataset):
    """AIdea AOI 瑕疵分類資料集。

    影像清單一律以 csv 為準,不掃資料夾——避免重複檔或未標註檔混入。
    """

    def __init__(self, csv_path, img_dir, transform=None):
        self.df = pd.read_csv(csv_path)
        self.img_dir = img_dir
        self.transform = transform

    def __len__(self):
        return len(self.df)

    def __getitem__(self, idx):
        row = self.df.iloc[idx]
        img_path = os.path.join(self.img_dir, row["ID"])

        # L(灰階)轉 RGB 三通道,以套用 ImageNet 預訓練權重
        image = Image.open(img_path).convert("RGB")

        if self.transform is not None:
            image = self.transform(image)

        label = int(row["Label"])
        return image, label
