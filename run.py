#!/usr/bin/env python
from kismetclient import Client as KismetClient
from kismetclient import handlers

from pprint import pprint

import logging
log = logging.getLogger('kismetclient')
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)

import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

address = ('127.0.0.1', 2501)
k = KismetClient(address)
#k.register_handler('TRACKINFO', handlers.print_fields)

def handle_alert(client, sec, usec, header, bssid, source, dest, other, channel, text):
	print 'sec: %s usec: %s header: %s bssid: %s source: %s dest: %s other: %s channel: %s text: %s ' % (sec, usec, header, bssid, source, dest, other, channel, text)
	r.publish('the_channel', '{"type": "alert","sec": "%s", "usec": "%s", "header": "%s", "bssid": "%s", "source": "%s", "dest": "%s", "other": "%s", "channel": "%s", "text": "%s"}' % (sec, usec, header, bssid, source, dest, other, channel, text))

def handle_battery(client, percentage, charging, ac, remaining):
	print 'percentage: %s charging: %s ac: %s remaining: %s ' % (percentage, charging, ac, remaining)
	r.publish('the_channel', '{"type": "battery","percentage": "%s", "charging": "%s", "ac": "%s", "remaining": "%s"}' % (percentage, charging, ac, remaining))

def handle_bssid(client, bssid, type, llcpackets, datapackets, cryptpackets, manuf, channel, firsttime, lasttime, atype, rangeip, netmaskip, gatewayip, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints, datasize, turbocellnid, turbocellmode, turbocellsat, carrierset, maxseenrate, encodingset, decrypted, dupeivpackets, bsstimestamp, cdpdevice, cdpport, fragments, retries, newpackets, freqmhz, datacryptset):
	print 'bssid: %s type: %s llcpackets: %s datapackets: %s cryptpackets: %s manuf: %s channel: %s firsttime: %s lasttime: %s atype: %s rangeip: %s netmaskip: %s gatewayip: %s gpsfixed: %s minlat: %s minlon: %s minalt: %s minspd: %s maxlat: %s maxlon: %s maxalt: %s maxspd: %s signal_dbm: %s noise_dbm: %s minsignal_dbm: %s minnoise_dbm: %s maxsignal_dbm: %s maxnoise_dbm: %s signal_rssi: %s noise_rssi: %s minsignal_rssi: %s minnoise_rssi: %s maxsignal_rssi: %s maxnoise_rssi: %s bestlat: %s bestlon: %s bestalt: %s agglat: %s agglon: %s aggalt: %s aggpoints: %s datasize: %s turbocellnid: %s turbocellmode: %s turbocellsat: %s carrierset: %s maxseenrate: %s encodingset: %s decrypted: %s dupeivpackets: %s bsstimestamp: %s cdpdevice: %s cdpport: %s fragments: %s retries: %s newpackets: %s freqmhz: %s datacryptset: %s ' % (bssid, type, llcpackets, datapackets, cryptpackets, manuf, channel, firsttime, lasttime, atype, rangeip, netmaskip, gatewayip, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints, datasize, turbocellnid, turbocellmode, turbocellsat, carrierset, maxseenrate, encodingset, decrypted, dupeivpackets, bsstimestamp, cdpdevice, cdpport, fragments, retries, newpackets, freqmhz, datacryptset)
	r.publish('the_channel', '{"type": "bssid","bssid": "%s", "type": "%s", "llcpackets": "%s", "datapackets": "%s", "cryptpackets": "%s", "manuf": "%s", "channel": "%s", "firsttime": "%s", "lasttime": "%s", "atype": "%s", "rangeip": "%s", "netmaskip": "%s", "gatewayip": "%s", "gpsfixed": "%s", "minlat": "%s", "minlon": "%s", "minalt": "%s", "minspd": "%s", "maxlat": "%s", "maxlon": "%s", "maxalt": "%s", "maxspd": "%s", "signal_dbm": "%s", "noise_dbm": "%s", "minsignal_dbm": "%s", "minnoise_dbm": "%s", "maxsignal_dbm": "%s", "maxnoise_dbm": "%s", "signal_rssi": "%s", "noise_rssi": "%s", "minsignal_rssi": "%s", "minnoise_rssi": "%s", "maxsignal_rssi": "%s", "maxnoise_rssi": "%s", "bestlat": "%s", "bestlon": "%s", "bestalt": "%s", "agglat": "%s", "agglon": "%s", "aggalt": "%s", "aggpoints": "%s", "datasize": "%s", "turbocellnid": "%s", "turbocellmode": "%s", "turbocellsat": "%s", "carrierset": "%s", "maxseenrate": "%s", "encodingset": "%s", "decrypted": "%s", "dupeivpackets": "%s", "bsstimestamp": "%s", "cdpdevice": "%s", "cdpport": "%s", "fragments": "%s", "retries": "%s", "newpackets": "%s", "freqmhz": "%s", "datacryptset": "%s"}' % (bssid, type, llcpackets, datapackets, cryptpackets, manuf, channel, firsttime, lasttime, atype, rangeip, netmaskip, gatewayip, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints, datasize, turbocellnid, turbocellmode, turbocellsat, carrierset, maxseenrate, encodingset, decrypted, dupeivpackets, bsstimestamp, cdpdevice, cdpport, fragments, retries, newpackets, freqmhz, datacryptset))

