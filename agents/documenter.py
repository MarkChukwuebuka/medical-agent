import datetime

class Documenter:

    @staticmethod
    def log(prompt, response):
        with open("logs.txt", "a") as f:
            f.write("\n-----------------\n")
            f.write(str(datetime.datetime.now()))
            f.write("\nPROMPT:\n")
            f.write(prompt)
            f.write("\nRESPONSE:\n")
            f.write(response)