from celery import shared_task
from celery.utils.log import get_task_logger
from vk.worker.oktyabrskiy_rayon.send_to_wall import (
	sendAvitoToOktyabrskiyRayon,
	sendPvestiToOktyabrskiyRayon,
	sendPinterestToOktyabrskiyRayon
)



logger = get_task_logger(__name__)


@shared_task
def send_avito_to_oktyabrskiy_rayon():
	logger.info("sendAvitoToOktyabrskiyRayon")
	sendAvitoToOktyabrskiyRayon()


@shared_task
def send_pvesti_to_oktyabrskiy_rayon():
	logger.info("sendPvestiToOktyabrskiyRayon")
	sendPvestiToOktyabrskiyRayon()


@shared_task
def send_pinterest_to_oktyabrskiy_rayon():
	logger.info("sendPinterestToOktyabrskiyRayon")
	sendPinterestToOktyabrskiyRayon()

