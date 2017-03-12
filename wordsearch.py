__author__ = 'Indy'

class WordSearch():

    def __init__(self, lettermatrix):
        self.lettermatrix = lettermatrix
        self.solutionmatrix = self.__initialisesolutionmatrix(len(lettermatrix))
        self.path = 1

    def __initialisesolutionmatrix(self, size):
        return [[0 for x in range(0, size)] for b in range(0, size)]

    def findword(self, word):

        for i in range(0, len(self.lettermatrix)):
            for j in range(0, len(self.lettermatrix)):
                if self.__findletter(self.lettermatrix, word, i, j, 0, len(self.lettermatrix)):
                    return self.solutionmatrix

        return "No Path Found"

    def __findletter(self, lettermatrix, word, ypos, xpos, index, sizeofmatrix):


        # First check that the cell isn't already being used or whether it matches the
        # first letter of the search word, if not return false and therefore move on
        try:
            if self.solutionmatrix[ypos][xpos] != 0 or self.lettermatrix[ypos][xpos] != word[index]:
                return False
        except IndexError:
            print("Index error " + str(xpos))


        # check if we are already at the end of the word and therefore exit
        if index == len(word)-1:
            self.solutionmatrix[ypos][xpos] = self.path
            return True

        # If we get this far we know we are at the start letter and start position
        self.solutionmatrix[ypos][xpos] = self.path
        self.path += 1

        if ypos < sizeofmatrix and self.__findletter(lettermatrix, word, ypos+1, xpos, index+1, sizeofmatrix):
            return True

        if ypos-1 >= 0 and self.__findletter(lettermatrix, word, ypos-1, xpos, index+1, sizeofmatrix):
            return True

        if xpos+1 < sizeofmatrix and self.__findletter(lettermatrix, word, ypos, xpos+1, index+1, sizeofmatrix):
            return True

        if xpos-1 >= 0 and self.__findletter(lettermatrix, word, ypos, xpos-1, index+1, sizeofmatrix):
            return True

        if ypos - 1 >= 0 and xpos + 1 >= 0 and self.__findletter(lettermatrix, word,
                                                               ypos - 1, xpos + 1, index + 1, sizeofmatrix):
            return True

        if ypos - 1 >= 0 and xpos - 1 >= 0 and self.__findletter(lettermatrix, word,
                                                               ypos - 1, xpos - 1, index + 1, sizeofmatrix):
            return True

        if ypos + 1 < sizeofmatrix and xpos - 1 >= 0 and \
                self.__findletter(lettermatrix, word, ypos + 1, xpos - 1, index + 1, sizeofmatrix):
            return True

        if ypos + 1 < sizeofmatrix and xpos + 1 < sizeofmatrix and \
                self.__findletter(lettermatrix, word, ypos + 1, xpos + 1, index + 1, sizeofmatrix):
            return True


        self.solutionmatrix[ypos][xpos] = 0
        self.path -= 1
        return False



def main():
    #We will always deal with a N x N matrix
    matrix = [['w', 'a', 'b', 'c'], ['g', 'q', 'a', 't'], ['u', 'x', 't', 'y'], ['m', 'u', 'e', 's']]

    wordsearch = WordSearch(matrix)


    #print out solution
    print(wordsearch.findword('mu'))

if __name__ == '__main__':
    main()
