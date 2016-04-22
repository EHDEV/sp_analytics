# Prepare to merge by name

dfnotmerged2.name = dfnotmerged2.name.str.lower()\
    .str.replace("", "").str.replace(")", "")\
    .str.replace("(", "").str.replace("and", "")\
    .str.replace("'", "").str.replace("&", "")\
    .str.replace(" ", "").str.replace("-", "")
temp_locu_train_df.name = temp_locu_train_df.name.str.lower()\
    .str.replace("", "")\
    .str.replace(")", "")\
    .str.replace("(", "")\
    .str.replace("and", "")\
    .str.replace("'", "")\
    .str.replace("&", "")\
    .str.replace(" ", "")\
    .str.replace("-", "")

df_merge_by_name = p.merge(dfnotmerged2, temp_locu_train_df[["id", "name"]], how='left', on=['name'], suffixes=('', '_l'))
dfnotmerged3 = dfmerged3[p.isnull(dfmerged3.id_l)]