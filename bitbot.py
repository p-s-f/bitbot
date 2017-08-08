import time
import sys, getopt

def main(argv):
    period = 10

    try:
        opts, args = getopt.getopt(argv, "hp:", ["period=",])
    except getopt.GetoptError:
        print 'bitbot.py -p <period>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print 'bitbot.py -p <period>'
            sys.exit()
        elif opt in ("-p", "--period"):
            if (int(arg) in [300,900,1800,7200,14400,86400]):
                period = arg
            else:
                print 'Poloniex requires periods in [300,900,1800,7200,14400,86400] seconds'
                sys.exit(2)

    while True:
        print "period"
        time.sleep(int(period))

if __name__ == "__main__":
    main(sys.argv[1:])      