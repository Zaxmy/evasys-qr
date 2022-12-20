#!/usr/bin/env python3

# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software 
# Foundation, either version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY 
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A 
# PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <https://www.gnu.org/licenses/>. 
#
#  Copyright Johan Zaxmy (2022)

import qrcode
import os
import argparse
import csv

PSWD =[]

def generate(PSWD,OUTPATH,URL):
    out_csv = []
    for pswd in PSWD:
        qr = qrcode.QRCode()
        qr.add_data("%s%s"%(URL,pswd))
        qr.make(fit = True)
        img = qr.make_image()
        filename = os.path.abspath(os.path.join(OUTPATH,pswd))
        img.save(f"{filename}.png")
        out_csv.append({"pswd":pswd,"@pswd_path":f"{filename}.png"})
        del qr, img
    with open(os.path.abspath(os.path.join(OUTPATH,"list.csv")),"w",newline='') as cvsfile:
        writer = csv.DictWriter(cvsfile,fieldnames=['pswd','@pswd_path'],delimiter=';')
        writer.writeheader()
        writer.writerows(out_csv)



parser = argparse.ArgumentParser(
    prog = "evasys-qr",
    description = "Generates QR codes with encoded URL's for Evasys evaulations"
)

parser.add_argument('-c','--csv-pswd', dest='csv_file',default='PSWDs-example.csv')
parser.add_argument('-u','--url',dest='url',default='https://evasys.his.se/evasys/public/online/index?user_tan=')
parser.add_argument('-o','--output-path',dest='outputPath',default='./output')

args = parser.parse_args()

with open(args.csv_file) as cvsfile:
    reader = csv.DictReader(cvsfile,fieldnames=['pswd'])
    for row in reader:
        PSWD.append(row['pswd'])
    cvsfile.close()

generate(PSWD,args.outputPath,args.url)
