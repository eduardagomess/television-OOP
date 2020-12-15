from remoteControl import RemoteControl
from television import Television

television = Television()
remote_control = RemoteControl(television)

remote_control.updateChannel(35)
remote_control.increaseChannel()
remote_control.increaseVolume()
