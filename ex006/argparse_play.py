import argparse


parser = argparse.ArgumentParser()
parser.add_argument('pipe_filename')
parser.add_argument('csv_filename')
parser.add_argument('--in-delimiter', help="the initial delimiter", type=str, default="|")
parser.add_argument('--in-quote', help="quote character", type=str, default="'")
args = parser.parse_args()

print(f"Input Delimiter is ({args.in_delimiter}).\n")
print(f"Input Quote is ({args.in_quote}).\n")
print(f"Pipe Filename is ({args.pipe_filename}).\n")
print(f"CSV Filename is ({args.csv_filename}).\n")
