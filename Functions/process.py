import psutil


def ProcessDisplay():
    list_process= []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])

            list_process.append(pinfo)

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return list_process


def main():
    print("process monitor")

    list_process = ProcessDisplay()

    for elem in list_process:
        print(elem)


if __name__ == "__main__":
    main()
