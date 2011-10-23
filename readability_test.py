# Yoon Hyup Hwang, Zhou Tan

import unittest
from readability import *

class readability_test (unittest.TestCase):
    def setUp(self):
        self.text = ["This text is a combination of etexts, one from the now-defunct ERIS\n", "project at Virginia Tech and one from Project Gutenberg's archives. The\n", "proofreaders of this version are indebted to The University of Adelaide\n", "Library for preserving the Virginia Tech version. The resulting etext\n", "was compared with a public domain hard copy version of the text."]
        self.sentences = getSentences(self.text)
        self.wordCount = getWordCount(self.sentences, {})
        self.longWordCount = getLongWordCount(self.sentences)
        self.sentenceCount = getSentenceCount(self.sentences)
        self.syllableCount = getSyllableCount(self.sentences)
        self.polysyllabicWordCount = getPolysyllableWordCount(self.sentences)
        self.letterCount = getLetterCount(self.sentences)

    def test_getSentences(self):
        self.assertEqual(['she said don\'t you dare'], getSentences(['She said,     ', '"Don\'t you    dare!"\n']))
        self.assertEqual(['how dare you', 'blah blah', 'and test'], getSentences(['How Dare \n', 'you? Blah blah.', 'And test.']))
        self.assertEqual(['this is a unit testing for getsentence function'], getSentences(['This is a ', 'Unit Testing\n for ', 'GetSentence', ' Function.']))
    def test_getSentenceCount(self):
        self.assertEqual(1, getSentenceCount(['she said don\'t you dare']))
        self.assertEqual(3, getSentenceCount(['how dare you', 'blah blah', 'and test']))
    def test_getWordCount(self):
        self.assertEqual(5, getWordCount(['she said don\'t you dare'], {'she': 1, 'said': 1}))
        self.assertEqual(7, getWordCount(['how dare you', 'blah blah', 'and test'], {'how': 1}))
        self.assertEqual(8, getWordCount(['this is a unit testing for getsentence function'], {}))
    def test_getLongWordCount(self):
        case1 = ['hello my name is john', 'i come from japan']
        case2 = ['hello my name is john', 'i come from brazil']
        case3 = ['america brazil russia mexico canada australia']
        case4 = ['america', 'brazil', 'russia', 'mexico', 'canada', 'australia']
        self.assertEqual(getLongWordCount(case1), 0)
        self.assertEqual(getLongWordCount(case2), 1)
        self.assertEqual(getLongWordCount(case3), 6)
        self.assertEqual(getLongWordCount(case4), 6)

    def test_getPolysyllableWordCount(self):
        caseVowel = ['these mysterious dishes are so delicious', 'tell me about it']
        caseOneSyllable = ['hi how are you', 'i am ill']
        caseBeginngY = ['yttric yttria yren']
        caseNoVowels = ['bbbbb ccccc kkkk lllll']
        self.assertEqual(getPolysyllableWordCount(caseVowel), 2)
        self.assertEqual(getPolysyllableWordCount(caseOneSyllable), 0)
        self.assertEqual(getPolysyllableWordCount(caseBeginngY), 0)
        self.assertEqual(getPolysyllableWordCount(caseNoVowels), 0)

    def test_getLetterCount(self): 
        case1 = ["hello world", "this is a test"]
        case2 = ["h'e'l'l'o w'o'r'l'd'", "t'h'i's i's a 't'e's't"]
        self.assertEqual(getLetterCount(case1), 21)
        self.assertEqual(getLetterCount(case2), 21)

    def test_getSyllableCount(self):
        caseVowel = ['these mysterious dishes are so delicious', 'tell me about it']
        caseOneSyllable = ['hi how are you', 'i am ill']
        caseBeginngY = ['yttric yttria yren']
        caseNoVowels = ['bbbbb ccccc kkkk lllll']
        self.assertEqual(getSyllableCount(caseVowel), 15)
        self.assertEqual(getSyllableCount(caseOneSyllable), 7)
        self.assertEqual(getSyllableCount(caseBeginngY), 3)
        self.assertEqual(getSyllableCount(caseNoVowels), 4)

    def test_checkSyllable(self):
        #beginning Y
        self.assertEqual(checkSyllable('yttle'), 1)
        self.assertEqual(checkSyllable('yattle'), 2)
        self.assertEqual(checkSyllable('delicious'), 3)
        #three or less letters
        self.assertEqual(checkSyllable('ado'), 1)
        self.assertEqual(checkSyllable('yahoo'), 2)
        #ending e, ed, es
        self.assertEqual(checkSyllable('agree'), 2)
        self.assertEqual(checkSyllable('played'), 1)
        self.assertEqual(checkSyllable('managed'), 2)
        self.assertEqual(checkSyllable('thirties'), 2)
        self.assertEqual(checkSyllable('arrayed'), 2)
        self.assertEqual(checkSyllable('counted'), 1)

    def test_getKincaidMeasure(self):
        self.assertEqual(round(getKincaidMeasure(self.sentenceCount, self.wordCount, 
                         self.syllableCount)), 11)

    def test_getARImeasure(self):
        self.assertEqual(round(getARImeasure(self.sentenceCount, self.wordCount, 
                         self.letterCount)), 12)

    def test_getColemanLiauMeasure(self):
        self.assertEqual(round(getColemanLiauMeasure(self.sentenceCount, self.wordCount, 
                         self.letterCount)), 14)

    def test_getFleschMeasure(self):
        self.assertEqual(round(getFleschMeasure(self.sentenceCount, self.wordCount, 
                         self.syllableCount)), 47)

    def test_getGunningFogMeasure(self):
        self.assertEqual(round(getGunningFogMeasure(self.sentenceCount, self.wordCount, 
                         self.polysyllabicWordCount)), 15)

    def test_getRichness(self):
        dictionary = {}
        wordCount = getWordCount(getSentences(self.text), dictionary)
        self.assertEqual(getRichness(dictionary), 11)
        
unittest.main()
