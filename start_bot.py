# If function is oneline only there is no need in this function.
def main():
    import setup # import goes first in file.
    setup.client.run_until_disconnected()
if __name__ == '__main__':
    main()
