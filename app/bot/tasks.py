from bot.worker.send_to_avosyka import (
	sendPvestiToAvosyka, 
	sendRiac34ToAvosyka, 
	sendPikabuToAvosyka,
	sendAvitoToAvosyka,
	sendOlanToAvosyka,
	sendPinterestToAvosyka,
	sendKuplusrazuToAvosyka,
	sendCianToAvosyka,
)
from bot.worker.send_to_okt_channel import sendPvesti, sendRiac34
from celery import shared_task
from celery.utils.log import get_task_logger
from config.celery import app


logger = get_task_logger(__name__)


@shared_task
def send_pvesti_to_okt_channel():
	logger.info("sendPvestiToOktChannel")
	sendPvesti()


@shared_task
def send_riac_to_okt_channel():
	logger.info("sendRiac34")
	sendRiac34()


@shared_task
def send_pvesti_to_avosyka():
	logger.info("sendPvestiToAvosyka")
	sendPvestiToAvosyka()


@shared_task
def send_riac_to_avosyka():
	logger.info("sendRiac34ToAvosyka")
	sendRiac34ToAvosyka()

@shared_task
def send_pikabu_to_avosyka():
	logger.info("sendPikabuToAvosyka")
	sendPikabuToAvosyka()


@shared_task
def send_avito_to_avosyka():
	logger.info("sendAvitoToAvosyka")
	sendAvitoToAvosyka()


@shared_task
def send_olan_to_avosyka():
	logger.info("sendOlanToAvosyka")
	sendOlanToAvosyka()


@shared_task
def send_pinterest_to_avosyka():
	logger.info("sendOlanToAvosyka")
	sendPinterestToAvosyka()

@shared_task
def send_kuplusrazu_to_avosyka():
	logger.info("sendKuplusrazuToAvosyka")
	sendKuplusrazuToAvosyka()


@shared_task
def send_cian_to_avosyka():
	logger.info("sendCianToAvosyka")
	sendCianToAvosyka()
