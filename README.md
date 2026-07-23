# AOI Defect Classification

使用深度學習對自動光學檢查（Automated Optical Inspection, AOI）影像
進行瑕疵分類。資料來源為工研院提供、AIdea 平台開放的 AOI 瑕疵檢測資料集。

## 專案目標
- 建立瑕疵分類 baseline 並逐步優化
- 探討 AOI 場景特有的挑戰：類別不平衡、小瑕疵、漏檢與過殺的取捨

## 資料集
資料集不包含在此 repo 中，請自行從 AIdea 下載後放置於：
```
data/
├── train_images/
├── test_images/
├── train.csv
└── test.csv
```
## 環境

```bash
pip install -r requirements.txt
```

## 目錄結構
| 路徑 | 說明 |
|---|---|
| `notebooks/` | 探索與實驗流程 |
| `src/` | 資料集、模型、訓練的可重用程式碼 |
| `results/` | 混淆矩陣、錯誤樣本等輸出 |
| `experiments.md` | 實驗日誌 |

## 結果
（待補）

## 心得與反思
（待補）