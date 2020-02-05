import pandas as pd
list_of_words = {
    "apple": [["noun"], ["def: red fruit"]], 
    "fruit": [["noun"], ["def: category of food"]],
    "School": [["noun"], ["def: place to learn"]],
    "apple": [["noun"], ["def: evil company that brainwash people and force them to pay 10x the actual value"]],
    "microsoft": [["noun"], ["def: another evil company that monitize their product, not as evil as apple"]],
    "computer": [["noun"], ["electronics used to code and go to reddit"]],
    "lain": [["noun"], ["let's all love lain"]],
    "wired": [["noun"], ["a superior synonym for internet"]]
    }




df_of_list = {"word": list(list_of_words.keys()), "POS and definitions": list(list_of_words.values())}
df = pd.DataFrame(data=df_of_list)
print(df.head())

print(df["apple"])