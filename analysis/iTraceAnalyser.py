import MySQLdb
import pandas
import matplotlib
import matplotlib.pyplot as plt
import math
import csv
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

#Returns a dictionary of Fixations 

def get_session(host,user,passwd,db, session_id, threshold):
        db = MySQLdb.connect(host=host,
                         user=user,
                         passwd=passwd,
                         db=db)

        cursor = db.cursor()
        session_info = cursor.execute("SELECT * FROM session_info WHERE session_id='"+session_id+"'")
        df = pandas.read_sql("SELECT * FROM (SELECT * FROM gazes JOIN sces ON gazes.gaze_id=sces.sce_gaze_id) a WHERE a.gaze_session_id='" + session_id + "';", db)
        #df has all sces. dfu only has sce of depth 0.
        dfu = df.drop_duplicates(subset="gaze_id")
        
        # I-VT. let's find some fixations!
        fixations = []
        saccades = []
        
        fix_list = []
        fixation = []
        prev_index = []
        
        
        for index, row in dfu.iterrows():
            curr_index = {'session_time' : row['session_time'], 
                       'x':row['x'], 'y':row['y'], 'sce_name':row['sce_name'],
                       'depth':row['depth'], 'gaze_name':row['gaze_name'], 'sce_type':row['sce_type'],
                       'gaze_session_id':row['gaze_session_id'],'line':row['line']}
            if not fixation:
                fixation.append(curr_index)
            #If time is less than 100
            if (fixation[len(fixation)-1]['session_time']/1e6 - fixation[0]['session_time']/1e6) < 100:    
                fixation.append(curr_index)
                #Ensure that while time is less than 100, threshold is met.
                while get_dispersion(fixation) > threshold:
                    fixation.pop(0)
                continue
            #If time is over 100, but threshold is less than threshold



            if get_dispersion(fixation) <= threshold:
                fixation.append(curr_index)

                if get_dispersion(fixation) > threshold:
                    fixation.pop(len(fixation)-1)
                    #print "fixation dispersion " + str(get_dispersion(fixation))
                    fix_list.append(fixation)
                    fixation = [curr_index]
            
        for fix in fix_list:
            #Getting the x and y values, for centroid
            x_list = []
            y_list = []
            sce_list = []
            sce_type_list = []
            line_list = []
            id_list = []
            for i in fix:
                x_list.append(i['x'])
                y_list.append(i['y'])
                sce_list.append(i['sce_name'])
                sce_type_list.append(i['sce_type'])
                line_list.append(i['line'])
                id_list.append(i['gaze_session_id'])

            
            centroid_x = sum(x_list)/len(x_list)
            centroid_y = sum(y_list)/len(y_list)

            #startTime, endTime and duration in seconds.
            startTime = fix[0]['session_time']/1e9
            endTime = fix[len(fix)-1]['session_time']/1e9
            duration = endTime - startTime
            
            depth = 0 #Not supported, but some day, maybe?
            
            fileName = fix[0]['gaze_name']
            #Sce name, if two source code entities are very close, we pick the one with the most gazes.
            sce_name =  max(set(sce_list), key=sce_list.count)
            sce_type =  max(set(sce_type_list), key=sce_type_list.count)
            line =  max(set(line_list), key=line_list.count)
            gaze_session_id =  max(set(id_list), key=id_list.count)


            #Returns a dictionary of Fixations (startTime, endTime, duration, X, Y, sceName, depth, file) 
            fixations.append({'start_time':startTime,
                              'end_time':endTime, 'duration':duration, 
                              'x':centroid_x, 'y':centroid_y, 
                              'sce_name':sce_name, 'depth':depth, 
                              'file_name':fileName, 
                              'sce_type':sce_type, 'line':line,
                              'gaze_session_id':gaze_session_id})
        return fixations#, saccades

def get_dispersion(fixation):
    #Finding distance between the points
    min_x = 999999
    max_x = 0;
    max_y = 0;
    min_y = 999999;
    min_line = 999999;
    max_line = 0
    for i in fixation:
        if i['x'] > max_x:
            max_x = i['x'] 
        if i['x'] < min_x:
            min_x = i['x'] 
        if i['y'] > max_y:
            max_y = i['y'] 
        if i['y'] < min_y:
            min_y = i['y'] 
        if i['line'] < min_line:
            min_line = i['line']
        if i['line'] > max_line:
            max_line = i['line']


    dispersion = (max_x-min_x) + (max_y-min_y)
    if (max_line - min_line) > 2:
        dispersion += 1000
    return dispersion



