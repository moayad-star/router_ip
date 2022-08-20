echo "The requirements will be installed automatically"
echo "Don't worry"
echo "press Enter to continue ↓"
read $enter
apt upgrade -y
apt install python3
pip install requests

echo "


Been completed"
echo "run : python3 router_ip.py"
