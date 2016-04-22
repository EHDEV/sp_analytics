import pandas as p
from data_access_layer.dao import Dao
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
import numpy as np


df_cells_feat = p.DataFrame.from_csv("/Users/EH/columbia/projects/capstone_sp/data/1000cell_user_freq_lifetime.csv", index_col=None)
df_cells_feat_piv = df_cells_feat.pivot(index='userid', columns='cellid', values='freq_updates')
# df_cells_feat_piv['userid'] = df_cells_feat_piv.index
da = Dao()

q = '''
    SELECT * FROM vw_avg_event_by_distinct_cell;
'''
user_cells_distinct = da.query(q)

dlist = []
for row in user_cells_distinct:
    dlist += [dict(row)]
df_user_cells_distinct = p.DataFrame(dlist)
df_user_cells_distinct.index = df_user_cells_distinct['userid']

merged = p.merge(df_user_cells_distinct[['userid', 'avg_updates_per_day']], df_cells_feat_piv, how='left', left_index=True,
                               right_index=True, suffixes=('', '_y'))
merged.fillna(0, inplace=True)

cos_dists = p.DataFrame(cosine_similarity(merged), columns=merged.index)
euc_dists = p.DataFrame(euclidean_distances(merged), columns=merged.index)

cos_dists.index = cos_dists.columns
euc_dists.index = euc_dists.columns

def get_sims(users, euc=False):
    """

    dists - a distance matrix
    product - a product id (integer)
    """
    if euc:
        dists = euc_dists
    else:
        dists = cos_dists

    u = dists[users].apply(lambda row: np.sum(row), axis=1)
    u = u.order(ascending=False)
    return u.index[u.index.isin(users)==False][0:10]

print(get_sims([-9210456170664700000], euc=True))