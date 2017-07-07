import os
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
from django.contrib.gis.utils import LayerMapping
from models import NTM

### Auto-generated `LayerMapping` dictionary for NTM model
ntm_mapping = {
    'chart' : 'Chart',
    'action' : 'Action',
    'itemname' : 'ItemName',
    'chartingla' : 'ChartingLa',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'latdd' : 'LatDD',
    'longdd' : 'LongDD',
    'publishedd' : 'PublishedD',
    'kapp' : 'Kapp',
    'rncpanel' : 'RNCPanel',
    'rncposted' : 'RNCPosted',
    'geom' : 'POINT',
}

ntm_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'NTM.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        NTM, ntm_shp, ntm_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)

