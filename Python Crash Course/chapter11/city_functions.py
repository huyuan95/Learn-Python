def city_country(City, Country, population = 0):
    if population != 0:
        return '%s, %s - population %s' % (City.title(), Country.title(),
                                           str(population))
    else:
        return '%s, %s' % (City.title(), Country.title())

