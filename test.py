import pandas as pd
import eng_decomp as eng
import random
import dfListFunc as dlist
import time
import numpy as np
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

current_directory = eng.get_cd()


filename1 = "POS\\newtest.csv"
filename2 = "Output\\out.csv"
filename3 = "Input\\file1.csv"
filename4 = "input\\file2.csv"

"""
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
#df1  = new_df[new_df["Word"].str.contains("apple")]
#print(df1)
"""
# 1, 000, 000
#1000
time1 = time.time()
df2 = pd.DataFrame(np.random.rand(500000, 300))
time2 = time.time()
eng.save_df_to_csv(current_directory+"Input\\df2.csv", df2)
time3 = time.time()
eng.save_pickle(current_directory + "Input\\df2.pkl", df2)
time7 = time.time()

print("to make 1st df", time2-time1)
print("to save data frame", time3-time2, "and as a whole took", time3-time1)
print("to save pickle:", time7-time3)

nump = np.zeros([300000, 50])
for i in range(500):
    a = random.randint(0, 300000)
    nump[a] = np.random.rand(50)
other = pd.DataFrame(nump)

time4 = time.time()
print("made weird array size 50: ", time4-time3)
df2 = df2.join(other, lsuffix='_caller', rsuffix='_other')
time5 = time.time()
print("joining", time5-time4)
eng.save_df_to_csv(current_directory+"Input\\df2joined.csv", df2)
time6 = time.time()
print("saving bigger csv", time6-time5)
eng.save_pickle(current_directory + "Input\\df2joined.pkl", df2)
print("end", time.time() - time6)