#!/usr/bin/python27

import datetime
import json
import logging
from optparse import OptionParser
import sys
import time

import requests

from elasticsearch import Elasticsearch


class TkElasticSearch(object):
    ENDPOINTS = {"PROD": 'http://search-portal-3s-vpw7n4zpz3x6hrh3q36oh3gnxu.ap-southeast-1.es.amazonaws.com:80/',
                 "INTG": 'http://search-es-integrated-environment-3s-s6bvfkwcech7mdmbksvmut2mr4.ap-southeast-1.es.amazonaws.com:80/'
                 }

    def __init__(self, env="PROD"):
        env = env.upper()
        self._endpoint = env
        self.switch_to(self._endpoint)

    def info(self):
        """
        Show elasticsearch info
        """
        print "Support %r" % (self.ENDPOINTS.keys())
        print self._endpoint, self._es.ping()

    def switch_to(self, env):
        """
        Switch elasticsearch
        @param env: environment string
        @rtype: boolean
        """
        env = env.upper()
        if env not in self.ENDPOINTS:
            raise TypeError("Not supported endpoint %r", env.upper())

        self._endpoint = env
        self._es = Elasticsearch([self.ENDPOINTS[self._endpoint]])

    def search_click_by_id(self, clickid, doc_type="info"):
        payload = {"query": {"match": {"clickid": clickid}}}
        res = self._es.search(index='tk_receiver_click_*', doc_type=doc_type, body=payload, timeout=30)
        hits = res["hits"]
        if hits["total"] < 1:
            logging.debug("Not found click %r", clickid)
            return None

        # click info
        _source = hits["hits"][0]["_source"]
        ts = _source["@timestamp"]
        click = _source["@fields"]
        logging.info("Found click %r, %s %s %s", clickid, ts, click["campaign"], click["channel"])
        return click

    def search_install_by_id(self, clickid, doc_type="info"):
        payload = {"query": {"match": {"mobvista_clickid": clickid}}}
        res = self._es.search(index='tk_receiver_install_*', doc_type=doc_type, body=payload, timeout=30)
        hits = res["hits"]
        if hits["total"] < 1:
            logging.debug("Not found install %r", clickid)
            return None

        # install info
        _source = hits["hits"][0]["_source"]
        ts = _source["@timestamp"]
        install = _source["@fields"]
        logging.info("Found install %r, %s %s %s", clickid, ts, install["campaign"], install["channel"])
        return install

    """
    @param start_ts: start timestamp, millisecs
    @param end_ts: end timestamp, millisecs
    @note: the result is sorted and uniqued
    """

    def search_unmatched_install(self, start_ts, end_ts):
        if end_ts - start_ts > 24 * 3600 * 1000:
            raise TypeError("Too large range for search %r - %r" % (start_ts, end_ts))

        payload = {"size": 500000,
                   "query": {"filtered": {"query": {"match_all": {}}, "filter": {
                       "bool": {"must": [
                           {"range": {"@timestamp": {"from": start_ts, "to": end_ts}}},
                           {"exists": {"field": "@fields.query.mobvista_clickid"}}]
                       }}}}}
        res = self._es.search(index='tk_receiver_install_*', doc_type='warning', body=payload, timeout=45)
        records = res['hits']['hits']

        click_list = []  # [(),()]
        idset = set()
        for record in records:
            clickid = record['_source']['@fields']['query']['mobvista_clickid']
            install = record['_source']['@fields']

            if len(clickid) != 24 or clickid in idset:
                if clickid in idset:
                    logging.debug("Duplicated clickid found %r, skip", clickid)
                continue
            if record['_source']['@fields']['error'] != "Data Not Found":
                continue

            click_list.append((clickid, install))

        logging.info("Found %s unique unmatched install", len(click_list))
        return click_list

    def search_warning_install(self, start_ts, end_ts, size=1500000, timeout=45):
        """
        """
        payload = {"size": size,
                   "query": {"filtered": {"query": {"match_all": {}}, "filter": {
                       "bool": {"must": [
                           {"range": {"@timestamp": {"from": start_ts, "to": end_ts}}}
                       ]
                       }}}}}
        res = self._es.search(index='tk_receiver_install_*', doc_type='warning', body=payload, timeout=timeout)
        records = res['hits']['hits']
        return records

if __name__ == "__main__":
    search = TkElasticSearch()
    search.search_click_by_id('')
