'''
# for later
with open("GermanSyllable\input.txt") as file:
    l = [x for x in file.read().split(' ')]
'''
test = 'Silbentrennung Worttrennung Zerlegung schule Hauptgrundlage Himbeere hinter zusammengesetzter Muster Hamster fenster hinstellen katze witzlos krapfen über'
# Kastrat and Foxtrott didn't pass the test (rule VtzV > Vt-zV and VCtzV > VCt-zV)
test2 = 'Diät Auto Seeufer Katze Tatze Pfütze putzen platzen Bürste Kiste Hamster Fenster hinstellen darstellen erstarren plötzlich Postauto Kratzbaum boxen heben rodeln Schifffahrt Mussspiel wichtigsten' 
# complex forms of vocals(V) and consonants(C)
complexVC = {
    # check if it needs to be like this or just one V or C?
    'ei' : 'VV',
    'ai' : 'VV',
    'ey' : 'VV',
    'ay' : 'VV',
    'eu' : 'VV',
    'äu' : 'VV',
    'ie' : 'VV',
    'au' : 'VV',
    'aa' : 'VV',
    'ee' : 'VV',
    'oo' : 'VV',
    'sch' : 'CCC',
    'ch' : 'CC',
    'ck' : 'CC',
    'qu' : 'CC',
    'ph' : 'CC',
    'tsch' : 'CCCC' # multiple forms (?)
}

# simple form of vocals(V) and consonants(C)
simpleVC = {
    'a' : 'V',
    'e' : 'V',
    'i' : 'V',
    'o' : 'V',
    'u' : 'V',
    'ä' : 'V',
    'ö' : 'V',
    'ü' : 'V',
    'b' : 'C',
    'c' : 'C',
    'd' : 'C',
    'f' : 'C',
    'g' : 'C',
    'h' : 'C',
    'j' : 'C',
    'k' : 'C',
    'l' : 'C',
    'm' : 'C',
    'n' : 'C',
    'p' : 'C',
    'q' : 'C',
    'r' : 'C',
    's' : 'C',
    't' : 'C',
    'v' : 'C',
    'w' : 'C',
    'x' : 'C',
    'y' : 'C',
    'z' : 'C',
    'ß' : 'C'
}

# list of prefixes that need to be separated 
prefix=['unter', 'über', 'hinter', 'wider', 'wieder', 'weiter', 'zurück', 'zurecht', 'zusammen', 'hyper', 'inter', 
        'haupt', 'nach', 'stink', 'stock', 'super', 'trans', 'durch', 
        'hoch', 'tief', 'niss', 'fehl', 'miss', 
        'ein', 'her', 'hin', 'auf', 'aus', 'dis', 'dar', 'los', 'mit', 'von', 'vor', 'weg', 'ver', 'zer', 'miß', 'niß', 'non', 'kon', 'tod', 'erz', 'ent', 
        'an', 'ab', 'in', 'um', 'un', 'ur', 'er', 'ex']

