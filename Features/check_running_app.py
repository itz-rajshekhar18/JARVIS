import psutil;

def get_running_apps_windows():
    try:
        process = [proc.name() for proc in psutil.process_iter(['name'])]
        return list(set(process))
    except Exception as e:
        return f"Error : {e}"

def check_running_app():
    running_apps = get_running_apps_windows()
    print("Running Applications :")
    for app in running_apps:
        print(app)