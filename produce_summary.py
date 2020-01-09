
def melon_produce(delivery_file):

    """organizing information in txt files

        into name of melon, count, and cost"""
    
    # function open files
    the_file = open(delivery_file)
    for line in the_file: # for each line in the file
        line = line.rstrip() # strip the line of whitespaces and new line breaks
        words = line.split('|') # split the line into sections based on '|'

        # for each of the parameters given
        melon = words[0] # melon is in the first position
        count = words[1] # count is in the next (second position)
        amount = words[2] # amount is in the next (third position)

        #print the floowing statment using the variables in the previous section
        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
    the_file.close()


#set the following files to vaiables
file_20140519 = "um-deliveries-20140519.txt"
file_20140520 = "um-deliveries-20140520.txt"
file_20140521 = "um-deliveries-20140521.txt"

# call the function for each of the variables
melon_produce(file_20140519)
melon_produce(file_20140520)
melon_produce(file_20140521)



# print("Day 3")
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print("Delivered {} {}s for total of ${}".format(
#         count, melon, amount))
# the_file.close()
