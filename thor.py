import requests
import json
import pifaceio
import time

def get_status():
    ms = round(time.time() * 1000)
    r = requests.get(
                'http://360.thormobile.net/thorcloud/api/productionpackets/GetBySystemID',
                params = { 'ids': 3360, 'ms': ms }
        )

    data = json.loads(r.content)
    data = data[list(data.keys())[0]]
    return data['FriendlyAdvisoryLevel']

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
