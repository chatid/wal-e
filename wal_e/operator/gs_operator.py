from wal_e.blobstore.swift import calling_format
from wal_e.operator.backup import Backup
from wal_e.worker.swift import swift_worker


class GSBackup(Backup):
    """
    A performs Google Storeage uploads of PostgreSQL WAL files and clusters
    """

    def __init__(self, layout, creds, gpg_key_id):
        super(GSBackup, self).__init__(layout, creds, gpg_key_id)
        self.cinfo = calling_format
        self.worker = swift_worker
