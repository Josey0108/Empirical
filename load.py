import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (replace 'file.xlsx' with your actual file)
file_path = r"C:\Users\josey\Downloads\Book1.xlsx"
xls = pd.ExcelFile(file_path)

# Read the two sheets (without AI and with AI)
df_without_ai = pd.read_excel(xls, sheet_name="Without AI")
df_with_ai = pd.read_excel(xls, sheet_name="With AI")

# Display first few rows
df_without_ai.head(), df_with_ai.head()
print(df_without_ai.head())
print(df_with_ai.head())

#Second checking normality
# Extract the debugging scores (Correctness, Efficiency, or Attempt Rate)
without_ai_scores = df_without_ai["Attemption rate"]  # Replace "Correctness" with your actual column name
with_ai_scores = df_with_ai["Attemption rate"]

# Perform Shapiro-Wilk test for normality
shapiro_without_ai = stats.shapiro(without_ai_scores)
shapiro_with_ai = stats.shapiro(with_ai_scores)

print("Shapiro-Wilk test (Without AI):", shapiro_without_ai)
print("Shapiro-Wilk test (With AI):", shapiro_with_ai)
 

 #proceeding with p test
 # Perform paired t-test
t_stat, p_value = stats.ttest_rel(without_ai_scores, with_ai_scores)

print("Paired t-test results:")
print("t-statistic =", t_stat)
print("p-value =", p_value)

#Data visualization
#plt.figure(figsize=(8, 5))
#sns.boxplot(data=[without_ai_scores, with_ai_scores], palette=["red", "blue"])
#plt.xticks([0, 1], ["Without AI", "With AI"])
#plt.ylabel("Correctness Score")
#plt.title("Comparison of Debugging Performance")
#plt.show()
sns.histplot(df_without_ai, kde=True, label="Without AI", color='blue')
sns.histplot(df_with_ai, kde=True, label="With AI", color='red')
plt.legend()
plt.show()



plt.hist(without_ai_scores, alpha=0.5, label="Without AI", color="red", bins=10)
plt.hist(with_ai_scores, alpha=0.5, label="With AI", color="blue", bins=10)
plt.xlabel("Attemption rate")
plt.ylabel("Frequency")
plt.legend()
plt.title("Distribution of Debugging Scores")
plt.show()


