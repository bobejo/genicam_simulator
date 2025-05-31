import pathlib
import config_parser, camera_register, broadcast


camera_config_path = pathlib.Path(__file__).parent / "data" / "camera_config.yaml"
camera_configuration = config_parser.CameraConfig(configuration_file=camera_config_path)

camera_register = camera_register.CameraRegister(camera_configuration)

# Set Mac address since gen_tl looks for it when detecting compatible cameras
camera_register.set_value("Device_MAC_address_High_Network_interface_0", 0x012345)
camera_register.set_value("Device_MAC_address_Low_Network_interface_0", 0x678910)


cb = broadcast.CameraBroadcaster(ip="0.0.0.0", register=camera_register)
cb.start()
cb.join()