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
parser.add_argument("-i",help="in")
args=parser.parse_args()
print(args)