def handle_bssidsrc(client, bssid, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi):
	print 'bssid: %s uuid: %s lasttime: %s numpackets: %s signal_dbm: %s noise_dbm: %s minsignal_dbm: %s minnoise_dbm: %s maxsignal_dbm: %s maxnoise_dbm: %s signal_rssi: %s noise_rssi: %s minsignal_rssi: %s minnoise_rssi: %s maxsignal_rssi: %s maxnoise_rssi: %s ' % (bssid, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi)
	r.publish('the_channel', '{"type": "bssidsrc","bssid": "%s", "uuid": "%s", "lasttime": "%s", "numpackets": "%s", "signal_dbm": "%s", "noise_dbm": "%s", "minsignal_dbm": "%s", "minnoise_dbm": "%s", "maxsignal_dbm": "%s", "maxnoise_dbm": "%s", "signal_rssi": "%s", "noise_rssi": "%s", "minsignal_rssi": "%s", "minnoise_rssi": "%s", "maxsignal_rssi": "%s", "maxnoise_rssi": "%s"}' % (bssid, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi))

def handle_capability(client, capabilities):
	print 'capabilities: %s ' % (capabilities)
	r.publish('the_channel', '{"type": "capability","capabilities": "%s"}' % (capabilities))

def handle_channel(client, channel, time_on, packets, packetsdelta, usecused, bytes, bytesdelta, networks, maxsignal_dbm, maxsignal_rssi, maxnoise_dbm, maxnoise_rssi, activenetworks):
	print 'channel: %s time_on: %s packets: %s packetsdelta: %s usecused: %s bytes: %s bytesdelta: %s networks: %s maxsignal_dbm: %s maxsignal_rssi: %s maxnoise_dbm: %s maxnoise_rssi: %s activenetworks: %s ' % (channel, time_on, packets, packetsdelta, usecused, bytes, bytesdelta, networks, maxsignal_dbm, maxsignal_rssi, maxnoise_dbm, maxnoise_rssi, activenetworks)
	r.publish('the_channel', '{"type": "channel","channel": "%s", "time_on": "%s", "packets": "%s", "packetsdelta": "%s", "usecused": "%s", "bytes": "%s", "bytesdelta": "%s", "networks": "%s", "maxsignal_dbm": "%s", "maxsignal_rssi": "%s", "maxnoise_dbm": "%s", "maxnoise_rssi": "%s", "activenetworks": "%s"}' % (channel, time_on, packets, packetsdelta, usecused, bytes, bytesdelta, networks, maxsignal_dbm, maxsignal_rssi, maxnoise_dbm, maxnoise_rssi, activenetworks))

