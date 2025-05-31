import threading
import time
import socket
import logging

import commands, camera_register
from genicam_simulator.commands import DiscoveryAck

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class  CameraBroadcaster(threading.Thread):
    """
    Thread that listens and replies to a camera identification request
    """
    def __init__(self, ip: str, register: camera_register.CameraRegister):
        threading.Thread.__init__(self)
        self.ip = ip
        self.register = register
        self._stop = threading.Event()

    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,  1)  # Enable broadcast
            try:
                server_socket.bind((self.ip, 3956))
            except OSError:
                logger.error('Failed to bind on %s, trying again!', self.ip)
                time.sleep(3)
            server_socket.setblocking(False)
            server_socket.settimeout(3)
            while not self._stop.is_set():
                try:
                    response = server_socket.recvfrom(1024)
                    if response[0]:
                        logger.debug("Got valid request from %s. It responded with %s", response[1], response[0])
                        if response[0][2:4] == commands.PackageCommandTypes.DISCOVERY_CMD:
                            logger.info("Got DISCOVERY_CMD request from %s", response[1])
                            packet = DiscoveryAck(self.register).payload
                            server_socket.sendto(packet, response[1])
                        elif response[0][2:4] == commands.PackageCommandTypes.FORCEIP_CMD:
                            logger.info("Got FORCEIP_CMD request from %s", response[1])
                        elif commands.PackageCommandTypes.READREG_CMD:
                            logger.info("Got READREG_CMD request from %s", response[1])
                        elif commands.PackageCommandTypes.WRITEREG_CMD:
                            logger.info("Got WRITEREG_CMD request from %s", response[1])
                        elif commands.PackageCommandTypes.READMEM_CMD:
                            logger.info("Got READMEM_CMD request from %s", response[1])
                        elif commands.PackageCommandTypes.WRITEMEM_CMD:
                            logger.info("Got WRITEMEM_CMD request from %s", response[1])
                        elif commands.PackageCommandTypes.PACKETRESEND_CMD:
                            logger.info("Got PACKETRESEND_CMD request from %s", response[1])
                        else:
                            logger.info("Got unknown request from %s: %s", response[1], response[0])

                except socket.timeout:
                    pass
                except IndexError:
                    logger.debug("Received an unexpected response format: %s", response)
                    pass


    def _create_request(self, response: bytes) -> bytes:
        return b"hello"
