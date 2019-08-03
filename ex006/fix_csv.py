import argparse
import csv


parser = argparse.ArgumentParser()
parser.add_argument('pipe_filename')
parser.add_argument('csv_filename')
parser.add_argument('--in-delimiter', help="the input delimiter", type=str, default=None)
parser.add_argument('--in-quote', help="the input quote character", type=str, default='"')
args = parser.parse_args()

lines = []

if not args.in_delimiter:
    with open(args.pipe_filename, 'r') as fr:
        dialect = csv.Sniffer().sniff(fr.read(1024))
        fr.seek(0)
        csv_reader = csv.reader(fr, dialect)
        for line in csv_reader:
            lines.append(line)

else:
    args.in_delimiter == '|'
    with open(args.pipe_filename, 'r') as fr:
        csv_reader = csv.reader(fr, delimiter=args.in_delimiter,
                                quotechar=args.in_quote)
        for line in csv_reader:
            lines.append(line)

with open(args.csv_filename, 'w', newline='') as fw:
    csv_writer = csv.writer(fw, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for line in lines:
        csv_writer.writerow(line)



