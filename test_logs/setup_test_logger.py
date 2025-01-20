import logging
import os

from datetime import datetime


logger = logging.getLogger(__name__)
time_now = datetime.now()
filename = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), f'tests-{time_now}.log'
)
logging.basicConfig(
    filename=filename,
    encoding='utf-8',
    level=logging.DEBUG,
    force=True
)
