#defining the argument, remember to put a ":" after the first line!
def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print "You have %d cheeses!" % cheese_count
        print "You have %d boxes of crackers!" % boxes_of_crackers
        print "Man that's enough for a party!"
#no clue what "\n" means
        print "Get a blanket.\n"

#inputting numbers directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#creating new variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


#im gonna try this one alone
def volleyball_games(game_count, week_count):
    print "We have %d games this weekend!" % game_count
    print "We have %d more weeks of volleyball" % week_count
    print "We should do really well."
    print "Let's get fans there!!! \n"
# i think "\n" repeats that line after each argument
print "I am putting the numbers here:"
game_count = 4
week_count = 6

volleyball_games(game_count, week_count)
