from turtle import color
import pandas as pd
import botometer
import xlrd
import csv
import glob
import json
import os
import re
import time
import matplotlib.pyplot as plt

startTime = time.time()

fakeH=0
fakeB=0
realH=0
realB=0
fakeHgc=0
fakeBgc=0
realHgc=0
realBgc=0
fakeHpf=0
fakeBpf=0
realHpf=0
realBpf=0


def gf():
    global fakeB
    global fakeH
    global fakeBgc
    global fakeHgc
    gc_fake = []
    f = open('csv/gossipcop_fake_users.csv')
    reader = csv.reader(f)
    for col in reader:
        gc_fake.append(col[1])
    gc_fake.pop(0)
    h,b = check_bots(gc_fake)
    fakeH+=int(h)
    fakeB+=int(b)
    fakeHgc+=int(h)
    fakeBgc+=int(b)
def gr():
    global realB
    global realH
    global realBgc
    global realHgc
    gc_real = []
    f = open('csv/gossipcop_real_users.csv')
    reader = csv.reader(f)
    for col in reader:
        gc_real.append(col[1])
    gc_real.pop(0)
    h,b = check_bots(gc_real)
    realH+=int(h)
    realB+=int(b)
    realHgc+=int(h)
    realBgc+=int(b)
def pf():
    global fakeB
    global fakeH
    global fakeBpf
    global fakeHpf
    pf_fake = []
    f = open('csv/politifact_fake_users.csv')
    reader = csv.reader(f)
    for col in reader:
        pf_fake.append(col[1])
    pf_fake.pop(0)
    h,b = check_bots(pf_fake)
    fakeH+=int(h)
    fakeB+=int(b)
    fakeHpf+=int(h)
    fakeBpf+=int(b)
def pr():
    global realB
    global realH
    global realBpf
    global realHpf
    pf_real = []
    f = open('csv/politifact_real_users.csv')
    reader = csv.reader(f)
    for col in reader:
        pf_real.append(col[1])
    pf_real.pop(0)
    h,b = check_bots(pf_real)
    realH+=int(h)
    realB+=int(b)
    realHpf+=int(h)
    realBpf+=int(b)


def api():
    rapidapi_key = "9ba67595c1msh35dbb5cab466f80p1943dejsnbb69823c3fab"
    twitter_app_auth = {
        'consumer_key': 'EvcXT4z12RQ37DAKGC4Z4IiWQ',
        'consumer_secret': 'UDAFs1f2MgY5IlZ0qn4YDzhJFtNLMzjhKOhbWdhZPgX0pXiNpw',
        'access_token': '2896267067-xeweJtmx6tzCISaq45xVHltPxV1csMWbMQEJ0oE',
        'access_token_secret': 'FRClARegtb0Caglzi8sdny6w4neHxdt3Ypyy0fuXBit9G',
    }

    bom = botometer.Botometer(wait_on_ratelimit=True,
                            rapidapi_key=rapidapi_key,
                            **twitter_app_auth)
    return bom
# Check a sequence of accounts
def check_bots(names):
    fails = []
    bots = []
    humans = []
    i= 0
    for screen_name, result in api().check_accounts_in(names):
        i+=1
        keyword = "display_scores"
        result = json.dumps(result)
        before_keyword, keyword, after_keyword = result.partition(keyword)
        k = "universal"
        b, k, a = before_keyword.partition(k)
        try:
            if float(a[3:-4])<=0.5:
                humans.append(screen_name)
            else:
                bots.append(screen_name)
        except:
            fails.append(screen_name)
        print(i)

    print("humans: " + str(len(humans)))
    print(humans)
    print("bots: " + str(len(bots)))
    print(bots)
    print("fails: " + str(len(fails)))
    print(fails)
    return len(humans), len(bots)

def make_graph():
    global realB,realH,fakeB,fakeH,realBpf,realHpf,fakeBpf,fakeHpf,fakeBgc,fakeHgc,realBgc,realHgc
    xAxis=['Gossipcop Bots Fakenews','Gossipcop Bots Realnews','Politifact bots Fakenews','Politifact bots Realnews']
    a=(fakeBgc/(fakeBgc+fakeHgc))*100
    b=(realBgc/(realBgc+realHgc))*100
    c=(fakeBpf/(fakeBpf+fakeHpf))*100
    d=(realBpf/(realBpf+realHpf))*100
    yAxis=[a,b,c,d]
    New_Colors = ['red','green','red','green']
    plt.bar(xAxis,yAxis,color=New_Colors)
    plt.title('Fake/Real -news, bots or humans')
    plt.xlabel('Users')
    plt.ylabel('Bot (%)')
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
    plt.show()

def data():
    global realB,realH,fakeB,fakeH,realBpf,realHpf,fakeBpf,fakeHpf,fakeBgc,fakeHgc,realBgc,realHgc
    with open('nikit.txt', 'w') as f:
        f.write('Humans Fakenews: ' + str(fakeH)+'\n'+ 'Humans Realnews: ' + str(realH) + '\n'+ 'Bots Fakenews: ' + str(fakeB) + '\n' + 'Bots Realnews: ' + str(realB))
        f.write('\n'+'---GossipCop---'+'\n'+'Humans Fakenews gc: ' + str(fakeHgc)+'\n'+ 'Humans Realnews gc: ' + str(realHgc) + '\n'+ 'Bots Fakenews gc: ' + str(fakeBgc) + '\n' + 'Bots Realnews gc: ' + str(realBgc))
        f.write('\n'+'---Politifact---'+'\n'+'Humans Fakenews pf: ' + str(fakeHpf)+'\n'+ 'Humans Realnews pf: ' + str(realHpf) + '\n'+ 'Bots Fakenews pf: ' + str(fakeBpf) + '\n' + 'Bots Realnews pf: ' + str(realBpf))

if __name__ == "__main__":
    gf()
    gr()
    pf()
    pr()
    data()
    make_graph()

