def maxNumOfMeetings(meet_time,max_time):
	no_of_meetings = 0
	total_time = 0
	while total_time <= max_time and no_of_meetings < n:
		total_time = total_time + meet_time[no_of_meetings]	
		no_of_meetings = no_of_meetings + 1
	return no_of_meetings


n = int(input('input number of meetings'))
meet_time = []
for i in range(n):
	start_time = int(input("Start time of meeting ",i+1," : "))
	end_time =  int(input("Enter the end time of meeting ",i+1," : "))
	meet_time.append(end_time-start_time)
meet_time.sorted()
max_time = int(input('Input max time for meetings'))
print("Max number of Meetings : ",maxNumOfMeetings(meet_time,max_time))
