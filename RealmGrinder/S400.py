"""A small script for growth inspection."""

td   = lambda hr,min: hr+(min/60)
diff = lambda l1, l2: (l2[1]-l1[1])/(l2[0]-l1[0])
avg  = lambda d: [diff(d[0],i) for i in d[1:]]
part = lambda d: [diff(d[i-1],d[i]) for i in range(1,len(d))]

if __name__ == "__main__":
    import sys, csv
    # h,m,s = sys.argv[1:4]
    with open('S400.csv', 'a', newline='') as db:
        csv.writer(db).writerow(sys.argv[1:4])
    with open('S400.csv', newline='') as db:
        d = [(td(int(l[0]),int(l[1])),float(l[2])) for l in csv.reader(db)]
    print("Current global slope is:", avg(d)[-1])
    print("Current latest slope is:", part(d)[-1])
    if(len(sys.argv)>4 and sys.argv[4]=='T'):
        print('='*32)
        for i in d[1:]:
            print(i)
        print('='*32)
        for i in avg(d):
            print(i)
        print('='*32)
        for i in part(d):
            print(i)
