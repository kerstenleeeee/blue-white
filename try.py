import subprocess
import os


# comments:
# okay siya nacconvert yung SVN folders into normal folders so cannot access 
bts_pc = "10.12.25.15"
bts_un= "upsct_pc"
bts_ps = "N@kia1234"
bts_input = "net use Z: \\\\" + bts_pc + "\\C$ /user:" + bts_un + " " + bts_ps

try:
	s = subprocess.call('net use Z: \\\\10.12.25.15\\C$ ', shell=True)
	s = subprocess.call('net use G: \\\\10.12.25.15\\D$ ', shell=True)
	if(s == 0):
		print("success - mount")
	elif(s == 2):
		print("already mounted")
	#subprocess.call('net use Z: /del /y', shell=True)
	'''try:
		#subprocess.call('net use Z: /del', shell=True)
		f = open("Z:\\Pegasus\\workspaceWCDMA_Pilot\\workspaceWCDMA_Pilot.txt", "r")
		contents = f.read()
		rev = contents.split(':')
		print(contents)
		print(rev)
		#print("success - unmount")
	except:
		print("fail - unmount")'''
except:
	print("fail - mount")
