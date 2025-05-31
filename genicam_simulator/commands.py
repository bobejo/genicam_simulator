import enum

import camera_register

class PackageTypes:
    ACK = b"\x00\x00"
    CMD = b"\x42"
    ERROR = b"\x80"
    UNKNOWN = b"\x8F"

class PackageCommandTypes:
    DISCOVERY_CMD = b"\x00\x02"
    DISCOVERY_ACK = b"\x00\x03"
    FORCEIP_CMD = b"\x00\x04"
    FORCEIP_ACK = b"\x00\x05"
    # Streaming Protocol Control
    PACKETRESEND_CMD = b"\x00\x40"
    #Device Memory Access
    READREG_CMD = b"\x00\x80"
    READREG_ACK = b"\x00\x81"
    WRITEREG_CMD = b"\x00\x82"
    WRITEREG_ACK = b"\x00\x83"
    READMEM_CMD = b"\x00\x84"
    READMEM_ACK = b"\x00\x85"
    WRITEMEM_CMD = b"\x00\x86"
    WRITEMEM_ACK = b"\x00\x87"
    PENDING_ACK = b"\x00\x89"




class DiscoveryAck:
    def __init__(self, register: camera_register.CameraRegister):

        self.major_version = register.get("MajorVersion")
        self.minor_version = register.get("MinorVersion")
        self.device_mode = register.get("Device_Mode")
        self.mac_address_higher = register.get("Device_MAC_address_High_Network_interface_0")
        self.mac_address_lower = register.get("Device_MAC_address_Low_Network_interface_0")
        self.vendor_name = register.get("VendorName")
        self.model_name = register.get("ModelName")
        self.user_defined_name = register.get("UserDefinedName")
        self.serial_number = register.get("Serial_number", "12345")
        self.manufacturer_information = register.get("Manufacturer_specific_information", "")
        self.device_version = register.get("Device_version", "1")
        self.current_ip = register.get("Current_IP_address_Network_interface_0")
        self.current_netmask = register.get("Current_subnet_mask_Network_interface_0")



        self.payload = (PackageTypes.ACK +
                    PackageCommandTypes.DISCOVERY_ACK +
                    self.minor_version.to_bytes() +
                    self.minor_version.to_bytes() +
                    self.device_mode.to_bytes() +
                    self.mac_address_higher.to_bytes() +
                    self.mac_address_lower.to_bytes() +
                    self.current_ip.to_bytes() +
                    self.current_netmask.to_bytes() +
                    bytes(4) + 
                    bytes(4) +
                    bytes(12) +
                    self.current_ip.to_bytes() +
                    bytes(12) +
                    self.current_netmask.to_bytes() +
                    bytes(12) +
                    bytes(4) +
                    self.vendor_name.value +
                    self.model_name.value +
                    self.device_version.to_bytes() +
                    self.manufacturer_information.value +
                    self.serial_number.to_bytes() +
                    self.user_defined_name.value
                    )

    def __value__(self):
        return self.payload

class ReadMemoryAck:
    def __init__(self, address: int, size: int, data: bytes):
        self.address = address
        self.size = size
        self.data = data

    def to_bytes(self) -> bytes:
        address_bytes = self.address.to_bytes(4, byteorder="big")
        size_bytes = self.size.to_bytes(4, byteorder="big")
        return super().to_bytes() + address_bytes + size_bytes + self.data

class WriteMemoryAck:
    def __init__(self, address: int, size: int):
        self.address = address
        self.size = size

    def to_bytes(self) -> bytes:
        address_bytes = self.address.to_bytes(4, byteorder="big")
        size_bytes = self.size.to_bytes(4, byteorder="big")
        return super().to_bytes() + address_bytes + size_bytes
    
class ReadRegisterAck:
    def __init__(self, register_address: int, value: int):
        self.register_address = register_address
        self.value = value

    def to_bytes(self) -> bytes:
        address_bytes = self.register_address.to_bytes(4, byteorder="big")
        value_bytes = self.value.to_bytes(4, byteorder="big")
        return super().to_bytes() + address_bytes + value_bytes

class WriteRegisterAck:
    def __init__(self, register_address: int, value: int):
        self.register_address = register_address
        self.value = value

    def to_bytes(self) -> bytes:
        address_bytes = self.register_address.to_bytes(4, byteorder="big")
        value_bytes = self.value.to_bytes(4, byteorder="big")
        return super().to_bytes() + address_bytes + value_bytes    