def handle_client(client, bssid, mac, type, firsttime, lasttime, manuf, llcpackets, datapackets, cryptpackets, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, agglat, agglon, aggalt, aggpoints, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, atype, ip, gatewayip, datasize, maxseenrate, encodingset, carrierset, decrypted, channel, fragments, retries, newpackets, freqmhz, cdpdevice):
	print 'bssid: %s mac: %s type: %s firsttime: %s lasttime: %s manuf: %s llcpackets: %s datapackets: %s cryptpackets: %s gpsfixed: %s minlat: %s minlon: %s minalt: %s minspd: %s maxlat: %s maxlon: %s maxalt: %s maxspd: %s agglat: %s agglon: %s aggalt: %s aggpoints: %s signal_dbm: %s noise_dbm: %s minsignal_dbm: %s minnoise_dbm: %s maxsignal_dbm: %s maxnoise_dbm: %s signal_rssi: %s noise_rssi: %s minsignal_rssi: %s minnoise_rssi: %s maxsignal_rssi: %s maxnoise_rssi: %s bestlat: %s bestlon: %s bestalt: %s atype: %s ip: %s gatewayip: %s datasize: %s maxseenrate: %s encodingset: %s carrierset: %s decrypted: %s channel: %s fragments: %s retries: %s newpackets: %s freqmhz: %s cdpdevice: %s ' % (bssid, mac, type, firsttime, lasttime, manuf, llcpackets, datapackets, cryptpackets, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, agglat, agglon, aggalt, aggpoints, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, atype, ip, gatewayip, datasize, maxseenrate, encodingset, carrierset, decrypted, channel, fragments, retries, newpackets, freqmhz, cdpdevice)
	r.publish('the_channel', '{"type": "client","bssid": "%s", "mac": "%s", "type": "%s", "firsttime": "%s", "lasttime": "%s", "manuf": "%s", "llcpackets": "%s", "datapackets": "%s", "cryptpackets": "%s", "gpsfixed": "%s", "minlat": "%s", "minlon": "%s", "minalt": "%s", "minspd": "%s", "maxlat": "%s", "maxlon": "%s", "maxalt": "%s", "maxspd": "%s", "agglat": "%s", "agglon": "%s", "aggalt": "%s", "aggpoints": "%s", "signal_dbm": "%s", "noise_dbm": "%s", "minsignal_dbm": "%s", "minnoise_dbm": "%s", "maxsignal_dbm": "%s", "maxnoise_dbm": "%s", "signal_rssi": "%s", "noise_rssi": "%s", "minsignal_rssi": "%s", "minnoise_rssi": "%s", "maxsignal_rssi": "%s", "maxnoise_rssi": "%s", "bestlat": "%s", "bestlon": "%s", "bestalt": "%s", "atype": "%s", "ip": "%s", "gatewayip": "%s", "datasize": "%s", "maxseenrate": "%s", "encodingset": "%s", "carrierset": "%s", "decrypted": "%s", "channel": "%s", "fragments": "%s", "retries": "%s", "newpackets": "%s", "freqmhz": "%s", "cdpdevice": "%s"}' % (bssid, mac, type, firsttime, lasttime, manuf, llcpackets, datapackets, cryptpackets, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, agglat, agglon, aggalt, aggpoints, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi, bestlat, bestlon, bestalt, atype, ip, gatewayip, datasize, maxseenrate, encodingset, carrierset, decrypted, channel, fragments, retries, newpackets, freqmhz, cdpdevice))
        
