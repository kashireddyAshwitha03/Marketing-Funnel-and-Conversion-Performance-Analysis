import pandas as pd
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv("data/marketing_funnel_data.csv")

print("Marketing Funnel Data:")
print(df)

# Calculate Conversion Rate
initial_users = df['Users'].iloc[0]
final_users = df['Users'].iloc[-1]

conversion_rate = (final_users / initial_users) * 100

print("\nOverall Conversion Rate:")
print(f"{conversion_rate:.2f}%")

# Funnel Visualization
plt.figure(figsize=(8,5))
plt.bar(df['Stage'], df['Users'])

plt.title("Marketing Funnel Analysis")
plt.xlabel("Funnel Stage")
plt.ylabel("Users")
plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig("data/funnel_chart.png")
plt.show()