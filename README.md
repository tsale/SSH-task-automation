# SSH-task-automation

This is a simple script that uses ssh to login to a host, run commands and exit itself whilst providing the output of the commands.


<h2>Usage</h2>

       ssh_login.py [-h] --ip IP [-k, SSH_KEY] [-c, "COMMAND"] -u USERNAME

    optional arguments:
        -h, --help            show this help message and exit
                     --ip IP, --ip IP      -Specify the host/ip
        -k, SSH_KEY, --ssh_key SSH_KEY<br>
                     -k Specify the ssh key to use
        -c, COMMAND, --command "COMMAND"  #Put your commands in quotation marks and seperate them with ';'"
                     -c Specify the command/commands to run
        -u USERNAME, --username USERNAME
                     -Specify the username to use in order to connect
