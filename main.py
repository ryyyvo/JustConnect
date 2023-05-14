from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(port=8600) # Change the port number to any other available port number