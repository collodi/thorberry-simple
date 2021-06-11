import requests
import xmltodict
import pifaceio
import time

def get_status():
    r = requests.get('http://maclay.thormobile3.net/FL0654.xml')
    data = xmltodict.parse(r.content)['loadmovie']
    return data['thordata']['lightningalert']

def set_light(pf, value):
    pf.write_pin(0, not value)
    pf.write()

def main():
    pf = pifaceio.PiFace()
    prev_extreme = 0 # 0 = AllClear, 1 = RedAlert

    while(True):
        status = get_status()

        if status == 'AllClear':
            prev_extreme = 0
            set_light(pf, 0)
        elif status == 'Caution':
            set_light(pf, prev_extreme)
        elif status == 'Warning':
            set_light(pf, 1)
        elif status == 'RedAlert':
            prev_extreme = 1
            set_light(pf, 1)
        else:
            # WTF?
            pass

        time.sleep(5)

if __name__ == '__main__':
    main()
