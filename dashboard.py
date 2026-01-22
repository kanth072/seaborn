import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
df = pd.read_csv('/content/sales_data.csv')

sns.set_theme(style="whitegrid", palette="muted")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.patch.set_facecolor("#f5f5f5")


# 1. Box Plot
sns.boxplot(x='Product', y='Price', data=df, ax=axes[0, 0])
axes[0, 0].set_title("Price Distribution by Product")

# 2. Violin Plot
sns.violinplot(x='Product', y='Price', data=df, ax=axes[0, 1])
axes[0, 1].set_title("Price Density by Product")

# 3. Bar Plot (Mean Price)
sns.barplot(x='Product', y='Price', data=df, estimator='mean', ax=axes[0, 2])
axes[0, 2].set_title("Average Price by Product")

# 4. Histogram
sns.histplot(df['Price'], kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Price Distribution")

# 5. Scatter Plot
sns.scatterplot(x='Quantity', y='Price', hue='Product', data=df, ax=axes[1, 1])
axes[1, 1].set_title("Price vs Quantity")

axes[1, 2].axis("off")
plt.tight_layout()
plt.show()
