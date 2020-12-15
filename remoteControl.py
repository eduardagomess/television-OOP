class RemoteControl:

    def __init__(self, a):
        self.television = a

    def increaseVolume(self):
        return self.television.changeVolume(+1)

    def decreaseVolume(self):
        return self.television.changeVolume(-1)

    def increaseChannel(self):
        return self.television.modifyChannel(+1)

    def decreaseChannel(self):
        return self.television.modifyChannel(-1)

    def updateChannel(self, new_channel_number):
        return self.television.updateChannel(new_channel_number)

    def showChannel(self):
        return self.television.getChannel()

    def showVolume(self):
        return self.television.getVolume()
