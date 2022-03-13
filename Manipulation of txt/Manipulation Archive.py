#First, open the file with the path.
#Opens the file in the current directory if not specified
#Or specify: "c:\folder\archive.txt")
#If you don't have the file it will automatically create with write and append.
#For read(r), write(w), append("a).
#######################################################################
#Be sure what you wrote so you don't delete what's in the file

#Write
# archive = open("c:\folder\something.txt", "w")
archive = open("something.txt", "w")
archive.write("You reset the txt and show you new text")
#Don't forget the close file.
archive.close()


#This method is safer for you don't forget the open file
#Write
with open("something.txt", "w") as variable:
    variable.write("Reset text or create new file")

#Append
with open("Something.txt", "a") as variable:
    #In another line, for the same line you don't need to add "\n"
    variable.write("\nWhat you want append")

#Read
with open("Something.txt", "r") as variable:
    print(variable.read())

#Reading line in line
archive = open("something.txt", "r")
for text in archive:
    #Replace \n for don't have blank line
    print(text.replace("\n", ""))