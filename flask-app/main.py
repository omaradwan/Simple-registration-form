from website import create_app

app=create_app()


if __name__=='__main__': # to make the app start from here
    app.run(debug=True) #debug=True to make the changes i've done before runnin
        