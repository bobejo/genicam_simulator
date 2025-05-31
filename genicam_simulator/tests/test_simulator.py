from harvesters.core import Harvester


h = Harvester()
h.add_cti_file("/opt/mvIMPACT_Acquire/lib/x86_64/mvGenTLProducer.cti")
h.update()
print(h.device_info_list)
