# Python file open(fileName, access mode) access modes
# 'r' = read only mode
# 'w' = write only mode - erases everything that was there already!
# 'a' = append mode (write without replacing data)


# Python file functions
# read() - return whole file
# readline() - returns one line of the file
# readlines() = returns ALL lines in a list (1 line per entry)

class FileRead:

    filename = None

    def __init__(self, inputFileName):
        print('File reader created!')
        self.filename = inputFileName

    def readFirstLineFromFile(self):
        ''' Print out the contents from the first line of  file '''
        try:
            with open(self.filename, 'r') as reader:
                data = reader.readline()
                print(data)
        except IOError:
            print('Unable to read from file: ', self.filename)

    def totalNumberOfLines(self):
        '''Print Out The Total Number of Lines In a File'''
        try:
          with open(self.filename, 'r') as reader:
            lines = reader.readlines()
            row_count = sum(1 for filename in lines)
            print ("the total number of lines is",row_count)
        except IOError:
            print('Unable to read from file: ', self.filename)

    def totalNumberOfWords(self):
        '''Print Out The Total Number of Words In a File'''
        with open(self.filename, 'r') as reader:
            words = reader.read()
            word = words.split()
            word_count = len(word)
            return word_count

    def readFileLineByLine(self):
        ''' Prints out contents of the file line by line '''
        with open(self.filename, 'r') as reader:
            line = reader.readline()
            while line:  #loop as long as line is defined (stops after last line is read and returns null)
                print(line)
                line = reader.readline()  # update line with next line data



    def readAllCharactersFromFile(self):
        '''Print The Number Of Characters In a File'''
        try:
            with open(self.filename, 'r') as reader:
                content = reader.read()
                char_count = len(content)
                print("the total number of characters is", char_count)

        except IOError:
            print('Unable to read from file: ', self.filename)

    def getFileAllLines(self):
        ''' Returns a list of file contents, 1 line per entry '''
        data = list()

        with open(self.filename, 'r') as reader:
            line = reader.readline()
            while line:  #loop as long as line is defined (stops after last line is read and returns null)
                data.append(line)  # add line to data
                line = reader.readline()  # update line with next line data

        return data     # return list containing all data after file reading complete

    def wordcheck(self):
        '''returns weather or not the given word is in the file'''
        data = self.getAllDataFromFile()
        userInput = input("What word would you like to check? ")

        if(userInput in data):
            print("The word is in the file")
        else:
            print("The word is not in the file")

    #This Length Check Was The Last Thing I Needed To Finish To Finish The File Read Aspect,
    #only returns the given file name cuz god knows why
    #file write encrypt, decrypt, and write have been left completely untouched, after this project i will continue in java,
    #because python is maddening and all erors are confusing and hard to solve, not to mention mind boggling
    def lengthCheck(self):
        words = self.filename.split()
        length = int(input("How long would you like to check for? "))
        return [word for word in words if len(word) >= length]

    def getAllDataFromFile(self):
        ''' Returns a String containing all data from file '''
        try:
            with open(self.filename, 'r') as reader:
                data = reader.read()
                return data
        except IOError:
            print('Unable to read from file: ', self.filename)



    # Allows us to clean up a list of data to remove '\n' (newline) content from it
    def removeNewlinesFromData(self, data):
        ''' Returns a file with all \n (newline) content removed '''
        for i in range(len(data)): #loop through all data
            data[i] = data[i].replace("\n", "") #remove all references to new lines in data
            if len(data[i]) == 0: #if there are now empty entries in the data, remove them!
                data.remove(data[i])
                i -= 1 #after removing an entry, we need to move back a step (the list is now 1 shorter)
        return data



    # TODO
    # Create a method that returns the total number of lines of data in a file (DONE)


    # Create a method that returns the total number of words in a file (DONE)


    # Create a method that returns the total number of characters in a file (DONE)


    # Create a method that returns whether or not a file contains a given word or phrase (DONE)


    # Create a method that returns a list that only includes words of a certain length (ex: all the words with 3 letters in them)
