import os
import sys
import urllib2
import urlparse
import fileinput
import glob
import csv
import osgeo.ogr as ogr
import osgeo.osr as osr

def main():
  list = ['https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12300',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12304',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12311',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12312',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12313',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12314',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12316',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12317',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12318',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12323',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12324',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12325',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12326',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12327',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12331',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12332',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12333',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12334',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12335',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12337',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12338',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12339',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12341',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12342',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12343',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12345',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12346',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12347',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12348',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12350',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12352',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12353',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12354',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12358',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12362',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12363',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12364',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12365',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12366',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12367',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12368',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12369',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12370',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12371',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12372',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12373',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12374',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12375',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12377',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12378',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12401',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=12402',
          'https://ocsdata.ncd.noaa.gov/ntm/Listing_Text.aspx?Chart=13003']

  def download(url):
      webFile = urllib2.urlopen(url)
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

  # use a dictionary reader so we can access by field name
  reader = csv.DictReader(open("ntm/data/NTM_Clean.txt","rb"),
      delimiter='\t',
      quoting=csv.QUOTE_NONE)

  # set up the shapefile driver
  driver = ogr.GetDriverByName("ESRI Shapefile")

  # create the data source
  data_source = driver.CreateDataSource("ntm/data/NTM.shp")

  # create the spatial reference, WGS84
  srs = osr.SpatialReference()
  srs.ImportFromEPSG(4326)

  # create the layer
  layer = data_source.CreateLayer("ntm", srs, ogr.wkbPoint)

  # Add the fields we're interested in
  field_chart = ogr.FieldDefn("Chart", ogr.OFTString)
  field_chart.SetWidth(300)
  layer.CreateField(field_chart)
  field_action = ogr.FieldDefn("Action", ogr.OFTString)
  field_action.SetWidth(300)
  layer.CreateField(field_action)
  field_itemname = ogr.FieldDefn("ItemName", ogr.OFTString)
  field_itemname.SetWidth(300)
  layer.CreateField(field_itemname)
  field_chartingla = ogr.FieldDefn("ChartingLa", ogr.OFTString)
  field_chartingla.SetWidth(300)
  layer.CreateField(field_chartingla)
  field_latitude = ogr.FieldDefn("Latitude", ogr.OFTString)
  field_latitude.SetWidth(300)
  layer.CreateField(field_latitude)
  field_longitude = ogr.FieldDefn("Longitude", ogr.OFTString)
  field_longitude.SetWidth(300)
  layer.CreateField(field_longitude)
  field_longitude = ogr.FieldDefn("LatDD", ogr.OFTString)
  field_longitude.SetWidth(300)
  layer.CreateField(field_longitude)
  field_longitude = ogr.FieldDefn("LongDD", ogr.OFTString)
  field_longitude.SetWidth(300)
  layer.CreateField(field_longitude)
  field_publishedd = ogr.FieldDefn("PublishedD", ogr.OFTString)
  field_publishedd.SetWidth(300)
  layer.CreateField(field_publishedd)
  field_kapp = ogr.FieldDefn("Kapp", ogr.OFTString)
  field_kapp.SetWidth(300)
  layer.CreateField(field_kapp)
  field_rncpanel = ogr.FieldDefn("RNCPanel", ogr.OFTString)
  field_rncpanel.SetWidth(300)
  layer.CreateField(field_rncpanel)
  field_rncposted = ogr.FieldDefn("RNCPosted", ogr.OFTString)
  field_rncposted.SetWidth(300)
  layer.CreateField(field_rncposted)


  # Process the text file and add the attributes and features to the shapefile
  for row in reader:
    # create the feature
    feature = ogr.Feature(layer.GetLayerDefn())
    # Set the attributes using the values from the delimited text file
    feature.SetField("Chart", row['Chart'])
    feature.SetField("Action", row['Action'])
    feature.SetField("ItemName", row['ItemName'])
    feature.SetField("ChartingLa", row['ChartingLa'])
    feature.SetField("Latitude", row['Latitude'])
    feature.SetField("Longitude", row['Longitude'])
    feature.SetField("LatDD", row['LatDD'])
    feature.SetField("LongDD", row['LongDD'])
    feature.SetField("PublishedD", row['PublishedD'])
    feature.SetField("Kapp", row['Kapp'])
    feature.SetField("RNCPanel", row['RNCPanel'])
    feature.SetField("RNCPosted", row['RNCPosted'])

    # create the WKT for the feature using Python string formatting
    wkt = "POINT(%f %f)" %  (float(row['LongDD']) , float(row['LatDD']))

    print("Creating NTM " + wkt)

    # Create the point from the Well Known Txt
    point = ogr.CreateGeometryFromWkt(wkt)

    # Set the feature geometry using the point
    feature.SetGeometry(point)
    # Create the feature in the layer (shapefile)
    layer.CreateFeature(feature)
    # Destroy the feature to free resources
    feature.Destroy()

  # Destroy the data source to free resources
  data_source.Destroy()

if __name__ == "__main__":
  main()
