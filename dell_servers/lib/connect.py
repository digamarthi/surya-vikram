import paramiko
class SSHClient: 
    def __init__(self,server_ip,username,password):
        self.server_ip = server_ip
        self.username = username
        self.password = password

    def exec_command(self,cmd):
        """this method is used to connect remote ssh machine and execute command
        param cmd
        return"""
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.server_ip,username=self.username,password=self.password)
        _stdin, _stdout, _stderr = client.exec_command(cmd)
        out = _stdout.read().decode()
        # return out.decode()
        client.close()
        return out


# b1 = SSHClient("192.168.0.109","winteck","Winteck@2023")
#
# print(type(b1))
# out = b1.exec_command("lsblk")
# print(out)

