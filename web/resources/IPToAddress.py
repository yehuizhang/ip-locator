import maxminddb

reader = maxminddb.open_database('data/GeoLite2-City.mmdb')
print(reader.get('73.252.161.175'));

reader.close()