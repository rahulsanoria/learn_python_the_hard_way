print "MY WISHES"

any = ' > '

print "Cost of sweet home :  "
home_cost = int(raw_input(any))            #mumbai city 

print "Cost of car :  "
car_cost = int(raw_input(any))             #bmw x3 or audi Q3

print "Cost of bike :  "
bike_cost = int(raw_input(any))            # kawasaki ninja 650

print "Cost of my phone :  "
iphone_cost = int(raw_input(any))           # updated version 

print "Cost of travelling :  "
travel_cost = int(raw_input(any))              # like europe etc.

print "Cost of camera :  "
camera_cost = int(raw_input(any))              #canon camera

total_cost = (home_cost + car_cost + iphone_cost + bike_cost + camera_cost + travel_cost)
print "\ntotal cost  :  %d" % total_cost



print "\nAge at starting of job :  "
current_age = int(raw_input(any))               # age at joining stage 



print "\nAge at which you want to get home : "
age_get_home = int(raw_input(any))
time = age_get_home - current_age
salary_per_month = home_cost / ( time * 12 )
print "salary_per_month required  for get home at age  %d is %d " % ( age_get_home , salary_per_month)

print "\nAge at which you want to get car : "
age_get_car = int(raw_input(any))
time = age_get_car - current_age
salary_per_month =  car_cost / (time * 12 )
print "salary_per_month required  for get car at age  %d is %d " % ( age_get_car , salary_per_month)


print "\nAge at which you want to get bike : "
age_get_bike = int(raw_input(any))
time = age_get_bike - current_age
salary_per_month = bike_cost / ( time * 12 )
print "salary_per_month required  for get bike at age  %d is %d " % ( age_get_bike , salary_per_month)

print "\nAge at which you want to get phone : "
age_get_iphone = int(raw_input(any))
time = age_get_iphone - current_age
salary_per_month = iphone_cost / ( time * 12 )
print "salary_per_month required  for get phone at age  %d is %d " % ( age_get_iphone , salary_per_month)

print "\nAge at which you want to get trvel (world) : "
age_get_travel = int(raw_input(any))
time = age_get_travel - current_age
salary_per_month = travel_cost / ( time * 12 )
print "salary_per_month required  for get travel at age  %d is %d " % ( age_get_travel , salary_per_month)
  
print "\nAge at which you want to get camera :"
age_get_camera = int(raw_input(any))
time = age_get_camera - current_age
salary_per_month = camera_cost / ( time * 12 )
print "salary_per_month required  for get camera at age  %d is %d " % ( age_get_camera , salary_per_month)





