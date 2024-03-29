# -*- coding: utf-8 -*-
"""ai in health.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eShydrIWa7mpf9TxuHZ5HYeHMgYg7umx
"""

# !pip install negspacy
# !pip install scispacy
# !pip install stanza
# !pip install spacy-stanza
# !pip install spacy
import spacy
import stanza
import spacy_stanza
from negspacy.negation import Negex
from negspacy.termsets import termset
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import re as regular





# !pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.1/en_ner_bc5cdr_md-0.5.1.tar.gz


with open('data1.txt','r') as f:
  e= f.read()

data = e.split("-----")
a=data[0].split("\n\n")
records={}
i=0
j=0


for d in data:
    re = d.split("\n\n")

    records.update({i:re})
    i+=1
    
    if i>99:
        break
a=0
incomplete=[]
for i in range(100):
    if len(records[i]) ==3:
        
        a+=1
    else:
        incomplete.append(i)

Records={}
i=0
j=0


for d in data:
    re = d.split("\n\n")
    if i not in incomplete:
        j+=1
        Records.update({j:re})
    
        
    i+=1

with open("structureData.txt", 'w', encoding='utf8') as f:
    for key, value in Records.items():
        f.write('%s:%s\n' % (key, value))

Records[1][1]

from negspacy.termsets import termset
ts = termset("en_clinical")
# customize the term list by adding more negation terms
ts.add_patterns({
            'preceding_negations': ['abstain from','other than','except for','except','with the exception of',
                                    'excluding','lack of','contraindication','contraindicated','interfere with',
                                   'prohibit','prohibits'],
            'following_negations':['negative','is allowed','impossible','exclusionary']
        })

# with open("data") as file:
#     text = file.read()
# #     print(text)
#     para = text.split('\n\n')
#     history = para[0]
history = '''A 34-year-old male accountant comes to the emergency department with acute chest
pain. There is a previous history of occasional stabbing chest pain for 2 years. The current
pain had come on 4 h earlier at 8 pm and has been persistent since then. It is central in
position, with some radiation to both sides of the chest. It is not associated with shortness
of breath or palpitations. The pain is relieved by sitting up and leaning forward. Two
paracetamol tablets taken earlier at 9 pm did not make any difference to the pain.
The previous chest pain had been occasional, lasting a second or two at a time and with
no particular precipitating factors. It has usually been on the left side of the chest
although the position had varied.
Two weeks previously he had an upper respiratory tract infection which lasted 4 days. This
consisted of a sore throat, blocked nose, sneezing and a cough. His wife and two children
were ill at the same time with similar symptoms but have been well since then. He has a history of migraine. In the family history his father had a myocardial infarction at the age of
51 years and was found to have a marginally high cholesterol level. His mother and two sisters, aged 36 and 38 years, are well. After his father’s infarct he had his lipids measured; the
cholesterol was 5.1mmol/L (desirable range !5.5mmol/L). He is a non-smoker who drinks
15 units of alcohol per week.'''
answer = '''The previous chest pains lasting a second or two are unlikely to be of any real significance. Cardiac pain, and virtually any other significant pain, lasts longer than this, and
stabbing momentary left-sided chest pains are quite common. The positive family history
increases the risk of ischaemic heart disease but there are no other risk factors evident
from the history and examination. The relief from sitting up and leaning forward is typical
of pain originating in the pericardium. The ECG shows elevation of the ST segment which
is concave upwards, typical of pericarditis and unlike the upward convexity found in the
ST elevation after myocardial infarction.
The story of an upper respiratory tract infection shortly before suggests that this may well
have a viral aetiology. The viruses commonly involved in pericarditis are Coxsackie B
viruses. The absence of a pericardial rub does not rule out pericarditis. Rubs often vary in
intensity and may not always be audible. If this diagnosis was suspected, it is often worth
listening again on a number of occasions for the rub. Pericarditis often involves some adjacent myocardial inflammation and this could explain the rise in creatine kinase.
Pericarditis may occur as a complication of a myocardial infarction but this tends to occur
a day or more later – either inflammation as a direct result of death of the underlying heart
muscle, or as a later immunological effect (Dressler’s syndrome). Pericarditis also occurs
as part of various connective tissue disorders, arteritides, tuberculosis and involvement
from other local infections or tumours. Myocardial infarction is not common at the age of
34 years but it certainly occurs. Other causes of chest pain, such as oesophageal pain or
musculoskeletal pain, are not suggested by the history and investigations.
Thrombolysis in the presence of pericarditis carries a slight risk of bleeding into the pericardial space, which could produce cardiac tamponade. This arises when a fluid (an effusion, blood or pus) in the pericardial space compresses the heart, producing a paradoxical
pulse with pressure dropping on inspiration, jugular venous pressure rising on inspiration
and a falling blood pressure. In this case, the evidence suggests pericarditis and thrombolysis is not indicated. The ECG and enzymes should be followed, the patient re-examined
regularly for signs of tamponade, and analgesics given.
A subsequent rise in antibody titres against Coxsackie virus suggested a viral pericarditis.
Symptoms and ECG changes resolved in 4–5 days. An echocardiogram did not suggest any
pericardial fluid and showed good left ventricular muscle function. The symptoms settled
with rest and non-steroidal anti-inflammatory drugs.'''

