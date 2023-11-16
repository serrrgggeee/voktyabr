from celery import shared_task
from celery.utils.log import get_task_logger
from config.celery import app
from main.workers.backup_database import backup_database


logger = get_task_logger(__name__)


@shared_task
def backup_databas():
	logger.info("Bacup run.")
	backup_database()

