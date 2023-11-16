from django.conf import settings
import logging
import subprocess


logger = logging.getLogger(__name__)


def backup_database():
	backap_script = settings.BASE_DIR + '/backap/backup.sh'
	logger.info(backap_script)  
	subprocess.call([backap_script])
 