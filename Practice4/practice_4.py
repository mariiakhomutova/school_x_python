from import_this import (generate_race_data, RaceInfo,)

N = None


def sort_racers(RACE_DATA: dict) -> dict:
    sorted_racers: dict = {}
    for value in RACE_DATA.values():
        finished_place = value["FinishedPlace"]
        sorted_racers[finished_place] = value
    return sorted_racers


def print_first_racer(sorted_racers: dict) -> None:
    winner: str = f"Выиграл - {sorted_racers[1]['RacerName']}!!!! Поздравляем!!!"
    print(winner + "\n" + "-" * len(winner))


def print_top3_racers(sorted_racers: dict) -> None:
    print("Первые 3 места:\n")
    for n in range(1, 4):
        value: dict = sorted_racers[n]
        print(f"Гонщик на {n} месте\n" +
              f"\tИмя: {value['RacerName']}\n" +
              f"\tКоманда: {value['RacerTeam']}\n" +
              f"\tВремя: {value['FinishedTimeSeconds'] // 3600}:" +
              f"{value['FinishedTimeSeconds'] % 3600 // 60}:" +
              f"{value['FinishedTimeSeconds'] % 60} (H:M:S)\n"
              )


if __name__ == '__main__':
    race_data: RaceInfo = generate_race_data(10)
    sorted_racers: dict = sort_racers(race_data)
    print_first_racer(sorted_racers)
    print_top3_racers(sorted_racers)