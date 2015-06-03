def createReservation(jobdesc):
    configs = jobdesc.get("Configurations", [])
    if len(configs) > 0:
        return configs[0]

    return None
