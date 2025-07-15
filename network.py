class Packet:
    def __init__(self, src, dst, data):
        self.src = src
        self.dst = dst
        self.data = data
    
    def __str__(self):
        return f"Пакет из {self.src} в {self.dst}: {self.data}"
        
class Computer:
    def __init__(self, name, router):
        self.name = name
        self.router = router
        router.connect(self)

    def send(self, dst, data):
        packet = Packet(self.name, dst, data)
        print(f"{self.name}: Отправка пакета в {dst}")
        self.router.route(packet)

    def receive(self, packet):
        print(f"{self.name}: Принятый пакет - {packet.data}")
        
class Router:
    def __init__(self):
        self.devices = {}
        
    def connect(self, device):
        self.devices[device.name] = device
    
    def route(self, packet):
        if packet.dst in self.devices:
            self.devices[packet.dst].receive(packet)
        else:
            print(f"Маршрутизатор: Пункт назначения '{packet.dst}' не найден!")
            
router = Router()
pc1 = Computer("PC1", router)
pc2 = Computer("PC2", router)
pc1.send("PC2", "Hello, World!")
pc2.send("PC3", "This will fail!")
  
