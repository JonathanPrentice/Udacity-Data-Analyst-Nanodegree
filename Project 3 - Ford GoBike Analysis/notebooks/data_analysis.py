import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('../data/201902-fordgobike-tripdata.csv')

# Display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Display summary statistics of the dataset
print("\nSummary Statistics:")
print(df.describe())

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop rows with missing values
df.dropna(inplace=True)

# Univariate Analysis: Distribution of trip duration
plt.figure(figsize=(10, 6))
sns.histplot(df['duration_sec'], kde=True)
plt.title('Distribution of Trip Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.savefig('../images/trip_duration_distribution.png')
plt.show()

# Bivariate Analysis: Trip duration by user type
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='user_type', y='duration_sec')
plt.title('Trip Duration by User Type')
plt.xlabel('User Type')
plt.ylabel('Duration (seconds)')
plt.savefig('../images/trip_duration_by_user_type.png')
plt.show()

# Multivariate Analysis: Trip duration by user type and gender
plt.figure(figsize=(10, 6))
sns.violinplot(data=df, x='user_type', y='duration_sec', hue='member_gender', split=True)
plt.title('Trip Duration by User Type and Gender')
plt.xlabel('User Type')
plt.ylabel('Duration (seconds)')
plt.savefig('../images/trip_duration_by_user_type_and_gender.png')
plt.show()

print("Analysis and visualizations completed.")