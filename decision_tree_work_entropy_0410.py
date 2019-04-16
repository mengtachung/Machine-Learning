import math

####### humid ##################################
sum = 14 ### yes=9; no=5 ####
entropy_root = (-9/14)*math.log(9/14, 2) - (5/14)*math.log(5/14, 2) ####math.log(a,Base)
print ("entropy root = ", entropy_root)

###### humid (high) ##########
yes = 3
no = 4
sum = yes + no
entropy_humid_high = (-yes/sum)*math.log(yes/sum, 2) - (no/sum)*math.log(no/sum, 2) ####math.log(a,Base)
print ("entropy of humid (high) = ", entropy_humid_high)

########  humid normal #####################################################################
yes = 6
no = 1
sum = yes + no
entropy_humid_normal = (-yes/sum)*math.log(yes/sum, 2) - (no/sum)*math.log(no/sum, 2) ####math.log(a,Base)
print ("entropy of humid (normal) = ", entropy_humid_normal)

################### humid weight ###########################
entropy_humid = (7/14)*entropy_humid_high + (7/14)*entropy_humid_normal
print ("entropy humid (weighted) = ", entropy_humid)
print ("information gain = ", entropy_root - entropy_humid)

####### wind ##################################

