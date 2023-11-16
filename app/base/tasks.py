from config.celery import app
from celery import shared_task
from celery.utils.log import get_task_logger

from base.okt.cian import OktCianTask
from base.okt.kuplusrazu import OktKuplusrazuTask
from base.okt.pinterest import OktPinterestTask
from base.oktavito import OktAvitoTask
from base.oktolan import OktOlanTask
from base.pikabu import PikabuTask
from base.pvesti import PvestiTask
from base.riac34 import Rica32Task


logger = get_task_logger(__name__)


@shared_task
def parse_pvesti_news():
	logger.info("PvestiTask")
	pvesti = PvestiTask()
	pvesti.get_values()


@shared_task
def parse_riac34():
	logger.info("Rica32Task")
	riac = Rica32Task()
	riac.get_values()


@shared_task
def parse_pikabu():
	logger.info("PikabuTask")
	pikabu = PikabuTask()
	pikabu.get_values()


@shared_task
def parse_okt_avito():
	logger.info("OktAvitoTask")
	avito = OktAvitoTask()
	avito.get_values()


@shared_task
def parse_okt_olan():
	logger.info("OktOlanTask")
	avito = OktOlanTask()
	avito.get_values()


@shared_task
def parse_okt_pinterest():
	logger.info("OktPinterestTask")
	avito = OktPinterestTask()
	avito.get_values()


@shared_task
def parse_okt_kupisrazu():
	logger.info("OktKuplusrazuTask")
	avito = OktKuplusrazuTask()
	avito.get_values()


@shared_task
def parse_okt_cian():
	logger.info("OktCianTask")
	cian = OktCianTask()
	cian.get_values()