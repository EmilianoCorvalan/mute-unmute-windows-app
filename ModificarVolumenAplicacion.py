from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(-3, None) #Set the master volume for all the system.  (-62 = 0% volumen  -3 = 100% volumen)
# volume.SetMute(False, None) You can use true or false to mute o unmute


sessions = AudioUtilities.GetAllSessions()
for session in sessions:
    volume = session._ctl.QueryInterface(ISimpleAudioVolume)
    if session.Process and session.Process.name() == "Spotify.exe":
        volume.SetMasterVolume(0.01, None)

# El resto es creatividad