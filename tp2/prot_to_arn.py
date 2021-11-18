#!/usr/bin/env python3
import argparse

parser = argparse.ArgumentParser(description='Codifica ARN en base de una secuencia Proteica')
parser.add_argument('-p', '--protein',
                    type=str,
                    help='An amino acid chain to decode to RNA, unsing single character IUPAC notation')


args = parser.parse_args()

aminoDict = {
    "A" : "GCU",
    "R" : "CGU",
    "N" : "AAU",
    "D" : "GAU",
    "C" : "UGU",
    "Q" : "CAA",
    "E" : "GAA",
    "Z" : "CAA",
    "G" : "GGU",
    "H" : "CAU",
    "I" : "AUU",
    "L" : "CUU",
    "K" : "AAA",
    "M" : "AUG",
    "F" : "UUU",
    "P" : "CCU",
    "S" : "UCU",
    "T" : "ACU",
    "W" : "UGG",
    "Y" : "UAU",
    "V" : "GUU"
}

def parseProtein(aProtein):
    rna = ""
    for aminoacid in aProtein:
        rna = rna + aminoDict[aminoacid]
    return rna



print(parseProtein(args.protein))