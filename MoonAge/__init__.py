import logging
import datetime
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        birthday = name
        birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        full_moons = full_moons_since_birthday(birthday)
        return func.HttpResponse(f"Hello, for this birthday {name}, your moon age is {full_moons}.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a birthday into the query string (yyyy-mm-dd).",
             status_code=200
        )

def full_moons_since_birthday(birthday):
        today = datetime.datetime.now().date()
        delta = today - birthday
        days_since_birthday = delta.days
        full_moon_cycle = 29.53
        return round(days_since_birthday / full_moon_cycle)

    


 