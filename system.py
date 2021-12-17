from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)


    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System.__find_hardware_by_name(hardware_name)

        if not hardware:
            return "Hardware does not exist"

        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System.__find_hardware_by_name(hardware_name)
        software = System.__find_software_by_name(software_name)

        if not hardware or not software:
            return "Some of the components do not exist"

        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        result = "System Analysis\n"
        hardware_memory_consumption = sum([hard.memory for hard in System._hardware])
        software_memory_consumption = sum([soft.memory_consumption for soft in System._software])
        hardware_capacity_consumption = sum([hard.capacity for hard in System._hardware])
        software_capacity_consumption = sum([soft.capacity_consumption for soft in System._software])
        result += f"""Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {software_memory_consumption} / {hardware_memory_consumption}
Total Capacity Taken: {software_capacity_consumption} / {hardware_capacity_consumption}"""

        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            express_software = System.__find_software("ExpressSoftware")
            if express_software:
                components = [hardware for hardware in hardware.software_components if hardware.__class__.__name__ == "ExpressSoftware"]
                result += f"Express Software Components: {len(components)}\n"
            else:
                result += "Express Software Components: 0\n"

            light_software = System.__find_software("LightSoftware")
            if light_software:
                components = [hardware for hardware in hardware.software_components if hardware.__class__.__name__ == "LightSoftware"]
                result += f"Light Software Components: {len(components)}\n"
            else:
                result += "Light Software Components: 0\n"

            result += f"""Memory Usage: {sum(memory.memory_consumption for memory in hardware.software_components)} / {hardware.memory}
Capacity Usage: {sum(capacity.capacity_consumption for capacity in hardware.software_components)} / {hardware.capacity}
Type: {hardware.hardware_type}\n"""
            if hardware.software_components == 0:
                result += "Software Components: None\n"
            else:
                result += f"Software Components: {', '.join(name.name for name in hardware.software_components)}\n"

        return result.strip()

    @staticmethod
    def __find_hardware_by_name(name):
        for hardware in System._hardware:
            if hardware.name == name:
                return hardware

    @staticmethod
    def __find_software_by_name(name):
        for software in System._software:
            if software.name == name:
                return software


    @staticmethod
    def __find_software(software_name):
        for hardware in System._hardware:
            for software in hardware.software_components:
                if software.__class__.__name__ == software_name:
                    return software


