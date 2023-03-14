import re
import itertools as it

# def findNear(text,word1,word2,precede=False):
#     wa = re.findall(rf"{word1}" +r"\W+(?:\w+\W+){0,0}?" + rf"{word2}" + r"\b",prepped_text)
#     if precede==False:
#         wa1 = re.findall(rf"{word2}" +r"\W+(?:\w+\W+){0,0}?" + rf"{word1}" + r"\b",prepped_text)
#         return wa, wa1
#     else:
#         return wa

def findSimp(text,word1,word2,precede=False):
    '''
    precede = False means word1 and word2 are looked at with either being first word
    precede = True means word1 must be first, word2 must be second
    
    '''

    wa = re.findall(rf"{word1}" +r"\W" + rf"{word2}" + r"\b",prepped_text)
    wal = len(wa)
    if precede==False:
        wa1 = re.findall(rf"{word2}" +r"\W" + rf"{word1}" + r"\b",prepped_text)
        wal1 = len(wa1)
        return wal + wal1
    else:
        return wal

def findSuperSimp(text,word):
    return len(re.findall(rf"{word}",text))


text0 = ['''

As part of an experimental e-flows ecologic study, we flow monitored the instream flow and water 
levels of a freshwater stream for several months. Our goal was to determine the optimum maintenance 
practices for this stream to ensure an acceptable flow and water level, while minimizing the 
need for flushing and compensating for any negative impacts on the environment. We also studied
the effects of flooding on the stream and developed a compensation plan to augment its natural
restoration processes. Our research showed that careful management of water discharge and in-stream
maintenance can lead to significant improvements in the stream's ecological and environmental health.

To achieve the desired results, we conducted regular flushing activities to remove excess sediment 
and debris from the stream. We also implemented a compensation program to provide financial support
to landowners who were e-flows willing to participate in the restoration efforts. This program not only helped
to restore the natural flow and water levels of the stream, but it also had a positive impact on the local community.

Our study revealed that in-stream maintenance activities should be conducted on a regular basis to ensure
the long-term health of the stream. This includes activities such as removing debris, stabilizing banks,
and planting vegetation to eflow prevent erosion. We also found that the stream's flow and water level are 
closely related to the surrounding environment, and any changes to the land use or development practices
can have a significant impact on the stream's health.

Overall, our research demonstrates the importance of careful management of freshwater resources and the 
need for ongoing monitoring and restoration efforts. By implementing sustainable practices and working 
collaboratively with local communities, we can ensure a healthy and thriving ecosystem for future generations.

''']

prepped_text = text0[0].replace("\n","")




''' 

search queries

\S* means any non whitespace character repeated an one or more number of times
\S means any single non whitespace character
\S\S means any two non whitespace characters, etc...

https://www.py4e.com/lessons/regex

'''

combo1_1 = ["ecologic\S*",'environmental\S*', 'minim\S\S', 'acceptable',
'augment\S*', 'compensation', 'experimental', 'flushing', 
'in-stream', 'instream', 'maintenance', 'optimum', 'restor\S*']

combo1_2 = ["flood\S*", 'flow\S*', 'freshwater\S','water', 
'water level\S', 'discharge']

combo2_1 = ['conservation','cultural','cut-off','cutoff','design','fish','functional',
'management','maximum','natural','preference','protection','rating','regime','residual',
'right\S','sanita\S*','scenario','standard','suitable','surplus','sustainable','threshold',
'use','vital']
combo2_2 = ['flow\S']

combo3_1 = ['downstream','dam','reservoir']
combo3_2 = ['water release\S','flow release\S']

combo4_1 = ['controlled','artificial']
combo4_2 = ['flood']

combo5_1 = ['hydrologic\S*']
combo5_2 = ['requirement','manipulation\S']

combo6_1 = ['\S*flow\S','freshwater\S','\S*water\S*','water level\S']
combo6_2 = ['abstraction','allocation','criteri\S*','delivery','demand\S','guideline\S',
'need','provision','requirement','reserv\S*','restrict\S*','withdrawal']


x1 = list(it.product(combo1_1,combo1_2))
x2 = list(it.product(combo2_1,combo2_2))
x3 = list(it.product(combo3_1,combo3_2))
x4 = list(it.product(combo4_1,combo4_2))
x5 = list(it.product(combo5_1,combo5_2))
x6 = list(it.product(combo6_1,combo6_2))
xeflows1 = ['e-flow']
xeflows2 = ['e-flows']

X = [x1,x2,x3,x4,x5,x6,xeflows1,xeflows2]
for idx,i in enumerate(X):
    if idx in [0,1,5]:
        for j in i:
            k = findSimp(prepped_text,j[0],j[1],precede=False)
            if k > 0:
                print(f'found match')
                break
        break

    elif idx in [2,3,4]:
        for j in i:
            k = findSimp(prepped_text,j[0],j[1],precede=True)
            if k > 0:
                print('found match')
                break
        break

    elif idx in [6,7]:
        for j in i:
            k = findSuperSimp(prepped_text,j)
            if k > 0:
                print('found match')
                break
        break
