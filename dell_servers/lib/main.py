# import datetime
import re
from logger import get_logger
from connect import SSHClient



log = get_logger(__file__)

#pylint == to check the code and its structure(pep8 standards) in correct format or not.

class MainLib:
    """ """

    def __init__(self,server_ip,username,password):
        self.server_ip = server_ip
        self.username = username
        self.password = password
        self.connect = SSHClient(self.server_ip, self.username, self.password)

    # def get_server_uptime(self):
        """
        This method is used to get the serer uptime
        :return: int
        """
    #     server_uptime = self.connect.exec_command("uptime")
    #     uptime = re.search(r"(\d+:\d+:\d+)", server_uptime)
    #     log.info(f"server uptime is {uptime.group(0)}")
    #     return uptime.group(0)
    #
    # def get_lscpu(self):
    #     cpu_model= self.connect.exec_command("lscpu")
    #     model_name=re.search(r"Model name:\s+(.+)",cpu_model)
    #     return model_name.group()
    def get_server_drives(self):
        drives_list=self.connect.exec_command("lsblk")
        server_drives = re.findall("sd[a-z]+",drives_list)
        return server_drives
    # def get_firmware_version(self,drive_names):
    #     firm_drive = self.connect.exec_command(f"smartctl -a {drive_names}")
    #     version = re.search("Revision:\s*(\w+)",firm_drive)
    #     if version:
    #         return version.group(1)
    #     else:
    #         return None
    def create_partition(self,new,partition_number,last_sector,drivename):
        partition_drives = self.connect.exec_command(f"echo -e '{new}\np\n{partition_number}\n\n{last_sector}\nw\n' | fdisk {drivename}")
        return partition_drives

    # def get_drive_performance(self, drive_name, test_name, block_size, quedepth, type_io, time):
    #     performance = self.connect.exec_command(f"fio --filename={drive_name} --name={test_name} --bs={block_size} --iodepth={quedepth} --rw={type_io} --runtime={time}")
    #     IOPS_match = re.search("IOPS=[\d.k]+", performance)
    #     BW_match = re.search("BW=([\d+]+[KMGTP]?iB/s)", performance)
    #     Lattency_match = re.search(r'\blat\b\s+\(nsec\):\s+min=([\d.]+), max=([\d.]+k), avg=([\d.]+)', performance)
    #     if Lattency_match:
    #         IOPS = IOPS_match.group()
    #         BW = BW_match.group(1)
    #         Lattency = Lattency_match.group(3)
    #         return IOPS, BW, Lattency
    #     else:
    #         return None
    # def get_drive_performance(self,drive_name,filename,block_size,read_write,mix_read,quedepth,time):
    #     drive_performance = self.connect.exec_command(f"fio --filename={drive_name} --name={filename} --bs={block_size} --rw={read_write} --rwmixread={mix_read} --iodepth={quedepth} --runtime={time}")
    #     return drive_performance


    # def get_file(self,filename):
    #     new_file = self.connect.exec_command(f"touch {filename}")
    #     list_files = self.connect.exec_command("ls")
    #     return new_file,list_files

    # def get1_file(self):
    #     list_files=self.connect.exec_command("ls")
    #     return list_files

# b1 = MainLib("192.168.0.106","winteck","Winteck@2023")
b1 = MainLib("192.168.0.105","root","Winteck@2023")
# print(b1.get_server_uptime())
print(b1.get_server_drives())
# print(b1.get_lscpu())

# def input(prompt):
#     user_input = input(prompt)
#     while not user_input:
#         print("Error: Please enter a value.")
#         user_input = input(prompt)
#     return user_input

drivename =input("enter drivename(/dev/sd_):")
while not drivename:
    print("Error: Please enter a drivename.")
    drivename = input("Enter drivename (/dev/sd_):")
    # if drivename == "":
    #     print("please give value")
new = input("Select (default p):")
partition_number = input("Partition number (1-4, default 1):")
last_sector = input("Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-585937499, default 585937499):")
#
#
print(b1.create_partition(new,partition_number,last_sector,drivename))

# k = input("enter file name: ")
# print(b1.get_file(k))
# print(b1.get1_file())
# data = b1.get_server_drives()
# for i in range(len(data)):
#     drive_names = "/dev/"+data[i]
#     fw_version = b1.get_firmware_version(drive_names)
#     if fw_version is not None:
#         print(drive_names + " : " + fw_version)

