# Yoon Hyup Hwang, Zhou Tan
import functools
import math
import operator

def main():
    print("This project is collaboratively finished by Yoon Hyup Hwang and Zhou Tan")
    fileName = input("Type in your file name('q' to quit the program): ")
    while fileName != 'q':
        text = readFile(fileName)
        sentences = getSentences(text)
        sentenceCount = getSentenceCount(sentences)
        dictionary = {}
        wordCount = getWordCount(sentences, dictionary)
        longWordCount = getLongWordCount(sentences)
        polysyllabicWordCount = getPolysyllableWordCount(sentences)
        letterCount = getLetterCount(sentences)
        syllableCount = getSyllableCount(sentences)
        KincaidMeasure = getKincaidMeasure(sentenceCount, wordCount, 
                                           syllableCount)
        print("1. KincaidMeasure: ", KincaidMeasure)
        ARImeasure = getARImeasure(sentenceCount, wordCount, letterCount)
        print("2. ARImeasure: ", ARImeasure)
        ColemanLiauMeasure = getColemanLiauMeasure(sentenceCount, wordCount, 
                                                   letterCount)
        print("3. ColemanLiauMeasure: ", ColemanLiauMeasure)
        FleschMeasure = getFleschMeasure(sentenceCount, wordCount, syllableCount)
        print("4. FleschMeasure: ", FleschMeasure)
        GunningFogMeasure = getGunningFogMeasure(sentenceCount, wordCount, 
                                                 polysyllabicWordCount)
        print("5. GunningFogMeasure: ", GunningFogMeasure)
        LixMeasure = getLixMeasure(sentenceCount, wordCount, longWordCount)
        print("6. LixMeasure: ", LixMeasure)
        SmogMeasure = getSmogMeasure(wordCount, polysyllabicWordCount)
        print("7. SmogMeasure: ", SmogMeasure)
        Richness = getRichness(dictionary)
        print("8. Richness: ", Richness)
        wordStats = [(key, dictionary[key]) for key in dictionary.keys()]
        sortedwordStats = sorted(wordStats, key = operator.itemgetter(1),
                                 reverse = True)
        print('Top 10 Frequent words:')
        for i in range(10):
            print(sortedwordStats[i][0], sortedwordStats[i][1], sep = ': ')
        fileName = input("Type in your file name('q' to quit the program): ")
    print("Goodbye!")
    return None

def readFile(fileName):
    '''Read the input text file.'''
    lineLists = []
    with open(fileName) as file:
        for line in file:
            lineLists.append(line)
    return lineLists

def getSentences(text):
    '''Reorganize and clean sentences from the raw input.'''
    filteredList = []
    filteredLine = ''
    previousChar = ''
    if(text[-1][-1] not in '.!?'):
        text[-1] += '.'
    for line in text:
        #check if the previous line doesn't end a sentence and starts with no spacs in between words
        if previousChar != ' ' and line[0] not in '.!? ':
            filteredLine += ' '
        for char in line:
            if char not in '.!?':
                filteredChar = char.lower()
                if not (char.isalpha() or char == '\''):
                    if previousChar == ' ':
                        continue
                    else:
                        filteredChar = ' '
                filteredLine += filteredChar
                previousChar = filteredChar
            elif len(filteredLine.strip()) != 0:
                filteredList.append(filteredLine.strip())
                filteredLine = ''
    return filteredList
    
def getSentenceCount(sentences):
    '''Get the total sentence count.'''
    return len(sentences)

def getWordCount(sentences, dictionary):
    '''Get the total word count.'''
    wordLists = []
    wordCount = 0
    for sentence in sentences:
        #words have been filtered already, just split them up
        wordLists = sentence.split()
        wordCount += len(wordLists)
        for word in wordLists:
            if(word in dictionary.keys()):
                dictionary[word] += 1
            else:
                dictionary[word] = 1
    return wordCount

def getLongWordCount(sentences):
    '''Get the Long word(words with 6 or more litters) count.'''
    wordLists = []
    longWordCount = 0
    for sentence in sentences:
        wordLists = sentence.split()
        for word in wordLists:
            if(len(word) >= 6):
                longWordCount += 1
    return longWordCount

