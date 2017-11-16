# Interoperability of Digital Geographic Information in the Domain of Maritime Navigation

## Abstract

> This thesis examines interoperability of digital geographic information (DGI) in the context of maritime navigation. Maritime navigation is a complex domain that draws on a wide variety of information resources. The diversity and multitude of such information creates challenges with respect to interoperability – the ability of software and hardware systems on multiple machines from multiple vendors to communicate with each other meaningfully. The Open Geospatial Consortium (OGC) is continually developing a series of standards for DGI that may provide solutions for DGI interoperability in the domain of maritime navigation. This thesis examines the OGC Web Services (OWS) and how the Web Feature Service (WFS) can be adopted to serve Notice to Mariners (NTM).

> Keywords: Geospatial Intelligence, Maritime Navigation, Interoperability

> Michael R. Rushin

> M.S. George Mason University, 2017

> Faculty Advisor: Dr. Phil Yang

## Table of Website Contents

- [Blog](https://github.com/mrushin/Thesis/tree/master/blog)
- [NTM](https://github.com/mrushin/Thesis/tree/master/ntm)
- [Resume](https://github.com/mrushin/Thesis/tree/master/resume)
- [Static](https://github.com/mrushin/Thesis/tree/master/static)
- [Templates](https://github.com/mrushin/Thesis/tree/master/templates)
- [Thesis](https://github.com/mrushin/Thesis/tree/master/thesis)
- [WFS](https://github.com/mrushin/Thesis/tree/master/wfs)
- [.gitignore](https://github.com/mrushin/Thesis/blob/master/.gitignore)
- [Procfile](https://github.com/mrushin/Thesis/blob/master/Procfile)
- [README.me](https://github.com/mrushin/Thesis/blob/master/README.md)
- [manage.py](https://github.com/mrushin/Thesis/blob/master/manage.py)
- [requirements.txt](https://github.com/mrushin/Thesis/blob/master/requirements.txt)

## Introduction

> The National Geospatial-Intelligence Agency (NGA) produces Digital Nautical Chart (DNC) Vector Product Format (VPF) Database Update (VDU) to support worldwide DNC navigation requirements of the U.S. Navy, Military Sealift Command (MSC), the U.S. Coast Guard, and certain foreign partners. The DNC maintenance system collects new source materials such as bathymetry, imagery, NTM, local notices, new foreign chart sources, etc. for inclusion in the DNC database. This thesis explores the use of open source software and standards to create a Web Feature Service (WFS) for local Notice to Mariners (LNM) to aid in the DNC maintenance process (Bowditch, 1802).

## OGC Web Services (OWS)

> Web services provide dynamic access, exchange and processing of information via the World Wide Web (WWW). A traditional web service is any web service that is available over the Internet, uses a standardized Extensible Markup Language (XML) messaging system, and is operating system agnostic. A client sends a request over the Internet, a server receives that request, processes it, and returns a response. When a browser makes a request for a web page, it receives Hypertext Markup Language (HTML) and other related content in the response. However, when a browser makes a request for data, a web service has been used. The OGC Web Services (OWS) operate in a similar way and fills two roles: accessing remote data sources as a consumer and serving up or sharing data as a provider for others. 

## Digital Nautical Charts (DNC)

> The DNC database is made up of 29 geographic regions that provide a worldwide footprint of over 5,000 charts of varying scales resulting in global coverage between 84 degrees North and 81 degrees South. The 29 regions are further broken down into libraries. Each library represents a different geographic area of interest and scale. The process of maintaining DNC databases includes manually entering printed NTM chart corrections into a DNC library. A library consists of 12 related feature class thematic layers. They are cultural landmarks, data quality, earth cover, environment, hydrography, inland waterways, land cover, limits, aids to navigation, obstructions, port facilities, and relief. A NTM chart correction will affect one of these layers within it’s corresponding chart bounding box. For geographic regions within U.S. territorial waters, NOAA corrections are used to update DNC databases because the DNC library is comprised of NOAA charts. These are known as local Notice to Mariners. NOAA local NTM, or LNM, are made available in text file format by NOAA and were used as the data in this project (Bowditch, 1802).

## Open Source Software for Internet GIS

> Django WFS is a web feature service implementation as a Django application by Vasco Pinho. Django WFS very loosely follows the OGC Web Feature Service Implementation Specification Version 1.0.0. OGC WFS allows a client to retrieve and update geospatial data encoded in the Geography Markup Language (GML). The Django WFS only offers the GetCapabilities, DescribeFeatureType, and GetFeature requests which makes it a Basic WFS. A basic WFS is defined as only implementing the GetCapabilities, DescribeFeatureType, and GetFeature operations. This is also considered a READ-ONLY WFS (Vretanos, 2002). 

## Django Web Development Framework

> Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. GeoDjango is the spatial counterpart to Django and makes it possible to build GIS Web applications and harness the power of spatially enabled data (Django Documentation, 2017). Django was used to create the website that hosts the NTM WFS.


