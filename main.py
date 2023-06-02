import interface


def main():
    interface.window.after(1000, interface.threading.Thread(target=interface.lisa_loop).start())
    interface.window.mainloop()


if __name__ == "__main__":
    main()
