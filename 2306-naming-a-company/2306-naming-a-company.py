class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        # // swapping the initial char from two words that have the same
        # // suffix is going to create the same set of words
        # // coffee , toffee
        # // toffee , coffee (we swapped c and t, but the suffix offee was the same)
        # // so can't count these
        
        # // idea is to store the words in a map with their starting char
        # // as the key and the rest of string as the value (in a set)
        
        # // then iterate through all the char key in the map
        # // iterate through all the char keys, continue if comparing same char
        # // find the intersect i.e. if the values from the maps in the two nested loops 
        # //  are same, then it means its a common suffix, and remember we already are
        # // two different char keys, therefore swapping those char in the words with same 
        # // suffix is not going to help


        wordMap = collections.defaultdict(set)

        for idea in ideas:
            wordMap[idea[0]].add(idea[1:])

        result = 0

        for char1 in wordMap:
            for char2 in wordMap:
                if char1 == char2:
                    continue
                
                intersect = 0

                for suffix1 in wordMap[char1]:
                    if suffix1 in wordMap[char2]:
                        intersect += 1

                distinct1 = len(wordMap[char1]) - intersect
                distinct2 = len(wordMap[char2]) - intersect

                result += distinct1 * distinct2

                # c : [afe, offee]

                # t : [ime, om, offee]

                # intersect = 1
                # distinct1 = 2 - 1 = 1
                # distinct2 = 3 - 1 = 2

                # the suffix 'offee' cant be used to form words.

                # between characters c and t, 'afe', 'ime' and 'om'
                # can be used

                # cime, com, tafe

                # "tafe cime"
                # "tafe com"

                # second interation:

                # "cime tafe"
                # "com tafe"

        return result