def handle_clisrc(client, bssid, mac, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi):
	print 'bssid: %s mac: %s uuid: %s lasttime: %s numpackets: %s signal_dbm: %s noise_dbm: %s minsignal_dbm: %s minnoise_dbm: %s maxsignal_dbm: %s maxnoise_dbm: %s signal_rssi: %s noise_rssi: %s minsignal_rssi: %s minnoise_rssi: %s maxsignal_rssi: %s maxnoise_rssi: %s ' % (bssid, mac, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi)
	r.publish('the_channel', '{"type": "clisrc","bssid": "%s", "mac": "%s", "uuid": "%s", "lasttime": "%s", "numpackets": "%s", "signal_dbm": "%s", "noise_dbm": "%s", "minsignal_dbm": "%s", "minnoise_dbm": "%s", "maxsignal_dbm": "%s", "maxnoise_dbm": "%s", "signal_rssi": "%s", "noise_rssi": "%s", "minsignal_rssi": "%s", "minnoise_rssi": "%s", "maxsignal_rssi": "%s", "maxnoise_rssi": "%s"}' % (bssid, mac, uuid, lasttime, numpackets, signal_dbm, noise_dbm, minsignal_dbm, minnoise_dbm, maxsignal_dbm, maxnoise_dbm, signal_rssi, noise_rssi, minsignal_rssi, minnoise_rssi, maxsignal_rssi, maxnoise_rssi))

def handle_clitag(client, bssid, mac, tag, value):
	print 'bssid: %s mac: %s tag: %s value: %s ' % (bssid, mac, tag, value)
	r.publish('the_channel', '{"type": "clitag","bssid": "%s", "mac": "%s", "tag": "%s", "value": "%s"}' % (bssid, mac, tag, value))

def handle_common(client, phytype, macaddr, firsttime, lasttime, packets, llcpackets, errorpackets, datapackets, cryptpackets, datasize, newpackets, channel, frequency, freqmhz, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signaldbm, noisedbm, minsignaldbm, minnoisedbm, signalrssi, noiserssi, minsignalrssi, minnoiserssi, maxsignalrssi, maxnoiserssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints):
	print 'phytype: %s macaddr: %s firsttime: %s lasttime: %s packets: %s llcpackets: %s errorpackets: %s datapackets: %s cryptpackets: %s datasize: %s newpackets: %s channel: %s frequency: %s freqmhz: %s gpsfixed: %s minlat: %s minlon: %s minalt: %s minspd: %s maxlat: %s maxlon: %s maxalt: %s maxspd: %s signaldbm: %s noisedbm: %s minsignaldbm: %s minnoisedbm: %s signalrssi: %s noiserssi: %s minsignalrssi: %s minnoiserssi: %s maxsignalrssi: %s maxnoiserssi: %s bestlat: %s bestlon: %s bestalt: %s agglat: %s agglon: %s aggalt: %s aggpoints: %s ' % (phytype, macaddr, firsttime, lasttime, packets, llcpackets, errorpackets, datapackets, cryptpackets, datasize, newpackets, channel, frequency, freqmhz, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signaldbm, noisedbm, minsignaldbm, minnoisedbm, signalrssi, noiserssi, minsignalrssi, minnoiserssi, maxsignalrssi, maxnoiserssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints)
	r.publish('the_channel', '{"type": "common","phytype": "%s", "macaddr": "%s", "firsttime": "%s", "lasttime": "%s", "packets": "%s", "llcpackets": "%s", "errorpackets": "%s", "datapackets": "%s", "cryptpackets": "%s", "datasize": "%s", "newpackets": "%s", "channel": "%s", "frequency": "%s", "freqmhz": "%s", "gpsfixed": "%s", "minlat": "%s", "minlon": "%s", "minalt": "%s", "minspd": "%s", "maxlat": "%s", "maxlon": "%s", "maxalt": "%s", "maxspd": "%s", "signaldbm": "%s", "noisedbm": "%s", "minsignaldbm": "%s", "minnoisedbm": "%s", "signalrssi": "%s", "noiserssi": "%s", "minsignalrssi": "%s", "minnoiserssi": "%s", "maxsignalrssi": "%s", "maxnoiserssi": "%s", "bestlat": "%s", "bestlon": "%s", "bestalt": "%s", "agglat": "%s", "agglon": "%s", "aggalt": "%s", "aggpoints": "%s"}' % (phytype, macaddr, firsttime, lasttime, packets, llcpackets, errorpackets, datapackets, cryptpackets, datasize, newpackets, channel, frequency, freqmhz, gpsfixed, minlat, minlon, minalt, minspd, maxlat, maxlon, maxalt, maxspd, signaldbm, noisedbm, minsignaldbm, minnoisedbm, signalrssi, noiserssi, minsignalrssi, minnoiserssi, maxsignalrssi, maxnoiserssi, bestlat, bestlon, bestalt, agglat, agglon, aggalt, aggpoints))

