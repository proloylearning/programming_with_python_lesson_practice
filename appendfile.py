writeMe = 'Some text'

saveFile = open('example2.txt', 'a')
saveFile.write('\n')
saveFile.write(writeMe)
saveFile.close()
