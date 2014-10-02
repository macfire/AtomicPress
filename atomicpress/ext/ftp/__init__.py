# -*- coding: utf-8 -*-

"""
atomicpress.ext.ftp
----------
Upload blog export to ftp.
"""

from atomicpress.utils import ftpsync
from atomicpress.app import app

from flask_script import Manager


FtpSyncCommand = Manager(usage='Sync files against ftp')

@FtpSyncCommand.command
def sync():
    ftpsync.set_default(app.config["FTP_HOST"], app.config["FTP_USERNAME"],
                        app.config["FTP_PASSWORD"])

    ftpsync.sync_folder(app.config["FREEZER_DESTINATION"],
                        app.config["FTP_DESTINATION"])
