import time,sys,subprocess,argparse

def timer(sec):
	for i in range(sec,0,-1):
		m,s=divmod(i,60)
		h,m=divmod(m,60)
		if(sec>3600):
			print("\rh:{} m:{} s:{} ".format(h,m,s),end="")
		else:
			print("\rm:{} s:{} ".format(m,s),end="")
		time.sleep(1)
	play() #function call to play alert sound

def play(fname="beep_beep_beep_alarm.mp3"): #function to play timer alert sound
	subprocess.call(["ffplay","-nodisp","-hide_banner","-autoexit",fname])

parser=argparse.ArgumentParser()
parser.add_argument("hours",help="hours in numbers",type=int) #compulsory argument of type int for hours
parser.add_argument("minutes",help="minutes in numbers",type=int) #compulsory argument of type int for mins 
parser.add_argument("seconds",help="seconds in numbers",type=int) #compulsory argument of type int for secs
args=parser.parse_args()
secs=0
if args.seconds>=60: #convert secs >60 to mins and secs
	args.seconds%=60
	args.minutes+=args.seconds//60
if args.minutes>=60: #convert mins >60 to hrs and mins
	args.minutes%=60
	args.hours+=args.minutes//60
secs+=args.hours*3600 #convert hrs to sec
secs+=args.minutes*60 #convert mins to sec
secs+=args.seconds #add secs
#print(secs)
timer(secs)