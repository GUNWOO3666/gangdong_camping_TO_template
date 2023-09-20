import pygetwindow as gw
import pyautogui
import time

# 카카오톡 창의 제목 (활성 창을 찾을 때 사용)
kakao_window_title = "친구이름"

# 대기 시간 (1시간 = 3600초)
interval = 3600

try:
    while True:
        # 카카오톡 창을 찾고 활성화합니다.
        kakao_window = gw.getWindowsWithTitle(kakao_window_title)
        if kakao_window:
            kakao_window[0].activate()
            
            # "생일축하해"를 입력하고 Enter 키를 누릅니다.
            pyautogui.write("toddlfcnrgkgo")
            pyautogui.press("enter")
        else:
            print("카카오톡 창을 찾을 수 없습니다.")

        # 1시간 동안 대기합니다.
        time.sleep(interval)

except KeyboardInterrupt:
    print("작업을 중지합니다.")