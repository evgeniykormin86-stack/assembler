import logging
import graypy

logger = logging.getLogger("python-sdk")
logger.setLevel(logging.INFO)
handler = graypy.GELFUDPHandler("graylog", 12201)  # Graylog service name in Docker
logger.addHandler(handler)
