import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('tips')
df = df.dropna()
print(df.info())
print(df.head())
print(df.describe())

sns.barplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Bill by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.countplot(x='day', hue='sex', data=df)
plt.title('Number of Coustomers by Gender')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x='day', y='total_bill', data=df)
plt.title('Bill amount per Coustomer')
plt.xlabel('Day')
plt.ylabel('Bill amount ($)')
plt.show()

sns.stripplot(x='day', y='total_bill', jitter=True, data=df)
plt.title('Bill amount per Coustomer')
plt.xlabel('Day')
plt.ylabel('Bill amount ($)')
plt.show()

sns.swarmplot(x='day', y='total_bill', data=df)
plt.title('Bill amount per Coustormer')
plt.xlabel('Day')
plt.ylabel('Bill amount ($)')
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, color='red')
plt.suptitle('Coustomer Bill vs Tip', y=1.02)
plt.show()

sns.jointplot(x='total_bill', y='tip', data=df, color='steelblue', kind='kde')
plt.suptitle('Coustomer Bill vs Tip - KDE', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pair Plot - Bill, Tip and Party Size', y=1.02)
plt.show()

sns.pointplot(x='day', y='total_bill', hue='sex', data=df)
plt.title('Average Coustomer Bill by Gender')
plt.xlabel('Day')
plt.ylabel('Average Bill ($)')
plt.show()

sns.lmplot(x='total_bill', y='tip', data=df)
plt.title('Coustomer Bill vs Tip - Trend Line')
