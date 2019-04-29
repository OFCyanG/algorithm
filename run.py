from main import *
import sys

al = Humidity(int(sys.argv[1]), int(sys.argv[2]))

print(al.MakeDecision())

