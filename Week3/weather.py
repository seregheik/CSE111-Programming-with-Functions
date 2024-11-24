def main():
    def wind_chill(temperature, wind_speed):
        chill_factor = 35.74 \
                       + 0.6215 * temperature \
                       - 35.75 * wind_speed ** 0.16 \
                       + 0.4275 * temperature * wind_speed ** 0.16
        return round(chill_factor, 1)

if __name__ == '__main__':
    main()