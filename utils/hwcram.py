#!/usr/bin/python3
# coding: utf-8
from utils.sync_deal import SyncAll
from multiprocessing import Pool
from time import sleep


def sync_deal():
    opsync = SyncAll()
    opsync.fill_token()
    opsync.update_token()
    opsync.fill_ecs()
    opsync.add_ecs()
    opsync.update_ecs()
    opsync.delete_ecs()
    opsync.status_ecs()
    opsync.delete_time_ecs()
    opsync.delete_tag_ecs()
    opsync.shutoff_tag_ecs()
    #opsync.deal_ecs()

def main():
    while True:
        p = Pool(processes=1)
        p.apply_async(sync_deal)
        p.close()
        p.join()
        sleep(3)

if __name__ == '__main__':
    main()