def handle_critfail(client, id, time, message):
	print 'id: %s time: %s message: %s ' % (id, time, message)
	r.publish('the_channel', '{"type": "critfail","id": "%s", "time": "%s", "message": "%s"}' % (id, time, message))

def handle_error(client, cmdid, text):
	print 'cmdid: %s text: %s ' % (cmdid, text)
	r.publish('the_channel', '{"type": "error","cmdid": "%s", "text": "%s"}' % (cmdid, text))

def handle_gps(client, lat, lon, alt, spd, heading, fix, satinfo, hdop, vdop, connected):
	print 'lat: %s lon: %s alt: %s spd: %s heading: %s fix: %s satinfo: %s hdop: %s vdop: %s connected: %s ' % (lat, lon, alt, spd, heading, fix, satinfo, hdop, vdop, connected)
	r.publish('the_channel', '{"type": "gps","lat": "%s", "lon": "%s", "alt": "%s", "spd": "%s", "heading": "%s", "fix": "%s", "satinfo": "%s", "hdop": "%s", "vdop": "%s", "connected": "%s"}' % (lat, lon, alt, spd, heading, fix, satinfo, hdop, vdop, connected))

def handle_info(client, networks, packets, crypt, noise, dropped, rate, filtered, clients, llcpackets, datapackets, numsources, numerrorsources):
	print 'networks: %s packets: %s crypt: %s noise: %s dropped: %s rate: %s filtered: %s clients: %s llcpackets: %s datapackets: %s numsources: %s numerrorsources: %s ' % (networks, packets, crypt, noise, dropped, rate, filtered, clients, llcpackets, datapackets, numsources, numerrorsources)
	r.publish('the_channel', '{"type": "info","networks": "%s", "packets": "%s", "crypt": "%s", "noise": "%s", "dropped": "%s", "rate": "%s", "filtered": "%s", "clients": "%s", "llcpackets": "%s", "datapackets": "%s", "numsources": "%s", "numerrorsources": "%s"}' % (networks, packets, crypt, noise, dropped, rate, filtered, clients, llcpackets, datapackets, numsources, numerrorsources))

def handle_kismet(client, version, starttime, servername, dumpfiles, uid):
	print 'version: %s starttime: %s servername: %s dumpfiles: %s uid: %s ' % (version, starttime, servername, dumpfiles, uid)
	r.publish('the_channel', '{"type": "kismet","version": "%s", "starttime": "%s", "servername": "%s", "dumpfiles": "%s", "uid": "%s"}' % (version, starttime, servername, dumpfiles, uid))

def handle_nettag(client, bssid, tag, value):
	print 'bssid: %s tag: %s value: %s ' % (bssid, tag, value)
	r.publish('the_channel', '{"type": "nettag","bssid": "%s", "tag": "%s", "value": "%s"}' % (bssid, tag, value))

