#
# from setup import handler_bot, callback, handler_client
# from setup import client, exit_bot


def main():
    import setup
    setup.client.run_until_disconnected()
if __name__ == '__main__':
    main()
