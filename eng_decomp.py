import os
import pickle
import pandas as pd
import numpy as np

def get_cd():
    scriptpath, filename = os.path.realpath(__file__), "" 
    for i in range(1,len(scriptpath)+1):
        if scriptpath[-i] == "\\":
            scriptpath = scriptpath[0:-i]
            break
    if os.getcwd() != scriptpath: filename = scriptpath + "\\"
    return filename

def load_pickle(filepath, default):
    """load an existing pickle file or make a pickle with default data and return the pickled data"""
    try:
        with open(filepath, "rb") as f:
            x = pickle.load(f)
    except Exception:
        x = default
        with open(path, "wb") as f:
            pickle.dump(x, f)
    return x

def open_csv(filepath, default):
    try:
        x = pd.read_csv(filepath, error_bad_lines=False)
    except Exception:
        print("exception, the filename you requested to open was not found.")
        if (input("do you want to make a new file? 1 for yes, 0 for no") == 1):
            default.to_csv(filepath, index=False, header=False)
    return x;
    
def save_df_to_csv(filepath, content):
    content.to_csv(filepath, index=False, header=False)

def save_pickle(filepath, content):
    content.to_pickle(filepath)

def edit_dataframe(data_df):
    pass

def load_metadata(filepath):
    try:
        pass
    except Exception:
        pass
    return []

def decide_mode(modes):
    print("from the following, pick the mode to start the system.")
    index_list, usr_input = [], ""
    for index, value in enumerate(modes):
        print(index, value)
        index_list.append(str(index))
    while(usr_input not in modes and usr_input not in index_list):
        usr_input = input("Pls enter the mode to boot the system:  ")
        switch = True if usr_input in index_list else False 
    if switch: usr_input = index_list[int(usr_input)]
    return usr_input

def make_NN(node_num, layer_num, architecture):
    pass

def train_NN(NN, sentences):
    pass

def test_NN(NN, sentences):
    pass

def tokenize(sentence):
    pass

def visualize_tree(sentence):
    pass

def parse_text(sentence):
    pass

def backpropagate():
    pass

def sigmoid():
    pass

def chain_rule():
    pass

def calculate_node_val():
    pass

def add_to_dictionary():
    pass

def update_single_word():
    #dot product and upgrade
    pass

def use_cuda():
    pass

def POS_markov_chain(inputPOS, outputPOS):
    markovChain = [
        ["Articles", "Noun", "verb", "gerund"], 
        [],





    ]
    
def main():
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
    df_def = pd.DataFrame.from_dict(list_of_words)
    print(df_def)
    mode_option = ["training", "add input", "create output", "exit"]
    mode = decide_mode(mode_option)
    if mode == mode_option[0]:
        current_dir = get_cd()
        input_file = current_dir+"Input\\"
        output_file = current_dir+"Output\\"
        POS_file = current_dir+"POS\\"
        pickle_name = current_dir+"Eng.pickle"
        csv_names = ["Pronouns.csv"] #["Articles.csv", "common_noun.csv", "proper_noun.csv"]
        cvsfiles = open_csv(POS_file+csv_names[0])
        for index, row in cvsfiles.iterrows():
            if index < 10:
                print(row.to_frame().T)
        eng_dict = {}

    elif mode == mode_option[1]:
        pass
    elif mode == mode_option[2]:
        pass
    elif mode == mode_option[3]:
        pass
    #pickle.dump(data, pickle_on)
    #pickle_on.close()
    #cvsfiles.close()

    #do a syntactical decomposition and meaning decomposition
    # look for errors
    # put the words in a NLP NN
    # example possesive before a gerund, is what and who a subject pronoun?


















if __name__=="__main__":  
    main()