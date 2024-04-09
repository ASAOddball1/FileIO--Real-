from FileRead import FileRead
from FileWrite import FileWrite
from FileEncrypter import FileEncrypter
from FileDecrypter import FileDecrypter
FileRead = FileRead("AllWords.txt")

print("Read Total Number Of Lines")

FileRead.totalNumberOfLines()

print("Read Total Number Of Characters In File")

FileRead.readAllCharactersFromFile()

print("Read Total Number Of Words In File")

FileRead.totalNumberOfWords()

print("Type In A Word, This Will Check If Its In The File")

FileRead.wordcheck()

FileRead.lengthCheck()

#print ("Read First Line")

#FileRead.readFirstLineFromFile()

#print ("Read Line By Line")

#FileRead.readFileLineByLine()



