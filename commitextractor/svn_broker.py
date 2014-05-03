import pysvn
import time


class SvnBroker(object):

    def __init__(self, repo_url, pysvn_client=None):
        self.repo_url = repo_url
        if not pysvn_client:
            pysvn_client = pysvn.Client()
        self.client = pysvn_client

    def get_logs(self, start_rev, end_rev):
        if start_rev:
            start = pysvn.Revision(pysvn.opt_revision_kind.number, start_rev)
        else:
            start = pysvn.Revision(pysvn.opt_revision_kind.head)

        if end_rev is None:
            end_rev = 0

        end = pysvn.Revision(pysvn.opt_revision_kind.number, end_rev)

        raw_logs = self.client.log(self.repo_url, revision_start=start, revision_end=end, discover_changed_paths=True)

        return self.parse_logs(raw_logs)

    def parse_logs(self, logs):
        parsed_logs = []
        for log in logs:
            parsed_log = {}
            parsed_log['time'] = time.localtime(log['date'])
            parsed_log['files'] = [path['path'] for path in log['changed_paths']]
            parsed_logs.append({log.revision.number: parsed_log})
        return parsed_logs
