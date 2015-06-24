import lxml.etree as ET
import sys
from argparse import ArgumentParser
from JSAnalysis import analyse

def main(args):

	f = open(args.js_in, "r")
	js = f.read()
	f.close()

	f = open(args.xml, "r")
	xml = f.read()
	f.close()

	try:
            tree = ET.fromstring(xml)            
        except Exception as e:
            sys.stderr.write("xml_creator cannot create tree: %s\n" % e)

	print analyse(js, tree)


if __name__ == "__main__":
	argparser = ArgumentParser()
	argparser.add_argument('js_in', help="file of js")
	argparser.add_argument('xml', help="xml file")
	args = argparser.parse_args()
	del argparser
	main(args)

