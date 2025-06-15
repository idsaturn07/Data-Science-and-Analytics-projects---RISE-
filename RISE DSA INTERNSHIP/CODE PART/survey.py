#Project 8: Survey Data Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean survey data
survey = pd.read_csv('survey_data.csv')
survey.columns = survey.columns.str.strip().str.lower()  # standardize column names

print("Available columns:", survey.columns.tolist())

# ------------------------
# Pie Chart: Would Recommend
# ------------------------
if 'would_recommend' in survey.columns:
    recommend_counts = survey['would_recommend'].value_counts()
    plt.figure(figsize=(4, 4))
    plt.pie(recommend_counts.values, labels=recommend_counts.index,
            autopct='%1.0f%%', colors=['#8fd175', '#ff9999'])
    plt.title('Would Recommend (%)')
    plt.tight_layout()
    plt.savefig('recommend_pie.png')
    plt.show()
else:
    print("⚠️ 'would_recommend' column missing.")

# ------------------------
# Heatmap: Avg Satisfaction by Age Group
# ------------------------
if 'age_group' in survey.columns and 'overall_satisfaction' in survey.columns:
    pivot_age = survey.pivot_table(index='age_group', 
                                    values='overall_satisfaction', 
                                    aggfunc='mean').sort_index()
    plt.figure(figsize=(4, 3))
    sns.heatmap(pivot_age, annot=True, cmap='magma', vmin=1, vmax=5)
    plt.title('Avg Satisfaction by Age Group')
    plt.tight_layout()
    plt.savefig('satisfaction_age_heat.png')
    plt.show()
    print("Average Satisfaction by Age Group:")
    print(pivot_age)
else:
    print("⚠️ 'age_group' or 'overall_satisfaction' column missing.")

# ------------------------
# Bar Chart: Favorite Product Count
# ------------------------
if 'favorite_product' in survey.columns:
    product_counts = survey['favorite_product'].value_counts()
    plt.figure(figsize=(5, 3))
    sns.barplot(x=product_counts.index, y=product_counts.values, 
                hue=product_counts.index, palette='Blues_r', legend=False)
    plt.title('Favorite Product Preference')
    plt.ylabel('Respondent Count')
    plt.xlabel('Product')
    plt.tight_layout()
    plt.savefig('favorite_product_bar.png')
    plt.show()
else:
    print("⚠️ 'favorite_product' column missing.")

# ------------------------
# Bar Chart: Avg Feature Importance
# ------------------------
features = ['feature_importance_ui', 'feature_importance_price', 'feature_importance_performance']
if all(col in survey.columns for col in features):
    avg_importance = survey[features].mean()
    feature_names = avg_importance.index.str.replace('feature_importance_', '', regex=False)

    plt.figure(figsize=(5, 3))
    sns.barplot(x=feature_names, y=avg_importance.values, 
                hue=feature_names, palette='viridis', legend=False)
    plt.title('Avg Feature Importance (1–5)')
    plt.ylabel('Importance Score')
    plt.xlabel('Feature')
    plt.ylim(1, 5)
    plt.tight_layout()
    plt.savefig('feature_importance_bar.png')
    plt.show()
else:
    print("⚠️ One or more feature importance columns missing.")