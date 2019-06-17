import warnings
warnings.filterwarnings("ignore")
import paramiko
COMPNAME = '10.12.25.15' # or '192.168.0.17'
USER = '.\\upsct_pc'
PASSWORD = 'N@kia1234'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(COMPNAME, username=USER, password=PASSWORD, port=24, allow_agent = False)
def check_stderr(stream):
    s = stream.read()
    if s:
        print("runtime error")
def ipconfig(ssh):
    com = "ipconfig"
    i, o, e = ssh.exec_command(com)
    check_stderr(e)
    return ''.join(o .readlines())
    
def home_dir(user):
    return "/cygdrive/c/Documents*Settings/" + user
if __name__ == "__main__":
    print (ipconfig(ssh))