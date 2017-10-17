import time,sys,subprocess,argparse

def timer(sec):
	for i in range(sec,0,-1):
		if(sec>3600):
			print("\rh:{} m:{} s:{} ".format(i%3600,i%60,i),end="")
		else:
			print("\rm:{} s:{} ".format(i%60,i))
		time.sleep(1)

def play(fname="beep_beep_beep_alarm.mp3"):
	subprocess.call(["ffplay","-nodisp","-autoexit",fname])

parser=argparse.ArgumentParser()
parser.add_argument("-hs","--hours",type=int,help="hours in numbers")
parser.add_argument("-m","--minutes",help="minutes in numbers",type=int)
parser.add_argument("-s","--seconds",help="seconds in numbers",type=int)
args=parser.parse_args()
print(len(vars(args)))