def get_raw_gazes(host,user,passwd,db, session_id):
		db = MySQLdb.connect(host=host,
                     user=user,
                     passwd=passwd,
                     db=db)
		cursor = db.cursor()
		session_info = cursor.execute("SELECT * FROM session_info WHERE session_id='"+session_id+"'")
		df = pandas.read_sql("SELECT * FROM (SELECT * FROM gazes JOIN sces ON gazes.gaze_id=sces.sce_gaze_id) a WHERE a.gaze_session_id='" + session_id + "';", db)
		#df has all sces. dfu only has sce of depth 0.
		dfu = df.drop_duplicates(subset="gaze_id")
		return dfu

def fixation_scatter_plot(fixations, fig, title):
    x_list = []
    y_list = []
    s_list = []
        
    for point in fixations:
        x_list.append(point['x'])
        y_list.append(point['y'])
        s_list.append(point['duration']*1000)
	plt.xlim(200, 700)
	plt.ylim(0, 600)
	plt.title(title)
    plt.gca().invert_yaxis()
    plt.scatter(x_list,y_list, s=s_list)
	#Uncomment for numbers in order.
    #i = 0
    #for x, y in zip(x_list, y_list):
    #    plt.text(x, y, str(i), color="red", fontsize=12)
    #    i += 1
    plt.savefig(fig + ".png", format='png')

    plt.show()

def gaze_scatter_plot(gazes, fig,title):
	x_list = []
	y_list = []
	for index, point in gazes.iterrows():
		x_list.append(point['x'])
		y_list.append(point['y'])
	plt.xlim(200, 700)
	plt.ylim(0, 600)
	plt.title(title)
	plt.gca().invert_yaxis()
	plt.scatter(x_list,y_list)
	plt.savefig(fig + ".png", format='png')

	plt.show()

	
def process_mining_data(fixations_list, csv_name, aoi, user_def='No'):
    #Make buckets, and define name of AoIs
    if(aoi == 'lines'):
        area = 'line'
        
    if (aoi == 'sce_grouped'):
        area = 'sce_type'
    if (aoi == 'sce'):
        area = 'sce_name'
        
    if (aoi == 'user_defined'):
        aoi_defs = []
        with open(user_def, 'rb') as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                start = int(line[1])
                end = int(line[2])
                aoi_defs.append([line[0],[i for i in range(start,end+1)]])
            
    
    with open(csv_name, 'w') as csvfile:
        #initialising csv file
        csv_writer = csv.writer(csvfile, delimiter=',')
        csv_writer.writerow(["subject", "area of interest", "start", "end"])

        #creating a name dictionary
        if aoi == 'lines':
            name_dict = {}
            for fixations in fixations_list:
                for fixation in fixations:
                    if fixation['line'] in name_dict:
                        name_dict[fixation['line']] = name_dict[fixation['line']] + [fixation['sce_type']]
                    else:
                        name_dict[fixation['line']] = [fixation['sce_type']]
        for fixations in fixations_list:
            #go through fixations and see if it matches a bucket. "empty" buckets whenever you find something from a new bucket.
            subject = ''
            name_of_aoi = ''
            start = 0
            end = 0
            aoi_list = []
            area_of_interest = []
            prev_fix = {}
            prev_group = ""
            fix_group = ""
            inAoI = False
            for fix in fixations:
                if(aoi == 'user_defined'):
                    for aoi_index in aoi_defs:
                        if (fix['line'] in aoi_index[1]):
                            inAoI = True
                    if (inAoI == False):
                        if not(area_of_interest == []): 
                            aoi_list.append(area_of_interest)
                            area_of_interest = []
                            prev_fix = {}
                            prev_group = ""
                        continue
                        
                
                if prev_fix == {}:
                    prev_fix = fix
                    if(aoi == 'user_defined'):
                        for aoi_index in aoi_defs:
                            if (prev_fix['line'] in aoi_index[1]):
                                prev_group = aoi_index[0]
                    continue
                    
                area_of_interest.append(prev_fix)
                
                if(aoi == 'user_defined'):
                    #if we don't set previous group (doesn't belong in any AoI), we dont append it.
                    #finding group for each fix
                    for aoi_index in aoi_defs:
                        if (fix['line'] in aoi_index[1]):
                            fix_group = aoi_index[0]
                    if (prev_group == fix_group and not (prev_fix['end_time']+1 < fix['start_time'])):
                        prev_fix = fix
                        prev_group = fix_group
                        
                    else:
                        aoi_list.append(area_of_interest)
                        area_of_interest = []
                        prev_fix = fix
                        prev_group = fix_group
                                
                #Not user_defined
                else:
                    if (prev_fix[area] == fix[area] and not (prev_fix['end_time']+1 < fix['start_time'])):
						area_of_interest.append(prev_fix)
						prev_fix = fix
                        
                    else:
                        aoi_list.append(area_of_interest)
                        area_of_interest = []
                        prev_fix = fix
                #special case for last
                if (fix == fixations[len(fixations)-1]):
                    area_of_interest.append(fix)
                    aoi_list.append(area_of_interest)
                    
            for l in aoi_list:
                name_of_aoi = ""
                subject = l[0]['gaze_session_id']
                start = l[0]['start_time']
                end = l[len(l)-1]['end_time']
                if (aoi == 'user_defined'):
                    for aoi_index in aoi_defs:
                        if (l[0]['line'] in aoi_index[1]):
                            name_of_aoi = aoi_index[0]
                    #That special case, where the last fixation, which we had to add
                    if name_of_aoi == "":
                        continue
                else:
                    #print str(set(name_dict[l[0]['line']]))[5:-2].
                    print str(set(name_dict[l[0]['line']]))[5:-2].replace(",", " ")
                    if aoi == 'lines':
                        name_of_aoi = str(l[0][area]) + " " + str(set(name_dict[l[0]['line']]))[5:-2].replace(",", " ")
                    else:
                        name_of_aoi = str(l[0][area])

                csv_writer.writerow([subject,name_of_aoi,start,end])
                
    
