<p align="center">
  <img src="https://img.shields.io/badge/Author-moayad--star-orange">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
  <img src="https://img.shields.io/badge/Version-v1.3-green">
</p>

# router_ip 

Show all embedded links as a router 

It written in Python 

It is open source and modifiable (The main code must be indicated) 


## more description 

The tool displays all links for internal routers 

***
Such as 


* Wireless Surveillance Cameras 

* wireless printers 

* server (if any) 

* Devices that support Port 80 

* wifi router 

* router tuning system (os) 

* internet receiver 


##  Mechanism of Action 


![Mechanism of Action](https://user-images.githubusercontent.com/60769512/185748020-f8242509-021b-476c-a11b-34eb5e25167c.jpg)



## requirements 

* python3.x


* Library requests (install from "pip3 install requests) 


* Network 


* Patience (the tool checks more than 65,025 IP address)


## Install for Linux and Termux :

> Upgrade your software
```
apt upgrade -y 
```

> install git

```
apt install git 
```

> install python latest version

```
apt install python3 
```

> Download requirements

```
pip install requests 
```

> install router_ip

```
git clone https://github.com/moayad-star/router_ip.git
```

> open it

```
cd router_ip 
```

> now can you run it from 

```
python3 router_ip.py 
```

> If you encounter runtime errors , run

```
bash requirements.sh
```


## USE 

> for start

```
python3 router_ip.py
```
> To make an update (if available)
```
python3 update.py 
```
## Screenshot 

![router_ip](https://user-images.githubusercontent.com/60769512/185744673-993faeec-a77b-4d41-8eb1-182cd6608181.png)


## NOTE 


* Make sure you are close to the network 
* The links will be displayed directly on the terminal, but the tool will not end until after a deep examination, so it will take about 5 minutes to complete 


#### common problems 

* Sometimes you find strange web pages, you should ignore them, as it is a problem of the interference of external services with internal services

## lssues ?
Feel free to ask your issues [here](https://github.com/moayad-star/router_ip/issues)
