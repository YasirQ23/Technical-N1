testString = "Patient presents today with several issues. Number one BMI has increased by 10% since their last visit number next patient reports experiencing dizziness several times in the last two weeks. Number next patient has a persistent cough that hasn’t improved for last 4 weeks Number next patient is taking drug number five several times a week"


def textTransformer(text):
    # create a dictionary for string to interger convertion
    numberMap = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    # use pythons built in split to create a list of the words in the given string
    # using a single pointer approach with a while loop so need to create a pointer variable
    # since the list can only start once and to counteract restarting the list with future use of the word 'number' within the given string create a boolean variable if the list has started or not
    # after the list is started we need to keep track where we are in the list since the list can start at any number 1-9 so we create the next number in the list variable
    # simple while loop to run through our list that we created from the given string named words
    words = text.split()
    pointer = 0
    listStarted = False
    nextNum = 0
    while pointer < len(words):
        # first if statement runs only once when the numbered list begins
            # change the boolean value to true so we know we have started the list
            # removing the string 'number' which is indicating an item in the list and replacing it with a new line for our print statement readability 
            # use the numberMap dictionary to replace the alphabetical format of the interger to the number integer and add a '.' for the list format
            # if the first word in any line in the list is not capitilized or already a Upper case word ex:'BMI' we capitilize the first letter
        if listStarted == False and words[pointer] == 'Number':
            listStarted = True
            words[pointer] = '\n'
            pointer += 1
            nextNum = int(numberMap[words[pointer]]) + 1
            words[pointer] = numberMap[words[pointer]] + '.'
            pointer += 1
            if words[pointer].isupper() == False:
                words[pointer] = words[pointer].capitilize()
        # next if statement runs only if the string is 'number' and followed by 'next' to counteract any problems with using the word 'number' ex: line 4 in our numbered list
            # removing the string 'number' which is indicating an item in the list and replacing it with a new line for our print statement readability 
            # use our nextNum variable to add a new item in our numbered list
            # update value for nextNum and traverse to the next string
            # if the first word in any line in the list is not capitilized or already a Upper case word ex:'BMI' we capitilize the first letter
        if words[pointer].lower() == 'number' and words[pointer+1].lower() == 'next':
            words[pointer] = '\n'
            pointer += 1
            words[pointer] = str(nextNum) + '.'
            nextNum += 1
            pointer += 1
            if words[pointer].isupper() == False:
                words[pointer] = words[pointer].capitalize()
        # if neither if statements activate then we traverse the list
        pointer += 1
    # return the list as a string in the correct format
    return ' '.join(words)


print(textTransformer(testString))


# Print Statement Returns
"""
Patient presents today with several issues. 
 1. BMI has increased by 10% since their last visit 
 2. Patient reports experiencing dizziness several times in the last two weeks. 
 3. Patient has a persistent cough that hasn’t improved for last 4 weeks 
 4. Patient is taking drug number five several times a week
"""