def fixation_average_duration_bar(fixations, filename, attribute):
    x = []
    y = []
    x_ticks = []
    #fixations = sorted(fixations, key=lambda k: k[attribute]) 

    for i in fixations:
        x_ticks.append(i[attribute])
    
    x_ticks = sorted(list(set(x_ticks)))
    print x_ticks
    durr = 0
    for ftype in x_ticks:
        avg_counter = 0
        for i in fixations:
            if i[attribute] == ftype:
                avg_counter += 1
                durr += i['duration']
        y.append(durr/avg_counter)
        durr = 0
    x = [i for i in range(len(x_ticks))]
    plt.xticks(x,x_ticks,rotation=90)
    if(len(x) > 15):
        plt.tick_params(axis='both', which='major', labelsize=5)
    plt.title(attribute + ' average fixation duration, seconds')
    #plt.tight_layout()
    plt.xlabel(str(attribute))
    plt.ylabel("seconds")

    plt.bar(x,y)
    plt.savefig(filename + ".png", format='png')

    plt.show()
    

    
def fixation_duration_bar(fixations, filename, attribute):
    x = []
    y = []
    x_ticks = []
    for i in fixations:
        x_ticks.append(i[attribute])
    
    x_ticks = sorted(list(set(x_ticks)))
    durr = 0
    for ftype in x_ticks:
        for i in fixations:
            if i[attribute] == ftype:
                durr += i['duration']
        y.append(durr)
        durr = 0
    x = [i for i in range(len(x_ticks))]
    plt.xticks(x,x_ticks,rotation=90)
    if(len(x) > 15):
        plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title( attribute + ' total fixation duration, seconds')
    #plt.tight_layout()
    plt.xlabel(str(attribute))
    plt.ylabel("seconds")


    plt.bar(x,y)
    plt.savefig(filename + ".png", format='png')

    plt.show()

def fixation_max_duration_bar(fixations, filename, attribute):
    x = []
    y = []
    x_ticks = []
    for i in fixations:
        x_ticks.append(i[attribute])
    
    x_ticks = sorted(list(set(x_ticks)))
    durr = 0
    for ftype in x_ticks:
        for i in fixations:
            if i[attribute] == ftype:
                if i['duration'] > durr:
                    durr = i['duration']
        y.append(durr)
        durr = 0
    x = [i for i in range(len(x_ticks))]
    plt.xticks(x,x_ticks,rotation=90)
    if(len(x) > 15):
        plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title( attribute + ' max fixation duration, seconds')
    #plt.tight_layout()
    plt.xlabel(str(attribute))
    plt.ylabel("seconds")


    plt.bar(x,y)
    plt.savefig(filename + ".png", format='png')

    plt.show()


    
def fixation_count_bar(fixations, filename, attribute):
    x = []
    y = []
    x_ticks = []
    for i in fixations:
        x_ticks.append(i[attribute])
    
    x_ticks = sorted(list(set(x_ticks)))
    count = 0
    for ftype in x_ticks:
        for i in fixations:
            if i[attribute] == ftype:
                count += 1
        y.append(count)
        count = 0
    x = [i for i in range(len(x_ticks))]
    plt.xticks(x,x_ticks,rotation=90)
    if(len(x) > 15):
        plt.tick_params(axis='both', which='major', labelsize=6)
    plt.title(attribute + ' fixation count')
    #plt.tight_layout()
    plt.xlabel(str(attribute))
    plt.ylabel("# of fixations")



    plt.bar(x,y)
    plt.savefig(filename + ".png", format='png')
    plt.show()

def session_duration(fixations):
    start = int(fixations[0]['start_time'])
    end = int(fixations[len(fixations)-1]['end_time'])
    return end-start;