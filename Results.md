## 1DCNN V0

Per-class accuracy:
NORM: 0.7031
MI: 0.7490
STTC: 0.7626
HYP: 0.8806
CD: 0.7739

Classification report (macro avg):
              precision    recall  f1-score   support

        NORM       0.68      0.61      0.64       964
          MI       0.00      0.00      0.00       553
        STTC       0.00      0.00      0.00       523
         HYP       0.00      0.00      0.00       263
          CD       0.00      0.00      0.00       498

   micro avg       0.68      0.21      0.32      2801
   macro avg       0.14      0.12      0.13      2801
weighted avg       0.23      0.21      0.22      2801
 samples avg       0.27      0.26      0.26      2801

 ### Lower threshold .5 --> .4

 Per-class accuracy:
NORM: 0.6877
MI: 0.7453
STTC: 0.7621
HYP: 0.8806
CD: 0.7594

Classification report (macro avg):
              precision    recall  f1-score   support

        NORM       0.62      0.76      0.68       964
          MI       0.48      0.18      0.26       553
        STTC       0.49      0.09      0.15       523
         HYP       0.00      0.00      0.00       263
          CD       0.40      0.13      0.20       498

   micro avg       0.57      0.34      0.43      2801
   macro avg       0.40      0.23      0.26      2801
weighted avg       0.47      0.34      0.35      2801
 samples avg       0.40      0.39      0.39      2801