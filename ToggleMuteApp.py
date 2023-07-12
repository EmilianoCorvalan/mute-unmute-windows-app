from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import keyboard

target_app = "FIFA23.exe"  # Reemplazar con el nombre de la aplicación a mutear
target_process = None
volume_interface = None

def toggle_mute():
    if not volume_interface:
        return

    current_mute = volume_interface.GetMute()
    volume_interface.SetMute(not current_mute, None)
    print("Estado del mute:", "Muteado" if not current_mute else "Desmuteado")

def setup_volume_interface():
    global volume_interface

    sessions = AudioUtilities.GetAllSessions()

    for session in sessions:
        volume = session._ctl.QueryInterface(ISimpleAudioVolume)
        if session.Process and session.Process.name() == target_app:
            volume_interface = volume
            break

    if not volume_interface:
        print("No se encontró la aplicación especificada.")
        exit()

keyboard.add_hotkey("p", toggle_mute)  # Reemplaza la tecla para mutear-desmutear
keyboard.add_hotkey("q", lambda: keyboard.unhook_all())  # Tecla de escape para salir del programa

setup_volume_interface()

#Mantener el programa en ejecución
keyboard.wait()