def handle_packet(client, type, subtype, timesec, encrypted, weak, beaconrate, sourcemac, destmac, bssid, ssid, prototype, sourceip, destip, sourceport, destport, nbtype, nbsource, sourcename):
	print 'type: %s subtype: %s timesec: %s encrypted: %s weak: %s beaconrate: %s sourcemac: %s destmac: %s bssid: %s ssid: %s prototype: %s sourceip: %s destip: %s sourceport: %s destport: %s nbtype: %s nbsource: %s sourcename: %s ' % (type, subtype, timesec, encrypted, weak, beaconrate, sourcemac, destmac, bssid, ssid, prototype, sourceip, destip, sourceport, destport, nbtype, nbsource, sourcename)
	r.publish('the_channel', '{"type": "packet","type": "%s", "subtype": "%s", "timesec": "%s", "encrypted": "%s", "weak": "%s", "beaconrate": "%s", "sourcemac": "%s", "destmac": "%s", "bssid": "%s", "ssid": "%s", "prototype": "%s", "sourceip": "%s", "destip": "%s", "sourceport": "%s", "destport": "%s", "nbtype": "%s", "nbsource": "%s", "sourcename": "%s"}' % (type, subtype, timesec, encrypted, weak, beaconrate, sourcemac, destmac, bssid, ssid, prototype, sourceip, destip, sourceport, destport, nbtype, nbsource, sourcename))

def handle_plugin(client, filename, name, version, description, unloadable, root):
	print 'filename: %s name: %s version: %s description: %s unloadable: %s root: %s ' % (filename, name, version, description, unloadable, root)
	r.publish('the_channel', '{"type": "plugin","filename": "%s", "name": "%s", "version": "%s", "description": "%s", "unloadable": "%s", "root": "%s"}' % (filename, name, version, description, unloadable, root))

def handle_protocols(client, protocols):
	print 'protocols: %s ' % (protocols)
	r.publish('the_channel', '{"type": "protocols","protocols": "%s"}' % (protocols))

def handle_remove(client, bssid):
	print 'bssid: %s ' % (bssid)
	r.publish('the_channel', '{"type": "remove","bssid": "%s"}' % (bssid))

def handle_source(client, interface, type, username, channel, uuid, packets, hop, velocity, dwell, hop_time_sec, hop_time_usec, channellist, error, warning):
	print 'interface: %s type: %s username: %s channel: %s uuid: %s packets: %s hop: %s velocity: %s dwell: %s hop_time_sec: %s hop_time_usec: %s channellist: %s error: %s warning: %s ' % (interface, type, username, channel, uuid, packets, hop, velocity, dwell, hop_time_sec, hop_time_usec, channellist, error, warning)
	r.publish('the_channel', '{"type": "source","interface": "%s", "type": "%s", "username": "%s", "channel": "%s", "uuid": "%s", "packets": "%s", "hop": "%s", "velocity": "%s", "dwell": "%s", "hop_time_sec": "%s", "hop_time_usec": "%s", "channellist": "%s", "error": "%s", "warning": "%s"}' % (interface, type, username, channel, uuid, packets, hop, velocity, dwell, hop_time_sec, hop_time_usec, channellist, error, warning))

def handle_ssid(client, mac, checksum, type, ssid, beaconinfo, cryptset, cloaked, firsttime, lasttime, maxrate, beaconrate, packets, beacons, dot11d):
	print 'mac: %s checksum: %s type: %s ssid: %s beaconinfo: %s cryptset: %s cloaked: %s firsttime: %s lasttime: %s maxrate: %s beaconrate: %s packets: %s beacons: %s dot11d: %s ' % (mac, checksum, type, ssid, beaconinfo, cryptset, cloaked, firsttime, lasttime, maxrate, beaconrate, packets, beacons, dot11d)
	r.publish('the_channel', '{"type": "ssid","mac": "%s", "checksum": "%s", "type": "%s", "ssid": "%s", "beaconinfo": "%s", "cryptset": "%s", "cloaked": "%s", "firsttime": "%s", "lasttime": "%s", "maxrate": "%s", "beaconrate": "%s", "packets": "%s", "beacons": "%s", "dot11d": "%s"}' % (mac, checksum, type, ssid, beaconinfo, cryptset, cloaked, firsttime, lasttime, maxrate, beaconrate, packets, beacons, dot11d))

