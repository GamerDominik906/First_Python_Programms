print("Hi, was wär dein Alter")
alter = input("Gebe ein Alter ein, wenn du z.b heute geboren wurdest, 80 Jahre ")

try:
    alter = int(alter)
    jahr = 2024 + alter


    print(f"So also, dieses Jahr ist 2024, wenn du heute geboren wärst, wär in {alter} Jahren, {jahr}")

except ValueError:
    print("Bitte gib eine gültige Zahl für das Alter ein.")