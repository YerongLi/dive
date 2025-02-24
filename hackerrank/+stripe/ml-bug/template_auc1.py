import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve, roc_curve, precision_score, recall_score

# 1️⃣ Load Dataset
data = load_breast_cancer()
X, y = data.data, data.target

# 2️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3️⃣ Train RandomForest Classifier
model = RandomForestClassifier(random_state=42, n_estimators=100)
model.fit(X_train, y_train)

# 4️⃣ Get Predictions (Probabilities for Class 1)
y_scores = 

# 5️⃣ Compute Precision, Recall, and ROC Curve
precision, recall, _ = 
fpr, tpr, _ = 
# 6️⃣ Wrong ROC AUC Calculation (Incorrect Summation)
wrong_roc_auc = sum(tpr)  # ❌ INCORRECT: Just summing up TPR


correct_roc_auc =

# 8️⃣ Compute Precision and Recall at threshold 0.5
y_pred = 
precision_manual = 
recall_manual = 

print(f"Precision: {precision_manual:.4f}, Recall: {recall_manual:.4f}")
print(f"🚨 Wrong ROC AUC (Incorrect Sum): {wrong_roc_auc:.4f}")  # Should be wrong
print(f"✅ Correct ROC AUC (Trapezoidal Rule): {correct_roc_auc:.4f}")  # Should be between 0-1

# 9️⃣ Plot Precision-Recall & ROC Curve
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(recall, precision, marker='.', label=f'PR AUC: {compute_auc_trapezoidal(recall, precision):.4f}')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(fpr, tpr, marker='.', label=f'ROC AUC: {correct_roc_auc:.4f}')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')  # Random classifier line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid()

plt.savefig("auc.png", dpi=300, bbox_inches='tight')
plt.show()
