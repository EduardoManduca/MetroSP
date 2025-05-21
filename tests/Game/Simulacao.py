import time
import pyautogui

def capturar_posicao_mouse():
    print("Posicione o mouse no local desejado. Você tem 5 segundos...")
    time.sleep(5)
    x, y = pyautogui.position()
    print(f"Posição capturada: x={x}, y={y}")
    return x, y

if __name__ == "__main__":
    capturar_posicao_mouse()