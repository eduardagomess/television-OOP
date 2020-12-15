class Television:

    def __init__(self, volume=0, channel=0):
        self.volume = volume
        self.channel = channel

    def getVolume (self):
        return self.volume

    def getChannel(self):
        return self.channel

    def changeVolume(self, new_volume):
        self.volume += new_volume
        return self.volume

    def updateChannel(self, new_channel_number):
        self.channel = new_channel_number
        return self.channel

    def modifyChannel(self, new_channel):
        self.channel += new_channel
        return self.channel
