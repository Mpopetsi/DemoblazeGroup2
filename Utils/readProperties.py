import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/loginDetails.ini")


class ReadConfig:
    def getbaseUrl(self):
        # sauceDemoURL = config.get('URLs', 'sauceDemoURL')
        # return sauceDemoURL
        return config.get('URLs', 'baseUrl')

    def getUsername(self):
        username = config.get('Login Details', 'username')
        return username

    def getPasswo2rd(self):
        password = config.get('Login Details', 'password')
        return password