# ARGUMENTS: list of syllables in the word and corresponding list of V and C
def divider(syllableList, VClist):
    acc=0
    # we will divide the word into syllables, 
    # each syllable will be one element in the list
    # same for their corresponding list of V and C
    wordlist=[]
    vclist=[]

    # at first if there isn't prefix there is just one element (whole word) in the list
    # at each iteration the word is separated into syllables
    for syllable in syllableList:
        # we search for corresponding list of V and C 
        syllableVC=VClist[syllableList.index(syllable)]

        # rule VCCV --> VC-CV 
        if 'VCCV' in syllableVC:
            # if a patter VCCV is in the syllable we divide it into two syllables
            sy1=syllable[:syllableVC.find('VCCV')+2]
            sy2=syllable[syllableVC.find('VCCV')+2:syllableVC.find('VCCV')+5]

            # same for corresponding V and C list
            sy1VC=syllableVC[:syllableVC.find('VCCV')+2]
            sy2VC=syllableVC[syllableVC.find('VCCV')+2:syllableVC.find('VCCV')+5]

            # get the remaining part of a syllable
            # same for corresponding V and C list 
            syllable=syllable.replace(sy1+sy2,'')
            syllableVC=syllableVC.replace(sy1VC+sy2VC,'',1)

            # if the remaining part is less then 2 letters we add it to the second divided syllables
            if len(syllable)<3:
                sy2+=syllable
                wordlist.append(sy1)
                wordlist.append(sy2)
            else:
                wordlist.append(sy1)
                wordlist.append(sy2)
                wordlist.append(syllable)
            # same for corresponding V and C list
            if len(syllableVC)<3:
                sy2VC+=syllableVC
                vclist.append(sy1VC)
                vclist.append(sy2VC)
            else:
                vclist.append(sy1VC)
                vclist.append(sy2VC)
                vclist.append(syllableVC)
        # all the other rules follow the same structure as the first rule
        # rule VCCCV --> VCC-CV
        elif 'VCCCV' in syllableVC:
            sy1=syllable[:syllableVC.find('VCCCV')+3]
            sy2=syllable[syllableVC.find('VCCCV')+3:syllableVC.find('VCCCV')+6]

            sy1VC=syllableVC[:syllableVC.find('VCCCV')+3]
            sy2VC=syllableVC[syllableVC.find('VCCCV')+3:syllableVC.find('VCCCV')+6]

            syllable=syllable.replace(sy1+sy2,'')
            syllableVC=syllableVC.replace(sy1VC+sy2VC,'',1)

            if len(syllable)<3:
                sy2+=syllable
                wordlist.append(sy1)
                wordlist.append(sy2)
            else:
                wordlist.append(sy1)
                wordlist.append(sy2)
                wordlist.append(syllable)
            if len(syllableVC)<3:
                sy2VC+=syllableVC
                vclist.append(sy1VC)
                vclist.append(sy2VC)
            else:
                vclist.append(sy1VC)
                vclist.append(sy2VC)
                vclist.append(syllableVC)

        # VCCCCV --> VCC-CCV
        # not a defined rule but I've noticed that it appears often
        elif 'VCCCCV' in syllableVC:
            sy1=syllable[:syllableVC.find('VCCCCV')+3]
            sy2=syllable[syllableVC.find('VCCCCV')+3:syllableVC.find('VCCCCV')+7]

            sy1VC=syllableVC[:syllableVC.find('VCCCCV')+3]
            sy2VC=syllableVC[syllableVC.find('VCCCCV')+3:syllableVC.find('VCCCCV')+7]

            syllable=syllable.replace(sy1+sy2,'')
            syllableVC=syllableVC.replace(sy1VC+sy2VC,'',1)

            if len(syllable)<3:
                sy2+=syllable
                wordlist.append(sy1)
                wordlist.append(sy2)
            else:
                wordlist.append(sy1)
                wordlist.append(sy2)
                wordlist.append(syllable)
            if len(syllableVC)<3:
                sy2VC+=syllableVC
                vclist.append(sy1VC)
                vclist.append(sy2VC)
            else:
                vclist.append(sy1VC)
                vclist.append(sy2VC)
                vclist.append(syllableVC)

        # rule VCV --> V-CV
        elif 'VCV' in syllableVC:
            #print('VCV')
            sy1=syllable[:syllableVC.find('VCV')+1]
            sy2=syllable[syllableVC.find('VCV')+1:syllableVC.find('VCV')+4]

            sy1VC=syllableVC[:syllableVC.find('VCV')+1]
            sy2VC=syllableVC[syllableVC.find('VCV')+1:syllableVC.find('VCV')+4]

            syllable=syllable.replace(sy1+sy2,'')
            syllableVC=syllableVC.replace(sy1VC+sy2VC,'',1)

            if len(syllable)<3:
                sy2+=syllable
                wordlist.append(sy1)
                wordlist.append(sy2)
            else:
                wordlist.append(sy1)
                wordlist.append(sy2)
                wordlist.append(syllable)
            if len(syllableVC)<3:
                sy2VC+=syllableVC
                vclist.append(sy1VC)
                vclist.append(sy2VC)
            else:
                vclist.append(sy1VC)
                vclist.append(sy2VC)
                vclist.append(syllableVC)
        
        # Not implementet rules:
            # tsch rule ???
            # VstV > Vs-tV (BUT THE TEST CASES PASSED)
            # VCstV > VCs-tV (BUT THE TEST CASES PASSED)
            # VstCV > Vs-tCV !!! TEST FAILED 
            # VxtCV > Vx-CV  !!! TEST FAILED
            # VtzV > Vt-zV (BUT THE TEST CASES PASSED)
            # VCtzV > VCt-zV ???
            # VtzCV > Vtz-CV (BUT THE TEST CASES PASSED)
            # VpfV > Vp-fV (BUT THE TEST CASES PASSED)
            # VCpfV > VCp-fV ???
            # VpfCV > Vpf-CV ???
            # Knie rule ???


        # if a syllable can't be broken down it stays the same
        else:
            acc+=1
            wordlist.append(syllable)
            vclist.append(syllableVC)

    # if no syllable can be broken down further we return the current list of syllables
    if acc == len(syllableList):
        return wordlist
    # else we apply divider on broken down list of syllables
    else:
        return divider(wordlist,vclist)
            

# split sentence into words 
test = test.split(' ')
keys = list(complexVC.keys())

for word in test:
    wordlist=[]
    vclist=[]
    acc=['']*len(word)
    word=word.lower()
    prefi=''

    # first saparate the prefix
    for pre in prefix:
        if pre in word and word.find(pre)==0:
            prefi=pre
            break

    # check for complex forms of vocals (V) and consonants (c)
    # Can complex forms have more then one instances?
    # we mark them like upper letters so we don't check them later
    for k in keys:
        if k in word:
            acc[word.find(k)]=complexVC[k]
            word=word.replace(k, k.upper())

    # check V or C for the remaining letters
    for i in range(len(word)):
        if(not word[i].isupper()): 
            acc[i]=simpleVC[word[i]]

    temp=''.join(acc)
    word=word.lower()

    # if the prefix exists add the prefix and the rest of the word to list sparatly
    # same for their corresponding list of V and C
    if prefi != '':
        lpre=len(prefi)
        vclist.append(temp[:len(prefi)])
        vclist.append(temp[len(prefi):])
        wordlist.append(prefi)
        wordlist.append(word.replace(prefi,''))
    # else they are one element in the list
    else:
        wordlist.append(word)
        vclist.append(''.join(acc))


    syllables=divider(wordlist,vclist)
    print(syllables)

