import codecademylib
import pandas as pd
import numpy as np

ad_clicks = pd.read_csv('ad_clicks.csv')

views_count = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(views_count)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks.head())

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])['user_id'].count().reset_index()
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()


clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])
print(clicks_pivot)

expgroup_count = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
#print(expgroup_count)
abgroup_count = ad_clicks.groupby(['experimental_group', 'is_click'])['user_id'].count().reset_index()
#print(abgroup_count)
abgroup_pivot = abgroup_count.pivot(columns = 'is_click', index = 'experimental_group', values = 'user_id').reset_index()
#print(abgroup_pivot)
abgroup_pivot['percent_clicked'] = abgroup_pivot[True] / (abgroup_pivot[True] + abgroup_pivot[False])
print(abgroup_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
print(a_clicks.head())
print(b_clicks.head())

a_clicks_group = a_clicks.groupby(['is_click','day'])['user_id'].count().reset_index()
b_clicks_group = b_clicks.groupby(['is_click','day'])['user_id'].count().reset_index()
print(a_clicks_group)
print(b_clicks_group)

a_clicks_pivot = a_clicks_group.pivot(columns = 'is_click', index = 'day', values = 'user_id')
b_clicks_pivot = b_clicks_group.pivot(columns = 'is_click', index = 'day', values = 'user_id')

a_clicks_pivot['click_percentage'] = a_clicks_pivot[True]/ (a_clicks_pivot[True] + a_clicks_pivot[False])
b_clicks_pivot['click_percentage'] = b_clicks_pivot[True]/ (b_clicks_pivot[True] + b_clicks_pivot[False])

print(a_clicks_pivot)
print(b_clicks_pivot)