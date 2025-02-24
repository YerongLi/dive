from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# 1. 加载数据
data = load_breast_cancer()
X, y = data.data, data.target  # 乳腺癌数据集是天然的二分类问题

# 2. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 训练模型
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# 4. 模拟历史数据（假设过去 30 天的预测概率）
np.random.seed(42)
historical_predictions = np.random.rand(30, len(y_test))  # 30 天的假设预测概率

# 5. 获取新一天的预测概率
new_predictions = model.predict_proba(X_test)[:, 1]  # 只取正类（患病）的概率

# 6. 计算历史数据均值和标准差
historical_mean = np.mean(historical_predictions, axis=1)  # 计算每天的均值
historical_std = np.std(historical_predictions, axis=1)    # 计算每天的标准差

# 7. 计算新一天的均值和标准差
new_mean = np.mean(new_predictions)
new_std = np.std(new_predictions)

# 8. 比较新数据与历史数据的差异
mean_diff = new_mean - np.mean(historical_mean)
std_diff = new_std - np.mean(historical_std)

print(f"历史均值: {np.mean(historical_mean):.4f}, 新一天均值: {new_mean:.4f}, 均值变化: {mean_diff:.4f}")
print(f"历史标准差: {np.mean(historical_std):.4f}, 新一天标准差: {new_std:.4f}, 标准差变化: {std_diff:.4f}")