def getPolysyllableWordCount(sentences):
    '''Get the total word count with ploy(three or more) syllable.'''
    worldLists = []
    polyCount = 0
    for sentence in sentences:
        wordLists = sentence.split()
        for word in wordLists:
            count = checkSyllable(word)
            if count >= 3:
                polyCount += 1
    return polyCount

def getLetterCount(sentences):
    '''Get the total letter count.'''
    letter = ''
    for sentence in sentences:
        letter += ''.join(list(filter(lambda x: x.isalpha() , sentence)))
    return len(letter)

def getSyllableCount(sentences):
    '''Get the total syllable count.'''
    worldLists = []
    syllableCount = 0
    for sentence in sentences:
        wordLists = sentence.split()
        for word in wordLists:
            syllableCount += checkSyllable(word) #strip out apostrophes
    return syllableCount

def checkSyllable(word):
    '''Check how many syllables are there for the given word.'''
    firstSyllable = ''
    syllableCount = 0
    if len(word) <= 3:
        return 1
    for i in range(0, len(word)):
        #find a vowel
        if(word[i] in 'aeiouy'): 
            if (firstSyllable == ''):
                firstSyllable = word[i]
        #consonant followed by a vowel, count it
        elif firstSyllable != '':
            syllableCount += 1
            firstSyllable = ''
    #last vowel also counts
    if word[-1] in 'aeiouy':
        syllableCount += 1
    if (syllableCount == 0):
        return 1
    if ((word[-2:] in ['es', 'ed'] and word[-3] not in "aeiouy") 
        or (word.endswith('e') and not word.endswith('le') and word[-2] not in 'aeiouy')):
        syllableCount -= 1
    if (word.startswith('y') and word[1] not in 'aeiouy'):
        syllableCount -= 1
    if syllableCount == 0:
        return 1
    return syllableCount

def getKincaidMeasure(sentenceCount, wordCount, syllableCount):
    '''Return with the Kincaid measurement.'''
    return ((11.8 * syllableCount / wordCount) + (0.39 * wordCount / sentenceCount) - 15.59)

def getARImeasure(sentenceCount, wordCount, letterCount):
    '''Return with the Automated Readability Index measurement.'''
    return ((4.71 * letterCount / wordCount) + (0.5 * wordCount / sentenceCount) - 21.43)

def getColemanLiauMeasure(sentenceCount, wordCount, letterCount):
    '''Return with the Coleman-Liau measurement.'''
    return ((5.89 * letterCount / wordCount) - ((0.3 * sentenceCount) / (100 * wordCount)) - 15.8)

def getFleschMeasure(sentenceCount, wordCount, syllableCount):
    '''Return with the Flesch measurement.'''
    return (206.835 - (84.6 * syllableCount / wordCount) - (1.015 * wordCount / sentenceCount))

def getGunningFogMeasure(sentenceCount, wordCount, polysyllabicWordCount):
    '''Return with the Fog(Gunning) measurement.'''
    return (0.4 * (wordCount / sentenceCount + 
           100 * polysyllabicWordCount / wordCount))

def getLixMeasure(sentenceCount, wordCount, longWordCount):
    '''Return with the Lix measurement.'''
    return (wordCount / sentenceCount + 100 * longWordCount / wordCount)

def getSmogMeasure(wordCount, polysyllabicWordCount):
    '''Return with the SMOG measurement.'''
    return (3 + math.sqrt(30 * polysyllabicWordCount / wordCount))

def getRichness(dictionary):
    '''Get how 'rich' the vocabulary is for given dictionary.'''
    wordStats = [(key, dictionary[key]) for key in dictionary.keys()]
    sortedwordStats = sorted(wordStats, key = operator.itemgetter(1),
                             reverse = True)
    totalWordCount = 0
    wordCount = 0
    richness = 0
    for (word, count) in sortedwordStats:
        totalWordCount += count
    for (word, count) in sortedwordStats:
        wordCount += count
        richness += 1
        if (wordCount >= 0.5 * totalWordCount):
            break
    return richness
