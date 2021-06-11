# thorberry-simple

Setup
---

Make sure the system is up to date, and spi is enabled.  
The user `pi` should be in groups `gpio` and `spi`.  
You need `python3` and `git`.  

Clone this repo in `pi`'s home directory.  
Run `pip3 install -r requirements.txt` in this project's root.  
Put the `thorberry.service` file in the `/etc/systemd/system` directory.  
Then, `sudo systemctl enable thorberry` and `sudo systemctl start thorberry`.  
Make sure everything is good with `sudo systemctl status thorberry`.  
