import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('pipe_filename')
parser.add_argument('csv_filename')
parser.add_argument('--in-delimiter', help="the initial delimiter", type=str, default="|")
parser.add_argument('--in-quote', help="quote character", type=str, default="'")
args = parser.parse_args()

lines = []

with open(args.pipe_filename, 'r') as fr:
    csv_reader = csv.reader(fr, delimiter=args.in_delimiter,
                            quotechar=args.in_quote)
    for line in csv_reader:
        lines.append(line)

with open(args.csv_filename, 'w') as fw:
    csv_writer = csv.writer(fw, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for line in lines:
        csv_writer.writerow(line)



