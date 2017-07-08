import os
import sys
import urllib
import fileinput
import glob
import csv
import shapefile
#from ntmlinks import list

def run():

    #def download(url):
    #    webFile = urllib.urlopen(url)
    #    localFile = open('ntm/data/' + 'Chart' + url.split('=')[1] + '.txt', 'w')
    #    localFile.write(webFile.read())
    #    webFile.close()
    #    localFile.close()

    #for i in list:
    #    download(i)
    #    print('Downloading' + ' ' + i)

    file_list = glob.glob("ntm/data/Chart" + "*" + "*.txt")

    with open('ntm/data/' + 'NTM.txt', 'wb') as file:
        file.write('Chart	Action	ItemName	ChartingLa	Latitude	Longitude	LatDD	LongDD	PublishedD	Kapp	RNCPanel	RNCPosted\n')
        for i in file_list:
            j = fileinput.input(i)
            j.next()
            j.next()
            file.writelines(j)

    # clean data
    f1 = open('ntm/data/NTM.txt', 'r')
    f2 = open('ntm/data/NTM_Clean.txt', 'w')
    for line in f1:
        f2.write(line.replace('&', 'and'))
    f1.close()
    f2.close()

    def getWKT_PRJ(epsg_code):
        import urllib
        wkt = urllib.urlopen("http://spatialreference.org/ref/epsg/{0}/prettywkt/".format(epsg_code))
        remove_spaces = wkt.read().replace(" ", "")
        output = remove_spaces.replace("\n", "")
        return output

    ntm_shp = shapefile.Writer(shapefile.POINT)

    ntm_shp.autoBalance = 1

    ntm_shp.field('Chart','C')
    ntm_shp.field('Action','C')
    ntm_shp.field('ItemName','C')
    ntm_shp.field('ChartingLa','C')
    ntm_shp.field('Latitude','C')
    ntm_shp.field('Longitude','C')
    ntm_shp.field('LatDD','C')
    ntm_shp.field('LongDD','C')
    ntm_shp.field('PublishedD','C')
    ntm_shp.field('Kapp','C')
    ntm_shp.field('RNCPanel','C')
    ntm_shp.field('RNCPosted','C')

    counter = 1

    with open('ntm/data/NTM_Clean.txt', 'rb') as f:
        reader = csv.DictReader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        next(reader, None)
        for row in reader:
            Chart = row['Chart']
            Action = row['Action']
            ItemName = row['ItemName']
            ChartingLa = row['ChartingLa']
            Latitude = row['Latitude']
            Longitude = row['Longitude']
            LatDD = row['LatDD']
            LongDD = row['LongDD']
            PublishedD = row['PublishedD']
            Kapp = row['Kapp']
            RNCPanel = row['RNCPanel']
            RNCPosted = row['RNCPosted']

            ntm_shp.point(float(LongDD),float(LatDD))

            ntm_shp.record(Chart,Action,ItemName,ChartingLa,Latitude,Longitude,LatDD,LongDD,PublishedD,Kapp,RNCPanel,RNCPosted)

            print("Feature " + str(counter) + " added to Shapefile.")
            counter = counter + 1

        ntm_shp.save("ntm/data/NTM")

        prj = open("ntm/data/NTM.prj", "w")
        epsg = getWKT_PRJ("4326")
        prj.write(epsg)
        prj.close()
