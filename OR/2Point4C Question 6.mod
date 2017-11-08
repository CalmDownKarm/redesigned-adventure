# 2.4C A department store operates 7 days a week. The manager estimates that the minimum number of sales
#people required is 12 for monday, 18 for tuesday, 20 for wednesday, 28 for thursday, 32 for friday
# 40 for sat and sunday. Each salesperson works 5 days a week with 2 consecutive off days staggered
# throughout the week, how many sales persons should be recruited and their offdays

#Create variables for individuals starting on Monday to Sunday
var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;
var x6 >= 0;
var x7 >= 0;
minimize cost: x1+x2+x3+x4+x5+x6+x7; # Minimize sum of total 
s.t. const1: x1+x4+x5+x6+x7 >= 12; # Monday constraint 
s.t. const2: x1+x2+x5+x6+x7 >= 18; # Tuesday constraint
s.t. const3: x1+x2+x3+x6+x7 >= 20; # Wednesday
s.t. const4: x1+x2+x3+x4+x7 >= 28; # Thursday
s.t. const5: x1+x2+x3+x4+x5 >= 32; # Friday
s.t. const6: x2+x3+x4+x5+x6 >= 40; # Saturday
s.t. const7: x3+x4+x5+x6+x7 >= 40; # Sunday
solve;
display x1;
display x2;
display x3;
display x4;
display x5;
display x6;
display x7;

# ampl: model programmingass1q3.mod;
#MINOS 5.51: optimal solution found.
# 4 iterations, objective 42
# x1 = 0
# x2 = 2  means 2 people off on Sunday and Monday
# x3 = 24 means 24 people are off monday tuesday
# x4 = 0 
# x5 = 14 means 14 people take off wednesday and thursday
# x6 = 0
# x7 = 2 2 people take off on Friday and Saturday
