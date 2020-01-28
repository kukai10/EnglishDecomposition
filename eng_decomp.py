"""goals of this project:
# - the program should be able to take formal and normal (text, speech, everyday conversation, etc) sentences as inputs
# - find clauses that resides in sentences, then clasify them into types of clauses (main, subordinating, etc)
#   as well as classify phrases and clauses that acts , as a whole, as a specific part od speach, ex: adjectival phrases 
"""
"""part of sentences and related vocabs:
- noun
- verb
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
- imperative(mood)
- indicative (mood)
- subjunctive (mood)
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
scriptpath, filename = os.path.realpath(__file__), "" 
for i in range(1,len(scriptpath)+1):
    if scriptpath[-i] == "\\":
        scriptpath = scriptpath[0:-i]
        break
if os.getcwd() != scriptpath: filename = scriptpath + "\\"



