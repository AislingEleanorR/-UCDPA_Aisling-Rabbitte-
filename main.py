import pandas as pd
import matplotlib.pyplot as plt

# read in the data
data = pd.read_csv("country_wise_latest.csv",
                   usecols=['Country/Region', 'Deaths', 'Recovered', 'WHO Region'])

# remove any duplicates
cleaned_data = data.drop_duplicates()

# remove missing rows
cleaned_data = cleaned_data.dropna()

# sort the data
sorted_data = cleaned_data.sort_values('Recovered', ascending=False)

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

# plot
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

plt.show()
