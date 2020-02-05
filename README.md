# EnglishDecomposition
 Decompose sentences and paragraphs using clause analysis and part of speach

 Languages: [English](README.md), [日本語/Japanese](README.jp.md)
 - [General and Getting Started](#getting-started)
     - [Motivation for the Project](#intro)
     - [Dependencies](#dependencies)
 - [list of POS implimented in this program](#POS)
 - [Functions](#functions)
     - [Clause detection](#general-overview)
     - [Tokenizing](#techniques)
     - [Neural Net](#NN)
     - [Performance](#performance)
     - [Error detection](#error)
 - [Explanatory Notes](#explanation)
     - [Limitation](#limitation)



--- 
<a id = "getting-started"></a> 
##General and Getting Started:


---
<a id = "intro"></a> 
###Motivation for this project
When I was in my English class, I learned about a class of sentences called "garden-path sentences", correct sentences designed to lure the reader in making a wrong interpertation.  It's called "garden-path sentences" because the sentences lure the reader into a dead-end and the reader needs multiple attempts at decoding the words.  Many online translators and grammer/spelling fixing programs fails to understand these garden path sentences. Heck, if you know another language, you can decode what the program's interpertation by translating the sentence. A very funny problem, but worrying to me, is the fact that google-translate interperts "the old man the boat" as two noun prase, "the old man" and "the boat".  Google-translate is the go-to translator for many people, even I use it for English to Japanese and vice versa; but google-translator have its issues and they haven't attempted to make their models better or fix these problems.

The goal of this project is to make functions that is required for processing natural language and impliment a neural network that takes in the processed data and respond in a natural manner. 

Dependencies 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

High level functions:

---
<a id = "getting-started"></a> 
##POS

-----------|-----------------------------|-----------|-------


Noun | verb | adjectives | adverb | coordinating conjunction
pronoun (subject, object, indefinite, possessive, reflexive, relative) | appositives | articles (a, an, the, null) | determiner | 
participle (verb, ussually with -ed or -ing, that act adjectivally) | prepositions
Conjucntive adverb | gerunds | quantifier

verb tense: past, present, future, perfect, imfinitive 
comma | dash | semicolon | hyphen | colon | approstrophe | quotes | ending punctuations
interuptives
Parallel structure
restrictive vs non-restrictive
moods:
imperative | indicative | subjunctive
split infinitive
fronting * 


<a id = "functions"></a> 
Functionalities of the program
 - decompose the input and create an appropriate output
 - Take formal and normal speech
 - POS (part of speech) detector and tokenize the inputs and outputs
 - Learn and figure out the meaning of the sentence
 - flexible dictionary
 - understand stylistic liberties
 - classify clauses (main clauses, restrictive vs non-restrictive)
 - figure out the functionality of the clause (Ex: some clauses act adjectivaly)





<a id = "error"></a>
The program will look for the following errors in the output:
 - Subject-verb agreement
 - semicolon error (mc; cordinating conjunction, mc) or list with internal punctuation
 -oxford/serial comma
 -appostrophie error
 - comma splice and fused sentences
 - sentence fragments
 - possesive before gerunds
 - misplaced modifier
 - commonly misspelled words or confused words (effect vs affect, alot --> a lot)