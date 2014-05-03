import argparse
import os.path
import sys
import svn_broker
import db_broker
from ConfigParser import SafeConfigParser


class CommitExtractor(object):

    def _parse_config(self, cnf_file):

        if not os.path.isfile(cnf_file):
            raise NoConfigError('Filename %s not found' % cnf_file)

        cnf = SafeConfigParser()
        cnf.read(cnf_file)
        self.db_cnf = dict(cnf.items("db"))
        self.svn_cnf = dict(cnf.items("svn"))

    def init_svn_client(self):
        pass

    def extract(self):
        pass


class NoConfigError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
