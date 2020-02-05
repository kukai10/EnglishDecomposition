"""goals of this project:
# - the program should be able to take formal and normal (text, speech, everyday conversation, etc) sentences as inputs
# - find clauses that resides in sentences, then clasify them into types of clauses (main, subordinating, etc)
#   as well as classify phrases and clauses that acts , as a whole, as a specific part od speach, ex: adjectival phrases 
"""
"""part of sentences and related vocabs:
- noun, verb
- adjective, modify noun, pronoun, or other adjectives, clauses can act adjectivally
- adverb, modify verb, ussually answers the 4W and H ("where", "when", "what", "who", "How")
- coordinating conjunction (and, but, so, or , for, nor, yet)
- pronoun (subject, object, indefinite, possesive, reflexive, relative)
- appositives
- articles/ determiner (a, an, the, no articles)
- conjunctive adverb (However, therefore, thus, etc)
- dashes
- quantifier
- gerunds
imperative(mood), indicative (mood), subjunctive (mood)
- infinitve verbs
- interruptive
- main clause
- restrictive vs non-restricitve
- parallel structure
- participle (verb, ussually with -ed or -ing, that act adjectivally)
- tense (past, present, future, perfect)
- preposition, denote relationships (about, up, down, on, in, around, among, with, ..., etc)
- prepositional phrases
- split infinitive
- fronting
- punctuation, (comma, colon, semicolon, appostrophe, dash, quotes, end punctuation)
"""
"""thigs to look out for or errors to recognize:
- subject-verb agreement error
- semicolon error (mc ; coordinating conjunction, mc), or lists with internal punctuation
- oxford/serial comma
- appostrophie error, comma splice
- sentence fragment or run-on sentences
- stylistic liberties
- possesive before gerunds
- missplaced modifier
- commonly misspelled words
- common confusing words (affect vs effect)
"""
"""things required:
- function that decompose the input
- output with the description
- part of speach detector
- learn meaning and figure the meaning of the sentence
- multiple input and output files
- saves floating value in txt
- expand dictionary
- relationship between other words
- king - man = queen, video - image = voice
- not coke = pepsi (negation)
"""
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

def open_csv(filepath):
    #list_of_words = {"apple": [["noun"], ["def: red fruit"]], "fruit": [["noun"], ["def: category of food"]]}
    #df_def = pd.DataFrame.from_dict(list_of_words)
    #print(df_def)
    try:
        x = pd.read_csv(filepath, error_bad_lines=False)
    except Exception:
        print("except")
        #df_def.to_csv()

def save_csv(filepath, content):
    content.to_csv(filename)

def save_pickle(filepath, context):
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
    
def main():
    list_of_words = {"apple": [["noun"], ["def: red fruit"]], "fruit": [["noun"], ["def: category of food"]]}
    df_def = pd.DataFrame.from_dict(list_of_words)
    print(df_def)
    mode_option = ["training", "add input", "create output", "exit"]
    mode = decide_mode(mode_option)
    current_dir = get_cd()
    input_file = current_dir+"Input\\"
    output_file = current_dir+"Output\\"
    POS_file = current_dir+"POS\\"
    pickle_name = current_dir+"Eng.pickle"
    csv_names = ["Pronouns.csv"] #["Articles.csv", "common_noun.csv", "proper_noun.csv"]
    cvsfiles = open_csv(POS_file+csv_names[0])
    for index, row in cvsfiles.iterrows():
        if index < 10:
            #print(index, row)
            print(row.to_frame().T)

    eng_dict = {}
    
    # a key: value pair in the dictionary will look like the following:
    #  "___word___" : [
    #                   [["tags"], ["definitions, meaning"], (vector)], 
    #                   [[], []], ...
    #                  ]

    #pickle.dump(data, pickle_on)
    #pickle_on.close()
    #cvsfiles.close()

    #do a syntactical decomposition and meaning decomposition
    # look for errors
    # put the words in a NLP NN
    # example possesive before a gerund, is what and who a subject pronoun?

if __name__=="__main__":  
    main()