from bqwm.database import db
from bqdm.models import JobConfiguration


def createReservation(config, jobdesc):
    configs = jobdesc.get("Configurations", [])
    if len(configs) > 0:
        utility_function = configs[0].get('utility_function', "")
        estimated_time = configs[0].get('estimated_time', -1)
        price = configs[0].get('price', 0)
        config = JobConfiguration(utility_function, estimated_time, price)
        print config
        db.session.add(config)
        db.session.commit()
        return configs[0]

    return {}
