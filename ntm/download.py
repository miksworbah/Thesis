import os
import sys
import urllib
import fileinput
import glob
import csv
import shapefile

def run():
   # list = ['https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12300',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12304',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12311',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12312',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12313',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12314',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12316',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12317',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12318',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12323',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12324',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12325',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12326',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12327',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12331',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12332',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12333',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12334',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12335',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12337',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12338',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12339',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12341',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12342',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12343',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12345',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12346',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12347',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12348',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12350',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12352',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12353',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12354',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12358',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12362',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12363',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12364',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12365',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12366',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12367',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12368',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12369',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12370',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12371',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12372',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12373',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12374',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12375',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12377',
   #         'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12378',
   #           'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12401',
   #           'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12402',
   #           'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=13003']
   #
   #   def download(url):
   #       webFile = urllib.urlopen(url)
   #       localFile = open('ntm/data/' + 'Chart' + url.split('=')[1] + '.txt', 'w')
   #       localFile.write(webFile.read())
   #       webFile.close()
   #       localFile.close()
   #
   #   for i in list:
   #       download(i)
   #       print('Downloading' + ' ' + i)

  file_list = glob.glob("src/ntm/data/Chart" + "*" + "*.txt")

  with open('src/ntm/data/' + 'NTM.txt', 'wb') as file:
      file.write('Chart	Action	ItemName	ChartingLa	Latitude	Longitude	LatDD	LongDD	PublishedD	Kapp	RNCPanel	RNCPosted\n')
      for i in file_list:
          j = fileinput.input(i)
          j.next()
          j.next()
          file.writelines(j)

  # clean data
  f1 = open('src/ntm/data/NTM.txt', 'r')
  f2 = open('src/ntm/data/NTM_Clean.txt', 'w')
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

  with open('src/ntm/data/NTM_Clean.txt', 'rb') as f:
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

      ntm_shp.save("src/ntm/data/NTM")

      prj = open("src/ntm/data/NTM.prj", "w")
      epsg = getWKT_PRJ("4326")
      prj.write(epsg)
      prj.close()