def handle_status(client, text, flags):
	print 'text: %s flags: %s ' % (text, flags)
	r.publish('the_channel', '{"type": "status","text": "%s", "flags": "%s"}' % (text, flags))

def handle_string(client, bssid, source, dest, string):
	print 'bssid: %s source: %s dest: %s string: %s ' % (bssid, source, dest, string)
	r.publish('the_channel', '{"type": "string","bssid": "%s", "source": "%s", "dest": "%s", "string": "%s"}' % (bssid, source, dest, string))

def handle_terminate(client, text):
	print 'text: %s ' % (text)
	r.publish('the_channel', '{"type": "terminate","text": "%s"}' % (text))

def handle_time(client, timesec):
	print 'timesec: %s ' % (timesec)
	r.publish('the_channel', '{"type": "time","timesec": "%s"}' % (timesec))

def handle_trackinfo(client, devices, packets, datapackets, cryptpackets, errorpackets, filterpackets, packetrate):
	print 'devices: %s packets: %s datapackets: %s cryptpackets: %s errorpackets: %s filterpackets: %s packetrate: %s ' % (devices, packets, datapackets, cryptpackets, errorpackets, filterpackets, packetrate)
	r.publish('the_channel', '{"type": "trackinfo","devices": "%s", "packets": "%s", "datapackets": "%s", "cryptpackets": "%s", "errorpackets": "%s", "filterpackets": "%s", "packetrate": "%s"}' % (devices, packets, datapackets, cryptpackets, errorpackets, filterpackets, packetrate))


def handle_wepkey(client, origin, bssid, key, encrypted, failed):
	print 'origin: %s bssid: %s key: %s encrypted: %s failed: %s ' % (origin, bssid, key, encrypted, failed)
	r.publish('the_channel', '{"type": "wepkey","origin": "%s", "bssid": "%s", "key": "%s", "encrypted": "%s", "failed": "%s"}' % (origin, bssid, key, encrypted, failed))

#def handle_gps_min(client, lat, lon):
#        print '{"lat":"%s","long":"%s"}' % (lat, lon)
#        print 'LAT: "%s" LONG: %s' % (lat, lon)
#        r.publish('the_channel', '{"lat":"%s","long":"%s", "type": "gps"}' % (lat, lon))

#k.register_handler('CLIENT', handlers.print_fields)

k.register_handler('ALERT', handle_alert)
k.register_handler('BATTERY', handle_battery)
k.register_handler('BSSID', handle_bssid)
k.register_handler('BSSIDSRC', handle_bssidsrc)
k.register_handler('CAPABILITY', handle_capability)
k.register_handler('CHANNEL', handle_channel)
k.register_handler('CLIENT', handle_client)
k.register_handler('CLISRC', handle_clisrc)
k.register_handler('CLITAG', handle_clitag)
k.register_handler('COMMON', handle_common)
k.register_handler('CRITFAIL', handle_critfail)
k.register_handler('ERROR', handle_error)
k.register_handler('GPS', handle_gps)
k.register_handler('INFO', handle_info)
k.register_handler('KISMET', handle_kismet)
k.register_handler('NETTAG', handle_nettag)
k.register_handler('PACKET', handle_packet)
k.register_handler('PLUGIN', handle_plugin)
k.register_handler('PROTOCOLS', handle_protocols)
k.register_handler('REMOVE', handle_remove)
k.register_handler('SOURCE', handle_source)
k.register_handler('SSID', handle_ssid)
k.register_handler('STATUS', handle_status)
k.register_handler('STRING', handle_string)
k.register_handler('TERMINATE', handle_terminate)
k.register_handler('TIME', handle_time)
k.register_handler('TRACKINFO', handle_trackinfo)
k.register_handler('WEPKEY', handle_wepkey)


try:
    while True:
        k.listen()
except KeyboardInterrupt:
    pprint(k.protocols)
    log.info('Exiting...')
