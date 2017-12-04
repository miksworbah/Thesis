import os
import sys
import urllib
import fileinput
import glob
import csv
import shapefile
#from ntmlinks import list

# Office of Coast Survey - Mid Atlantic - Jacksonville to Georgetown
list = ['https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11488',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11400',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11401',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11402',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11404',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11405',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11406',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11407',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11408',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11409',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11411',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11412',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11415',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11416',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11420',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11424',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11425',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11426',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11427',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11428',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11429',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11430',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11431',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11432',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11433',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11434',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11438',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11439',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11441',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11442',
'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11465']
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11446',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11447',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11448',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11449',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11450',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11451',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11452',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11453',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11459',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11460',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11462',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11463',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11464',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11465',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11466',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11467',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11468',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11469',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11470',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11472',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11474',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11475',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11476',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11478',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11480',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11481',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11484',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11485',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11486',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11487',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11488',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11489',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11490',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11491',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11492',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11495',
#'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=11498'

def run():

    def download(url):
        webFile = urllib.urlopen(url)
        localFile = open('ntm/data/' + 'Chart' + url.split('=')[1] + '.txt', 'w')
        localFile.write(webFile.read())
        webFile.close()
        localFile.close()

    for i in list:
        download(i)
        print('Downloading' + ' ' + i)

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
