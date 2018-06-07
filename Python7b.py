#Still some cleanup and plenty of room for improvement
#Author: Luke McCormick
#Date Modified: 06/07/2018



# Tell the script what modules to use
import netmiko
from netmiko import ConnectHandler
from datetime import datetime
import os.path
import os
import time
import csv
import sys
#Open CSV with Switch connection information
#list.csv must be formatted in the following manner, with these headers
#Switch Name,type,ip,username,password

infile = open('list.csv', 'r')
reader = csv.DictReader(infile)

for row in reader:
	hostname = (row['name'])
	device_type = (row['type'])
	ip = (row['ip'])
	username = (row['username'])
	password = (row['password'])
	
	device = {'device_type': device_type, 'ip': ip,	'username': username, 'password': password}
	
	outfile = (hostname + ".txt")
	f = open(outfile,"w")
	net_connect = ConnectHandler(**device)
	ShVlan = net_connect.send_command("sh vlan".format(device['ip']))
	ShIp = net_connect.send_command("sh ip".format(device['ip']))
	ShIpRoute = net_connect.send_command("sh ip route".format(device['ip']))
	ShSpannChange = net_connect.send_command("sh spann | inc Change".format(device['ip']))
	ShSpannRoot = net_connect.send_command("sh spann | inc Root".format(device['ip']))
	ShSpannBlock = net_connect.send_command("sh spann | inc Block".format(device['ip']))
	ShLLDPInfRem = net_connect.send_command("sh lldp inf rem".format(device['ip']))
	ShLLDPInfRemAll = net_connect.send_command("sh lldp inf rem all".format(device['ip']))
	ShIntBrie = net_connect.send_command("sh int brie".format(device['ip']))
	ShInt = net_connect.send_command("sh int".format(device['ip']))
		
	
	f.write(ShVlan)
	f.write(ShIp)
	f.write(ShIpRoute)
	f.write(ShSpannChange)
	f.write(ShSpannRoot)
	f.write(ShSpannBlock)
	f.write(ShLLDPInfRem)
	f.write(ShLLDPInfRemAll)
	f.write(ShIntBrie)
	f.write(ShInt)
	
	f.close()
	
