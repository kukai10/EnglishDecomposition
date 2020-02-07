import pandas as pd
import eng_decomp as eng
import random
import dfListFunc as dlist
#df_of_list = {"word": list(list_of_words.keys()), "POS and definitions": list(list_of_words.values())}
#df = pd.DataFrame(data=df_of_list)

def make_randvect(df_list, dimensions):
    dimensions = max(1, dimensions)
    df_list[0].append("Vector representation")
    for i in range(1,len(df_list)):
        vect = [random.random() for i in range(dimensions)]
        df_list[i].append(vect)
    return df_list

def print_df(df_list, vect_index, n=20, ignore=True, parse_len=80):
    if n > len(df_list): n = min(20, len(df_list))
    if ignore:
        for i in range(n):
            print(df_list[i][:vect_index] + ["vector"])
    else: 
        for i in range(n):
            print(str(df_list[i])[:parse_len])

list_of_words = [['Id', 'Word', 'POS', 'Definition', 'vector'],
[0, 'apple', 'noun', 'def: redfruit', 'vector'],
[1, 'fruit', 'noun', 'def category of food', 'vector'],
[2, 'school', 'noun', 'def: place to learn', 'vector'],
[3, 'apple', 'noun', 'def: evil company', 'vector'],
[4, 'microsoft', 'noun', 'def: electronics', 'vector'],
[5, 'computer', 'noun', 'def electronics', 'vector'],
[6, 'lain', 'noun', "let's all love lain", 'vector'],
[7, 'wired', 'noun', 'internet', 'vector']]



fl = eng.get_cd()
#flname = "POS\\newtest.csv"
flname = "Output\\out.csv"
content = eng.open_csv(fl+flname, list_of_words)
print(content)

df_list = [content.columns.values.tolist()]+content.values.tolist()
make_randvect(df_list, 3)
print_df(df_list, 4, ignore=False)

# make a new dataframe from the list
new_df = pd.DataFrame(df_list)
print("###########new data frame########")
print(new_df)
#print(new_df.loc[[0]])
#new_df.to_csv(fl+"Output\\out.csv", index=False, header=False)

# "apple" : [["noun | verb | ... | ...", "def:red fruit", (vector)], ["noun" ,"def: corporation", (vector)]]

df1  = new_df[new_df["Word"].str.contains("apple")]
print(df1)