import sys
y = 0.0
testscore = 0.0
overallscore = 0.0
 
tests = int(sys.argv[1])
 
while y < tests:
        testscore = input("Please enter score ")
        overallscore = overallscore + testscore
        y = y + 1.0
else:   
        overallscore = overallscore / tests
        if overallscore >= 90:
                print "avg.",overallscore, "% A"
        elif overallscore >= 80:
                print "avg.",overallscore, "% B"
        elif overallscore >= 70:
                print "avg.",overallscore, "% C"
        elif overallscore >= 60:
                print "avg.",overallscore, "% D"
        else:   
                print "avg.",overallscore, "% You Suck F"