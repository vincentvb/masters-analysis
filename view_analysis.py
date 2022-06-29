import pandas as pd
import matplotlib.pyplot as plt

df_2019 = pd.read_json('data/views_2019.json')
df_2020 = pd.read_json('data/views_2020.json')
df_2021 = pd.read_json('data/views_2021.json')

df_merged = df_2019.merge(df_2020, on='channelId')[['channelId', 'views_x', 'views_y']]

df_merged.rename(columns={
    'views_x': 'views_2019',
    'views_y': 'views_2020'
}, inplace=True)

df_final = df_merged.merge(df_2021, on='channelId')[['channelId', 'views_2019', 'views_2020', 'views']]

df_final.rename(columns={
    'views': 'views_2021'
}, inplace=True)

channel_df = pd.read_json('data/channel_info.jsonl.gz', lines=True, compression='gzip')

df_final = df_final.merge(channel_df, on='channelId')

df_final['mainstream'] = df_final.tags.apply(lambda x: 1 if 'Mainstream News' in x else 0)

df_grouped = df_final.groupby('mainstream').sum()[['views_2019', 'views_2020', 'views_2021']].reset_index()
df_grouped_not_cable = df_grouped[df_grouped['mainstream'] == 0][['views_2019', 'views_2020', 'views_2021']]
df_grouped_cable = df_grouped[df_grouped['mainstream'] == 1][['views_2019', 'views_2020', 'views_2021']]

plt.plot(['2019', '2020', '2021'], [df_grouped_not_cable['views_2019'], df_grouped_not_cable['views_2020'], df_grouped_not_cable['views_2021']], label='Non-Cable Channels')
plt.plot(['2019', '2020', '2021'], [df_grouped_cable['views_2019'], df_grouped_cable['views_2020'], df_grouped_cable['views_2021']], label='Cable Channels')
plt.xlabel('Year')
plt.ylabel('Number of Views')
plt.legend()
plt.show()