nlp_sd = spacy.load("en_ner_bc5cdr_md")
nlp_sd.add_pipe("negex", config={"ent_types":["CHEMICAL","DISEASE"]})
tt_nlp=spacy_stanza.load_pipeline('en', package='mimic', processors={'ner': 'i2b2'})
tt_nlp.add_pipe("negex", config={"ent_types":["TEST",'TREATMENT']})
nlp_age=spacy.load("en_core_web_sm")
nlp_age=spacy.load("en_core_web_sm")

def gender(history,nlp_sd):
  sex = nlp_sd.get_pipe('attribute_ruler')
  sex.add([[{"TEXT":"male"}],[{"TEXT":"man"}],[{"TEXT":"boy"}],[{"TEXT":"him"}],[{"TEXT":"he"}],[{"TEXT":"his"}]],{"LEMMA":"Male"})
  sex.add([[{"TEXT":"female"}],[{"TEXT":"woman"}],[{"TEXT":"girl"}],[{"TEXT":"her"}],[{"TEXT":"she"}]],{"LEMMA":"Female"})
  sex_doc = nlp_sd(history)
  gender =["Male","Female"]
  for token in sex_doc:
      if str(token.lemma_) in gender:
          
          if token.lemma_ == "Male":
              
              return "M"
          else:
              return "F"
          break

gender(Records[1][0],nlp_sd)

# for extracting age


def determineAge(history,nlp_age):
  
  doc_age=nlp_age(history)
  for ent in doc_age.ents:
    if ent.label_ == "DATE" and regular.search('years-old|years old|year-old|year old',ent.text):
      return ent.text

determineAge(Records[1][0],nlp_age)

for i in range(1,len(Records)):
  # doc_age=determineAge(Records[i][0])

  # doc_sex=gender(Records[1][0])

  # for exracting symptoms and pre medications
  doc_s = nlp_sd(Records[i][0])

  # for e in doc_s.ents:
  #     print(e.text, e._.negex, e.label_)
  # print('-'*10)

  # for exracting diagnosis
  doc_d = nlp_sd(Records[i][2])

  # for e in doc_d.ents:
  #     print(e.text, e._.negex, e.label_)
  # print('-'*10)

  # for extracting test and treatment
  answer_doc_tt_nlp=tt_nlp(Records[i][2])

  # for e in answer_doc_tt_nlp.ents:
  #   print(e.text, e._.negex, e.label_)

patient_records = {}

bad_data = ['alcohol', 'treatment', 'examination', 'death']

for i in range(1, len(Records)):
  symptoms =set()
  pre_medications =set()
  diagnosis = set()
  tests = set()
  treatments= set()
  age=determineAge(Records[i][0],nlp_age)
  sex=gender(Records[i][0],nlp_sd)
# sy
  for e in doc_s.ents:
    # print(e.text, e._.negex, e.label_)
      if str(e._.negex) == "False" and str(e.label_) == "DISEASE":
       symptoms.add(e.text)
      if str(e._.negex) == "False" and str(e.label_) == "CHEMICAL" and str(e.text).lower() not in bad_data:
        pre_medications.add(e.text)
    #di
  for e in doc_d.ents:
      # print(e.text, e._.negex, e.label_)
      if str(e._.negex) == "False" and str(e.label_) == "DISEASE":
          diagnosis.add(e.text)

  #test
  for e in answer_doc_tt_nlp.ents:
      # print(e.text, e._.negex, e.label_)
      if str(e._.negex) == "False" and str(e.label_) == "TEST" and str(e.text).lower() not in bad_data:
          tests.add(e.text)

      if str(e._.negex) == "False" and str(e.label_) == "TREATMENT" and str(e.text).lower() not in bad_data:
          treatments.add(e.text)

  patient_records.update({i:{"Age":age,
                             "Sex":sex,
                              "Symptoms":list(symptoms),
                             "Pre_Medication":list(pre_medications),
                             "Test":list(tests),
                             "Diagnosis":list(diagnosis),
                             "Treatment":list(treatments)}})



"""todo: dictionary: unhashable list, set
      examination
      many dataset ...in loop formating
      mongodb store
      react visualize

"""