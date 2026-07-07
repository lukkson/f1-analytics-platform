from container import ApplicationContainer

container = ApplicationContainer()
races = container.extraction_container.race_client.get_races(2024)
print(races[0])


races = container.extraction_container.race_client.get_races(2024)
drivers = container.extraction_container.driver_client.get_drivers(2024)
laps = container.extraction_container.lap_client.get_laps(2024, 1)
pit_stops = container.extraction_container.pit_stop_client.get_pit_stops(2024, 1)
for round_num in range(1, 25):
    standings = container.extraction_container.standings_client.get_standings(
        2024, round_num
    )
    container.loading_container.f1_db.insert_standings(standings)
    print(f"Załadowano standings dla rundy {round_num}")

container.loading_container.f1_db.insert_races(races)
container.loading_container.f1_db.insert_drivers(drivers)
container.loading_container.f1_db.insert_lap_times(laps)
container.loading_container.f1_db.insert_pit_stops(pit_stops)
