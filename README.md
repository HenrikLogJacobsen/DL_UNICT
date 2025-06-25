# Project 5: ECG Arrhythmia Classification

**Reference Person:** [Raffaele Mineo](mailto:raffaele.mineo@unict.it)  
**Goal:** Classify 12-lead ECG signals for multi-label arrhythmia detection.

## Dataset

- **Name:** PTB-XL  
- **Description:** 21,799 clinical 12-lead ECG recordings (10 seconds each) from 18,869 patients. Each recording is annotated with up to 71 diagnostic statements, including rhythm, form, and diagnostic categories.  
- **Link:** [PTB-XL Dataset on Kaggle](https://www.kaggle.com/datasets/khyeh0719/ptb-xl-dataset)  
- **Size:** 3.2 GB  

## Methodology

Design and implement a deep learning model suitable for sequential ECG data, such as:
- 1D Convolutional Neural Network (1D-CNN)
- Transformer-based architecture

## Performance Evaluation

Evaluate model performance across different diagnostic tasks (e.g., specific arrhythmia detection) using appropriate **multi-label classification metrics**.

## References

- Wagner, Patrick, et al. *“PTB-XL, a large publicly available electrocardiography dataset.”* Scientific Data 7.1 (2020): 1–15.  
- PTB-XL Kaggle dataset and starter code.

## Expected Completion Time

**Estimated time:** 40 hours

## Additional Notes

### Guideline
- According to the source of the dataset, there are recommended stratified 10-folds, where the same patients are kept within the same folds. Moreover, 9th fold and 10th are of higher quality, which are recommeded to be used as validation set and test set.

Cross-validation Folds: recommended 10-fold train-test splits (strat_fold) obtained via stratified sampling while respecting patient assignments, i.e. all records of a particular patient were assigned to the same fold. Records in fold 9 and 10 underwent at least one human evaluation and are therefore of a particularly high label quality. We therefore propose to use folds 1-8 as training set, fold 9 as validation set and fold 10 as test set.