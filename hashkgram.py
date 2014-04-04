#!user/bin/env python
#-*- encoding:utf-8 -*-

import os

k = 7
w = 10
d = 256
q = 101
wt = 0

lexical_path = '../gitLearning/standard_files/'
for file_name in os.listdir(lexical_path):
    i = 0
    h = 1
    times = 0
    fingerpri = 1000
    locate = 0
    value_kgram = [1]
    file_size = 0

    fingerprints = {}
    kgram_list = []
    kgram = []
    window = []

    file_size = os.path.getsize(os.path.join(lexical_path,file_name))
    with open(os.path.join(lexical_path,file_name),'r') as files:
        while i <= file_size - k - 1:                             #create k-gram
            i += 1
            kgram_list.append(files.read(k)) 
            files.seek(i,0)

#pow(h,k-1)%q
    for i in range(1,k):
        h = (h * d) %q

#the value of the first k-gram
    kgram = kgram_list[0]
    for bit_range in range(0,k):
        value_kgram[0] = (value_kgram[0] * d + ord(kgram[bit_range])) % q

#all of the value of k-gram
    for kgram_range in range(1,file_size - 8):
        value_kgram.append((d * (value_kgram[kgram_range - 1] - 
            h * ord(kgram_list[kgram_range - 1][0])) + ord(kgram_list[kgram_range][6])) % q)

    for window_range in range(0,len(value_kgram) - 9):
        window = value_kgram[window_range:window_range + 10]
        for min_locate in range(0,10):
            if window[min_locate] <= fingerpri:
                fingerpri = window[min_locate]
                locate = min_locate + window_range
        if fingerprints.get(locate) == None:
            fingerprints[locate] = fingerpri;
        fingerpri = 1000
    
    wt += 1
    fingerprint_path = '../gitLearning/fingerprints/'
    with open(os.path.join(fingerprint_path,str(wt)),'w+') as write_file:
        print fingerprints
        write_file.write(str(fingerprints))

