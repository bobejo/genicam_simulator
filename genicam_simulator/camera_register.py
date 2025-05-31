from typing import Literal

import config_parser


class RegisterInfo:
    def __init__(self, name: str, address: int, size: int, description: str = ""):
        self.name = name
        self.address = address
        self.size = size
        self.value = 0

    def __str__(self):
        return f"{self.name} (0x{self.address:04x}): [{self.size} bytes]"

    def to_bytes(self, byteorder: Literal["big", "little"] = "big") -> bytes:
        return self.value.to_bytes(self.size, byteorder=byteorder)

    def __repr__(self):
        return f"RegisterInfo(name={self.name}, address=0x{self.address:04x}, size={self.size}, value={self.value})"


class CameraRegister:
    def __init__(self, camera_config: config_parser.CameraConfig):
        self.camera_config = camera_config
        self.registers: list[RegisterInfo] = [
            RegisterInfo("MajorVersion", 0x0000, 2),
            RegisterInfo("MinorVersion", 0x0002, 2),
            RegisterInfo("Device_Mode", 0x0004, 4),
            RegisterInfo("Device_MAC_address_High_Network_interface_0", 0x0008, 3),
            RegisterInfo("Device_MAC_address_Low_Network_interface_0", 0x000C, 3),
            RegisterInfo("Supported_IP_configuration_Network_interface_0", 0x0010, 4),
            RegisterInfo("Current_IP_configuration_procedure_Network_interface_0", 0x0014, 4),
            RegisterInfo("Current_IP_address_Network_interface_0", 0x0024, 4),
            RegisterInfo("Current_subnet_mask_Network_interface_0", 0x0034, 4),
            RegisterInfo("Current_default_Gateway_Network_interface_0", 0x0044, 4),
            RegisterInfo("VendorName", 0x0048, 32),
            RegisterInfo("ModelName", 0x0068, 32),
            RegisterInfo("Device_version", 0x0088, 32),
            RegisterInfo("Manufacturer_specific_information", 0x00A8, 48),
            RegisterInfo("Serial_number", 0x00D8, 16),
            RegisterInfo("UserDefinedName", 0x00E8, 16),
            RegisterInfo("XML_Device_Description_File_First_URL", 0x0200, 512),
            RegisterInfo("XML_Device_Description_File_Second_URL", 0x0400, 512),
            RegisterInfo("Number_of_network_interfaces", 0x0600, 4),
            RegisterInfo("Persistent_IP_address_Network_interface_0", 0x064C, 4),
            RegisterInfo("Persistent_subnet_mask_Network_interface_0", 0x065C, 4),
            RegisterInfo("Persistent_default_gateway_Network_interface_0", 0x066C, 4),
            RegisterInfo("Link_Speed_Network_interface_0", 0x0670, 4),
            RegisterInfo("MAC_address_High_Network_interface_1", 0x0680, 4),
            RegisterInfo("MAC_address_Low_Network_interface_1", 0x0684, 4),
            RegisterInfo("Supported_IP_configuration_Network_interface_1", 0x0688, 4),
            RegisterInfo("Current_IP_configuration_procedure_Network_interface_1", 0x068C, 4),
            RegisterInfo("Current_IP_address_Network_interface_1", 0x069C, 4),
            RegisterInfo("Current_subnet_mask_Network_interface_1", 0x06AC, 4),
            RegisterInfo("Current_default_gateway_Network_interface_1", 0x06BC, 4),
            RegisterInfo("Persistent_IP_address_Network_interface_1", 0x06CC, 4),
            RegisterInfo("Persistent_subnet_mask_Network_interface_1", 0x06DC, 4),
            RegisterInfo("Persistent_default_gateway_Network_interface_1", 0x06EC, 4),
            RegisterInfo("Link_Speed_Network_interface_1", 0x06F0, 4),
            RegisterInfo("MAC_address_High_Network_interface_2", 0x0700, 4),
            RegisterInfo("MAC_address_Low_Network_interface_2", 0x0704, 4),
            RegisterInfo("Supported_IP_configuration_Network_interface_2", 0x0708, 4),
            RegisterInfo("Current_IP_configuration_procedure_Network_interface_2", 0x070C, 4),
            RegisterInfo("Current_IP_address_Network_interface_2", 0x071C, 4),
            RegisterInfo("Current_subnet_mask_Network_interface_2", 0x072C, 4),
            RegisterInfo("Current_default_gateway_Network_interface_2", 0x073C, 4),
            RegisterInfo("Persistent_IP_address_Network_interface_2", 0x074C, 4),
            RegisterInfo("Persistent_subnet_mask_Network_interface_2", 0x075C, 4),
            RegisterInfo("Persistent_default_gateway_Network_interface_2", 0x076C, 4),
            RegisterInfo("Link_Speed_Network_interface_2", 0x0770, 4),
            RegisterInfo("MAC_address_High_Network_interface_3", 0x0780, 4),
            RegisterInfo("MAC_address_Low_Network_interface_3", 0x0784, 4),
            RegisterInfo("Supported_IP_configuration_Network_interface_3", 0x0788, 4),
            RegisterInfo("Current_IP_configuration_procedure_Network_interface_3", 0x078C, 4),
            RegisterInfo("Current_IP_address_Network_interface_3", 0x079C, 4),
            RegisterInfo("Current_subnet_mask_Network_interface_3", 0x07AC, 4),
            RegisterInfo("Current_default_gateway_Network_interface_3", 0x07BC, 4),
            RegisterInfo("Persistent_IP_address_Network_interface_3", 0x07CC, 4),
            RegisterInfo("Persistent_subnet_mask_Network_interface_3", 0x07DC, 4),
            RegisterInfo("Persistent_default_gateway_Network_interface_3", 0x07EC, 4),
            RegisterInfo("Link_Speed_Network_interface_3", 0x07F0, 4),
            RegisterInfo("Number_of_Message_channels", 0x0900, 4),
            RegisterInfo("Number_of_Stream_channels", 0x0904, 4),
            RegisterInfo("Number_of_Action_Signals", 0x0908, 4),
            RegisterInfo("Action_Device_Key", 0x090C, 4),
            RegisterInfo("Stream_channels_Capability", 0x092C, 4),
            RegisterInfo("Message_channel_Capability", 0x0930, 4),
            RegisterInfo("GVCP_Capability", 0x0934, 4),
            RegisterInfo("Heartbeat_timeout", 0x0938, 4),
            RegisterInfo("Timestamp_tick_frequency_High", 0x093C, 4),
            RegisterInfo("Timestamp_tick_frequency_Low", 0x0940, 4),
            RegisterInfo("Timestamp_control", 0x0944, 4),
            RegisterInfo("Timestamp_value_latched_High", 0x0948, 4),
            RegisterInfo("Timestamp_value_latched_Low", 0x094C, 4),
            RegisterInfo("Discovery_ACK_delay", 0x0950, 4),
            RegisterInfo("GVCP_Configuration", 0x0954, 4),
            RegisterInfo("Pending_Timeout", 0x0958, 4),
            RegisterInfo("Control_Switchover_Key", 0x095C, 4),
            RegisterInfo("Control_Channel_Privilege", 0x0A00, 4),
            RegisterInfo("Primary_Application_Port", 0x0A04, 4),
            RegisterInfo("Primary_Application_IP_address", 0x0A14, 4),
            RegisterInfo("MCP", 0x0B00, 4),
            RegisterInfo("MCDA", 0x0B10, 4),
            RegisterInfo("MCTT", 0x0B14, 4),
            RegisterInfo("MCRC", 0x0B18, 4),
            RegisterInfo("MCSP", 0x0B1C, 4),
            RegisterInfo("Stream_Channel_Port_0", 0x0D00, 4),
            RegisterInfo("Stream_Channel_Packet_Size_0", 0x0D04, 4),
            RegisterInfo("SCPD0", 0x0D08, 4),
            RegisterInfo("Stream_Channel_Destination_Address_0", 0x0D18, 4),
            RegisterInfo("SCSP0", 0x0D1C, 4),
            RegisterInfo("SCC0", 0x0D20, 4),
            RegisterInfo("SCCFG0", 0x0D24, 4),
            RegisterInfo("SCP1", 0x0D40, 4),
            RegisterInfo("SCPS1", 0x0D44, 4),
            RegisterInfo("SCPD1", 0x0D48, 4),
            RegisterInfo("SCDA1", 0x0D58, 4),
            RegisterInfo("SCSP1", 0x0D5C, 4),
            RegisterInfo("SCC1", 0x0D60, 4),
            RegisterInfo("SCCFG1", 0x0D64, 4),
            RegisterInfo("SCP511", 0x8CC0, 4),
            RegisterInfo("SCPS511", 0x8CC4, 4),
            RegisterInfo("SCPD511", 0x8CC8, 4),
            RegisterInfo("SCDA511", 0x8CD8, 4),
            RegisterInfo("SCSP511", 0x8CDC, 4),
            RegisterInfo("SCC511", 0x8CE0, 4),
            RegisterInfo("SCCFG511", 0x8CE4, 4),
            RegisterInfo("Manifest_Table", 0x9000, 512),
            RegisterInfo("ACTION_GROUP_KEY0", 0x9800, 4),
            RegisterInfo("ACTION_GROUP_MASK0", 0x9804, 4),
            RegisterInfo("ACTION_GROUP_KEY1", 0x9810, 4),
            RegisterInfo("ACTION_GROUP_MASK1", 0x9814, 4),
            RegisterInfo("ACTION_GROUP_KEY127", 0x9FF0, 4),
            RegisterInfo("ACTION_GROUP_MASK127", 0x9FF4, 4)
        ]
        self.set_values()
        self.set_value("Device_Mode", 0x0003)

    def get(self, name: str, default = None):
        for reg in self.registers:
            if reg.name == name:
                return reg
        return default

    def get_value(self, name: str) -> int:
        reg = self.get(name)
        if reg:
            return reg.value
        else:
            raise ValueError(f"Register {name} not found.")

    def get_size(self, name) -> int | None:
        reg = self.get(name)
        if reg:
            return reg.size
        return None

    def set_value(self, name: str, value: int | bytes) -> None:
        reg = self.get(name)
        if reg:
            reg.value = value
        else:
            raise ValueError(f"Register {name} not found.")

    def set_values(self) -> None:
        for name, value in self.camera_config.get("RegisterDescription").items():
            try:
                if isinstance(value, str):
                    size = self.get_size(name)
                    if size:
                        self.set_value(name, value.encode("utf-8").ljust(size, b"\x00"))
                    else:
                        self.set_value(name, value.encode("utf-8"))
                else:
                    self.set_value(name, value)
            except ValueError as e:
                pass
