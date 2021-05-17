import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# read in the data
data = pd.read_csv("country_wise_latest.csv")

# remove any duplicates
cleaned_data = data.drop_duplicates()

# remove missing rows
cleaned_data = cleaned_data.dropna()

# show first 5 rows
print(cleaned_data.head())

# show final 5 rows
print(cleaned_data.tail())

# print the columns
print(cleaned_data.columns)

# sort the data
sorted_data = cleaned_data.sort_values('Recovered', ascending=False)

# print sorted data
print(sorted_data)

# index the data
indexed_data = sorted_data.reset_index(drop=True)

# group the data
grouped_data = indexed_data.groupby(['WHO Region', 'Deaths', 'Recovered']).agg('sum')

# print information
pd.options.display.max_rows = None
print(f'Columns: \n{data.columns} \n')
print(f'Data Types: \n{data.dtypes} \n')
print(f'Data: \n{data} \n')

print(f'Cleaned: \n{cleaned_data} \n')
print(f'Sorted: \n{sorted_data} \n')
print(f'Indexed: \n{indexed_data} \n')
print(f'Grouped: \n{grouped_data} \n')

# plot 1
fig, ax = plt.subplots()
x_axis = indexed_data['Country/Region']
y_axis_names = indexed_data['WHO Region'].unique()

y_axes_data_frames = {}
for y_axis_name in y_axis_names:
    death_count = 0
    recovered_count = 0

    for row in indexed_data.iterrows():
        entry = row[1]
        if entry['WHO Region'] == y_axis_name:
            death_count += entry['Deaths']
            recovered_count += entry['Recovered']

    data_frame = pd.DataFrame({'WHO Region': [y_axis_name],
                               'Deaths': [death_count],
                               'Recovered': [recovered_count]})

    y_axes_data_frames[y_axis_name] = data_frame

for entry in y_axes_data_frames.values():
    recovered = entry['Recovered']
    deaths = entry['Deaths']
    ax.bar(entry['WHO Region'], recovered, label='Recovered', color='g')
    ax.bar(entry['WHO Region'], deaths, label='Deaths', bottom=recovered, color='r')

ax.set_title('Recovered vs Deaths per WHO Region')
ax.set_xlabel('WHO Region')
ax.set_ylabel('Recovered (green) vs Deaths (red)')

sns.lineplot(x=data['WHO Region'].head(5),y=data['Deaths'].head(5))
plt.show()

sns.lineplot(x=data['WHO Region'].head(5),y=data['Recovered'].head(5))

plt.show()

sns.set_theme(style="whitegrid")
sns.barplot(x=data.Confirmed, y=data.Recovered)
plt.title("Confirmed vs Recovered")
plt.ylabel("Recovered")
plt.xlabel("Confirmed")
plt.ylim(0,1000)
plt.xlim(0,1000)
plt.show()

# list of top 3 countries highest confirmed cases using numpy array to print the first country
confirmed = ["US", 4290259, "Brazil", 2442375, "India", 1480073]

print(confirmed)

first = confirmed[0]

print(first)

# list of top 3 countries with recovered cases using numpy array to print the first country
recovered = ["Brazil", 1846641, "US", 1325804, "India", 951166]

print(recovered)

top = recovered[0]

print(top)

# list of top 3 deaths

death = ["US", 148011, "Brazil", 87618, "United Kingdom", 45844]

print(death)

highest = death[0]

print(highest)

# plot 3 highest countries with confirmed cases
y = np.array([4290259, 2442375, 1480073])
mylabels = ["US", "Brazil", "India"]

plt.pie(y, labels = mylabels, startangle = 90, shadow= True)
plt.legend(title = "3 highest confirmed cases per country:")
plt.legend()
plt.show()

# plot 3 highest countries with recovered cases
y = np.array([1846641, 1325804, 951166])
mylabels = ["Brazil", "US", "India"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.legend(title = "3 highest recovered cases per country:")
plt.legend()
plt.show()