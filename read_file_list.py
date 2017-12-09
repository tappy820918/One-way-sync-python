import paramiko
import time as tm
import csv
import datetime as dt
from subprocess import check_output

#modify here~~!
local = 'D:/DHVAC/'
filename = 'Toy.tar.gz'
filepath = '/home/tappy/Desktop/Server/'+filename
time0 = tm.time()
# host = '172.29.36.29'
# usr = 'Delta\samantha.tc.liu'
# pwd = 'Ji32k7au4a83'
# pwd = 'uno@1'
pwd = 'qwe51006'

#read IPCS list from file
#with open('/home/tappy/Desktop/IPCS_list.csv', 'rb') as f:
try:
    #reader = csv.reader(f)
    #data_csv = list(reader)
    #for row in data_csv:
    usr = 'tappy'
    host = '192.168.0.104'
    #initial ssh
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=usr, password=pwd)
    #initial sftp
        # sftp = paramiko.SFTPClient.from_transport(ssh.get_transport())
    #sftp = ssh.open_sftp()
    #run sftp
        # sftp.put(filepath, '/home/ubuntu/' + filename)
        # sftp.close()
    #run ssh
    # ssh.exec_command('cd /home/ubuntu')
    # ssh.exec_command('tar zxvf %s' %filename)
    # ssh.exec_command('cd /home/ubuntu/posix_ipc-1.0.0')
    #stdout = ssh.exec_command('cd /home/tappy/Desktop/Server ; find $(pwd) -type f')
    stdout = ssh.exec_command('cd /home/tappy/Desktop/Server ; ls ')
    print stdout
    #Str = stderr.readlines()
    #print Str
    #for i in range(len(Str)):
    #    print str(Str[i][:-2])
    #stdin.flush()
    ssh.close()
except Exception as e:
    print e
print 'Elapsed time = %f seconds' % (tm.time() - time0)

pwd = 'qwe51006'
HOST = 'tappy@192.168.0.104'
sync_folder = "/home/tappy/Desktop/Sync"
server_folder = "/home/tappy/Desktop/Server"

## $(pwd) to get full path
get_folder_cmd = ' find $(pwd) -type d '
get_file_cmd = ' find $(pwd) -type f  | xargs ls -lc --time-style="+%d-%m-%Y-%H:%M:%S" | tr -s " " |cut -f 6- -d " " '
##
get_folder_cmd = ' find -type d '
get_file_cmd = ' find -type f  | xargs ls -lc --time-style="+%d-%m-%Y-%H:%M:%S" | tr -s " " |cut -f 6- -d " " '
folder_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_folder_cmd+" '"
file_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_file_cmd  +" '"
folder_directory = check_output(folder_CMD,shell = True)
file_directory   = check_output(file_CMD,shell = True)


# folder_directory = check_output("sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_folder_cmd+" '",shell = True)
# file_directory   = check_output("sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_file_cmd  +" '",shell = True)

folder_list = folder_directory.split("\n")
file_list = file_directory.split("\n")

folder_list
file_list


os.system("sshpass -p 'qwe51006' rsync --recursive '/home/tappy/Desktop/Server/Toy.tar.gz' tappy@192.168.0.104:/home/tappy/Desktop/wewq/ < /dev/null")
os.system("sshpass -p 'qwe51006' rsync --recursive '/home/tappy/Desktop/Server/Toy.tar.gz' tappy@192.168.0.104:/home/tappy/Desktop/123/ ")

def get_Sync_dir():
    get_folder_cmd = ' find -type d '
    get_file_cmd = ' find -type f  | xargs ls -lc --time-style="+%d-%m-%Y-%H:%M:%S" | tr -s " " |cut -f 6- -d " " '
    folder_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_folder_cmd+" '"
    file_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+sync_folder+" ; "+get_file_cmd  +" '"
    folder_directory = check_output(folder_CMD,shell = True)
    file_directory   = check_output(file_CMD,shell = True)
    folder_list = folder_directory.split("\n")
    file_list = file_directory.split("\n")
    return folder_list[1:-1],file_list[:-1]

def get_Server_dir():
    get_folder_cmd = ' find -type d '
    get_file_cmd = ' find -type f  | xargs ls -lc --time-style="+%d-%m-%Y-%H:%M:%S" | tr -s " " |cut -f 6- -d " " '
    folder_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+server_folder+" ; "+get_folder_cmd+" '"
    file_CMD = "sshpass -p '"+pwd+"' ssh -o 'StrictHostKeyChecking=no' "+HOST+" 'cd "+server_folder+" ; "+get_file_cmd  +" '"
    folder_directory = check_output(folder_CMD,shell = True)
    file_directory   = check_output(file_CMD,shell = True)
    folder_list = folder_directory.split("\n")
    file_list = file_directory.split("\n")
    return folder_list[1:-1],file_list[:-1]

Sync_folder,Sync_file = get_Sync_dir()
Server_folder,Server_file = get_Server_dir()

print "Sync_folder : ", Sync_folder , "\n"
print "Sync_file : ", Sync_file , "\n"
print "Server_folder : ", Server_folder , "\n"
print "Server_file : ", Server_file , "\n"
Sync_file_list = [S.split() for S in Sync_file] 
Server_file_list = [F.split()for F in Server_file] 
Server_file_list[1][2]