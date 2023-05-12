from Television import *


def main():
    window = Tk()
    window.title('Television and Remote')
    window.geometry('500x500')
    window.resizable(False, False)
    Television(window)
    window.mainloop()


if __name__ == '__main__':
    main()
