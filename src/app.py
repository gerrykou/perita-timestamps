#!/usr/bin/env python3
from pyfiglet import Figlet
import argparse, sys, datetime, pytz

VAR_CHOICES={'1h' : 'an hour', '1d':'a day', '1mo':'a month', '1y':'a year'}
FORMAT = "%Y%m%dT%H%M%SZ"
def show_title():
    """Show the program title
    """
    f = Figlet(font='standard')
    print(f.renderText('peri task timestamps'))

def parse_args():
    parser = argparse.ArgumentParser( description = 'Print periodic tasks timestamps')
    #parser.add_argument("--period", metavar='', type=str, required=True, choices=VAR_CHOICES.keys(), help="The supported periods are: 1h, 1d, 1mo, 1y.")
    parser.add_argument("--period", metavar='', type=str, required=True, help="The supported periods are: 1h, 1d, 1mo, 1y.")
    parser.add_argument("--t1",metavar='', required=True, help="t1 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--t2",metavar='', required=True, help="t2 in UTC with seconds accuracy, in the following form: 20060102T150405Z")
    parser.add_argument("--tz",metavar='', type=str, required=True, help="timezone e.g --tz=Europe/Athens")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-v','--verbose', action='store_true', default=False, help="increase the verbosity level")
    output = parser.parse_args()

    if output.period not in VAR_CHOICES:
        parser.error("ERROR: Unsupported period")

    _validate_timezone(output.tz,parser)

    date_list=[output.t1,output.t2]
    for input_date in date_list:
        _validate_datetime(input_date,parser)
        
    return output


def _validate_timezone(input_timezone,parser):
    if input_timezone in pytz.all_timezones:
        pass
    else:
        parser.error('Invalid timezone string!')


def _validate_datetime(input_date,parser):
    #print(input_date)
    try:
        datetime.datetime.strptime(input_date, FORMAT)
    except ValueError:
        parser.error("This is not a correct date string format. It should be YYYYMMDDTHHMMSSZ, try --help for more info")


def main():
    show_title()
    args = parse_args()
    
    #PERIOD = args.period
    #T1 = args.t1
    #T2 = args.t2
    #TZ = args.tz
    #print (PERIOD,T1,T2,TZ)
    #timevar=datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    #print(timevar)
    while True:
        try:
            print("Program arguments:")
            print(args)
            sys.exit(0)
        except ValueError:
            if period not in VAR_CHOICES.keys():
                print('ERROR: Unsupported period')
            sys.stderr.write("spam\n")
            sys.exit(10)


    
    

    
if __name__ == "__main__":
    main()