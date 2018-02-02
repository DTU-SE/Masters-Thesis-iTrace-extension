import iTraceAnalyser as IA

#Creating session fixation data for a specific user at different sensitivities. For Chapter 4 section 2.

rawGazes = IA.get_raw_gazes("localhost","root","1234","iTrace",'20171219T095731-0417+0100')
fixations15 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100', 5)
fixations25 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100',10)
fixations35 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100',15)
fixations45 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100',20)
fixations55 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100',25)
fixations65 = IA.get_session("localhost","root","1234","iTrace",'20171219T095731-0417+0100',30)

#Creating scatter plots for the fixation sesnsitivity analysis Chapter 4 section 2.
IA.gaze_scatter_plot(rawGazes, "TestGaze", "Gazes")
IA.fixation_scatter_plot(fixations5,"TestFix5", "Fixations 5")
IA.fixation_scatter_plot(fixations10,"TestFix10", "Fixations 10")
IA.fixation_scatter_plot(fixations15,"TestFix15", "Fixations 15")
IA.fixation_scatter_plot(fixations20,"TestFix20", "Fixations 20")
IA.fixation_scatter_plot(fixations25,"TestFix25", "Fixations 25")
IA.fixation_scatter_plot(fixations30,"TestFix30", "Fixations 30")

#Importing the test subjects data
iTrace1 = IA.get_session("localhost","root","1234","iTrace",'20171201T092946-0684+0100',15) 
iTrace2 = IA.get_session("localhost","root","1234","iTrace",'20171201T101056-0578+0100',15) 
iTrace3 = IA.get_session("localhost","root","1234","iTrace",'20171205T100741-0299+0100',15) 
iTrace4 = IA.get_session("localhost","root","1234","iTrace",'20171205T102737-0035+0100',15) 
iTrace5 = IA.get_session("localhost","root","1234","iTrace",'20171205T105857-0765+0100',15) 

#Creating bar plots for Chapter 4 section 3.
IA.fixation_count_bar(iTrace1,"count_lines","line")
IA.fixation_count_bar(iTrace1,"count_types","sce_type")

IA.fixation_duration_bar(iTrace1,"dur_lines","line")
IA.fixation_duration_bar(iTrace1,"dur_types","sce_type")

IA.fixation_average_duration_bar(iTrace1,"avg_dur_lines","line")
IA.fixation_average_duration_bar(iTrace1,"avg_dur_types","sce_type")

IA.fixation_max_duration_bar(iTrace1,"dur_max_lines","line")
IA.fixation_max_duration_bar(iTrace1,"dur_max_types","sce_type")

#creating event logs for chapter 4 section 4
IA.process_mining_data([iTrace1,iTrace2,iTrace3,iTrace4,iTrace5],"test_sort_lines.csv",'lines')
IA.process_mining_data([iTrace1,iTrace2,iTrace3,iTrace4,iTrace5],"test_sort_userdef.csv",'user_defined',"insertion.csv")
