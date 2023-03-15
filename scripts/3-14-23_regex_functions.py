#import cProfile
import re
#import itertools as it

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

    regexp = f"{word1}\\W{word2}\\b"
    if precede==False:
        regexp = f"({regexp})|({word2}\\W{word1}\\b)"

    wa = re.findall(regexp, text)
    wal = len(wa)

    return(wal)


def findSuperSimp(text,word):
    return len(re.findall(f"{word}", text))


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

\S* matches any non whitespace character repeated zero or more times
\S? means any single non whitespace character, zero or one time
\S\S means any two non whitespace characters, etc...

https://www.py4e.com/lessons/regex

'''

combo1_1 = ["ecologic\S*",'environmental\S*', 'minim\S\S', 'acceptable',
            'augment\S*', 'compensation', 'experimental', 'flushing',
            'in[-]?stream', 'maintenance', 'optimum', 'restor\S*']

combo1_2 = ["flood\S*", 'flow\S*', '\S*water\S*',
            'water level\S?', 'discharge']

combo2_1 = ['conservation', 'cultural', 'cut[-]?off', 'design', 'fish', 'functional',
            'management', 'maximum', 'natural', 'preference', 'protection', 'rating', 'regime', 'residual',
            'right\S?', 'sanita\S*', 'scenario', 'standard', 'suitable', 'surplus', 'sustainable', 'threshold',
            'use', 'vital']
combo2_2 = ['flow\S?']

combo3_1 = ['downstream', 'dam', 'reservoir']
combo3_2 = ['water release\S?', 'flow release\S?']

combo4_1 = ['controlled', 'artificial']
combo4_2 = ['flood\S?']

combo5_1 = ['hydrologic\S*']
combo5_2 = ['requirement\S?', 'manipulation\S?']

combo6_1 = ['\S*flow\S?', 'freshwater\S?', '\S*water\S*', 'water level\S?']
combo6_2 = ['abstraction\S?', 'allocation\S?', 'criteri\S*', 'deliver\S*', 'demand\S?', 'guideline\S?',
            'need\S?', 'provision', 'requirement\S?', 'reserv\S*', 'restrict\S*', 'withdrawal\S?']

#Join all strings in a list with | signs and parentheses
def recomb(in_str):
    if isinstance(in_str, list):
        return(f"({'|'.join(f'({w})' for w in in_str)})")
    else:
        return(in_str)

#Profile whether faster to use product upstream or to use | in regex
# with cProfile.Profile() as prof:
#     for x in range(100000):
#         x1 = list(it.product(combo1_1, combo1_2))
#         for j in x1:
#             findSimp(prepped_text, j[0], j[1],precede=False)
# prof.print_stats()
#
# with cProfile.Profile() as prof:
#     x1 = [recomb(combo1_1), recomb(combo1_2)]
#     for x in range(100000):
#         findSimp(prepped_text,x1[0],x1[1],precede=False)
# prof.print_stats()
###### Using | in regex exp is 6.5 faster

searchdict = {'x1': ['with', [recomb(combo1_1), recomb(combo1_2)]],
              'x2': ['with', [recomb(combo2_1), recomb(combo2_2)]],
              'x3': ['pre', [recomb(combo3_1), recomb(combo3_2)]],
              'x4': ['pre', [recomb(combo4_1), recomb(combo4_2)]],
              'x5': ['pre', [recomb(combo5_1), recomb(combo5_2)]],
              'x6': ['with', [recomb(combo6_1), recomb(combo6_2)]],
              'xeflows': [None, rf'e[-]?flow\S?']
              }

def combo_refind(in_searchdict, text):
    for regexp_combo in in_searchdict.values():
        if regexp_combo[0] == 'with':
            k = findSimp(text, regexp_combo[1][0], regexp_combo[1][1], precede=False)
        elif regexp_combo[0] == 'pre':
            k = findSimp(text, regexp_combo[1][0], regexp_combo[1][1], precede=True)
        elif regexp_combo[0] is None:
            k = findSuperSimp(text, regexp_combo)
        else:
            break

        return (k)
        # if k > 0:
        #
        #     break


combo_refind(in_searchdict = searchdict,
             text = prepped_text)