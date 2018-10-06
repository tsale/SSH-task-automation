#!/usr/bin/python3
#!/usr/bin/env python

from pexpect import pxssh
import subprocess
import argparse


def args():
  global ip
  global ssh_key
  global command
  global username
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", "--ip", help="-Specify the host/ip",required=True)
  parser.add_argument("-k,", "--ssh_key", help="-k   Specify the ssh key to use",required=False)
  parser.add_argument("-c,", "--command", help="-c   Specify the command/commands to run",required=False)
  parser.add_argument("-u", "--username", help="-Specify the usrname to use to connect",required=True)

  args = parser.parse_args()
  ip = args.ip
  ssh_key = args.ssh_key
  command = args.command
  username = args.username

def ssh_session(ip, username, command, ssh_key):
    s = pxssh.pxssh()
    s.login(ip, username, ssh_key=ssh_key) #Remove "SSH_key" if not applicable and replace it with password. You can leverage getpass module for using password to login.

    try:
        s.sendline("{0}".format(command))  #Run the command (run multiple commands by seperating them with ";")
        s.prompt()
        print(s.before)  #Print the results of the above command
        s.logout()
    except:
        print ("pxssh failed on login.")
        

if __name__ == "__main__":
  try:
    args()
  except:
    print("\nTry puting the commands in quotation marks\n\n")
  try:
    ssh_session(ip, username, command, ssh_key)
  except BaseException as error:
    print('An exception occurred: {}'.format(error))



