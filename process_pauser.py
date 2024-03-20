import psutil
import time

def pause_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            process = psutil.Process(proc.info['pid'])
            process.suspend()
            print(f"{process_name} 프로세스를 일시 중지했습니다.")
            return

    print(f"{process_name} 프로세스가 없습니다.")

def resume_process(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            process = psutil.Process(proc.info['pid'])
            process.resume()
            print(f"{process_name} 프로세스를 다시 시작했습니다.")
            return

    print(f"{process_name} 프로세스가 없습니다.")

if __name__ == "__main__":
    process_name = input("일시 중지할 프로세스 이름을 입력하세요: ")
    pause_process(process_name)
    time.sleep(5)  # 예시로 5초 대기
    resume_process(process_name)