# a =input("enter drivename:")
# b =input("enter name :")
# c =input("enter blocksize:")
# d =input("enter iodepth:")
# e =input("enter rand/write :")
# f =input("enter runtime:")
# output_text = b1.get_drive_performance(a,b,c,d,e,f)
#
# if output_text:
#     IOPS, BW, Lattency = output_text
#     with open("Performanceondrives.txt", "a") as file:
#         file.write(f"Drive Name {a}\n")
#         file.write(f"Test Name {b}\n")
#         file.write(f"Block Size {c}\n")
#         file.write(f"Que depth {d}\n")
#         file.write(f"Type of IO {e}\n")
#         file.write(f"Run time {f}\n")
#         file.write(f"IOPS {IOPS}\n")
#         file.write(f"Throughput {BW}\n")
#         file.write(f"Average Lattency {Lattency}\n")
#         file.write(f"************************************\n")
# else:
#     print("error")




























# import re
# output_text = """test69: (g=0): rw=read, bs=(R) 512B-512B, (W) 512B-512B, (T) 512B-512B, ioengine=psync, iodepth=32
# fio-3.28
# Starting 1 process
#
# test69: (groupid=0, jobs=1): err= 0: pid=4577: Tue Sep 12 13:14:42 2023
#   read: IOPS=661k, BW=323MiB/s (338MB/s)(18.9GiB/60001msec)
#     clat (nsec): min=864, max=9900.7k, avg=1208.11, stdev=6891.51
#      lat (nsec): min=899, max=9900.7k, avg=1242.95, stdev=6892.78
#     clat percentiles (nsec):
#      |  1.00th=[   892],  5.00th=[   900], 10.00th=[   908], 20.00th=[   916],
#      | 30.00th=[   916], 40.00th=[   924], 50.00th=[   924], 60.00th=[   940],
#      | 70.00th=[   956], 80.00th=[  1020], 90.00th=[  1112], 95.00th=[  1144],
#      | 99.00th=[  2352], 99.50th=[  4128], 99.90th=[100864], 99.95th=[101888],
#      | 99.99th=[107008]
#    bw (  KiB/s): min=166477, max=345768, per=100.00%, avg=330691.23, stdev=31032.58, samples=119
#    iops        : min=332954, max=691536, avg=661382.81, stdev=62065.16, samples=119
#   lat (nsec)   : 1000=76.48%
#   lat (usec)   : 2=21.60%, 4=1.42%, 10=0.18%, 20=0.13%, 50=0.01%
#   lat (usec)   : 100=0.07%, 250=0.12%, 500=0.01%, 750=0.01%, 1000=0.01%
#   lat (msec)   : 2=0.01%, 4=0.01%, 10=0.01%
#   cpu          : usr=44.37%, sys=54.69%, ctx=68369, majf=0, minf=15
#   IO depths    : 1=100.0%, 2=0.0%, 4=0.0%, 8=0.0%, 16=0.0%, 32=0.0%, >=64=0.0%
#      submit    : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
#      complete  : 0=0.0%, 4=100.0%, 8=0.0%, 16=0.0%, 32=0.0%, 64=0.0%, >=64=0.0%
#      issued rwts: total=39664815,0,0,0 short=0,0,0,0 dropped=0,0,0,0
#      latency   : target=0, window=0, percentile=100.00%, depth=32
#
# Run status group 0 (all jobs):
#    READ: bw=323MiB/s (338MB/s), 323MiB/s-323MiB/s (338MB/s-338MB/s), io=18.9GiB (20.3GB), run=60001-60001msec
#
# Disk stats (read/write):
#   sdg: ios=154634/0, merge=0/0, ticks=61132/0, in_queue=61132, util=99.91%"""
# # Define a function to extract a specific value using a regular expression
# def extract_value(pattern, text):
#     match = re.search(pattern, text)
#     return match.group(1) if match else "N/A"
#
# # Extract IOPS, BW, and alt(nsec) values using the function
# iops = extract_value(r'IOPS=([\d\.k]+)', output_text)
# bw = extract_value(r'BW=([\d\.MiB/s]+)', output_text)
# alt_nsec = extract_value(r'lat (nsec): min=([\d+])', output_text)
#
# # Print the extracted values
# print(f"IOPS: {iops}")
# print(f"BW: {bw}")
# print(f"alt(nsec): {alt_nsec}")
#
# # Define the output file name
# output_file_name = "performance.txt"
#
# # Write the extracted values to a file
# with open(output_file_name, "w") as output_file:
#     output_file.write(f"IOPS: {iops}\n")
#     output_file.write(f"BW: {bw}\n")
#     output_file.write(f"alt(nsec): {alt_nsec}\n")
#
# print(f"Extracted values have been saved to '{output_file_name}'")






















