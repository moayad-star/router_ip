
# router_ip 

Show all embedded links as a router 

It was written in Python 

It is open source and modifiable (The main code must be indicated) 


# more description 

The tool displays all links for internal routers 

Such as 

Wireless Surveillance Cameras 

wireless printers 

server (if any) 

Devices that support Port 80 

wifi router 

router tuning system (os) 

internet receiver 


#  Mechanism of Action 

It works by sending requests to possible addresses , start from 192.168.0.0 to the end addresses which are 192.168.255.255 

That is, 65.025 requests are sent to addresses between 192.168.0.0-192.168.255.255

# requirements 

* python3.x

* Library requests (install from "pip3 install requests) 

* Network 

* Patience (the tool checks more than 65,025 IP address)

# Install 

$ apt upgrade -y 

$ apt install git 

$ apt install python3 

$ pip install requests 

$ git clone https://github.com/moayad-star/router_ip.git 

$ cd router_ip 

now can you run it from $ python3 router_ip.py 

If you encounter runtime errors , run $ bash auto_install.sh



# USE 

$ python3 router_ip.py



# Screenshot 

![Screenshot_20220819_220811_com termux~3](https://user-images.githubusercontent.com/60769512/185690427-99f7e3c7-5b5a-4759-84f5-f23167cc60f0.jpg) 

# NOTE 


* Make sure you are close to the network 
* The links will be displayed directly on the terminal, but the tool will not end until after a deep examination, so it will take about 5 minutes to complete 


# common problems 

* Sometimes you find strange web pages, you should not ignore them, as it is a problem of the interference of external services with internal services
