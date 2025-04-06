import random
import csv


def generate_equipment_data(n=400):
    # IdE
    # Condition
    # NameE
    # IdR
    conditions = ['T', 'F']
    equipment_names = [
        'Treadmill',
        'Dumbbells',
        'Yoga Mats',
        'Bench Press',
        'Row Machine',
        'Kettlebells',
        'Pull-up Bar',
        'Med Ball',
        'Ab Roller',
        'Smith Machine',
        'Jump Rope',
        'Stepper',
        'Trap Bar',
        'Barbell',
        'Spin Bike',
        'Plyo Box',
        'Power Rack',
        'Weight Plate',
        'Squat Rack',
        'Lat Machine',
        'Glute Band',
        'Dip Bars',
        'EZ Curl Bar',
        'Leg Press',
        'Calf Raise',
        'Wrist Roller',
        'Grip Trainer',
        'Slam Ball',
        'Core Trainer',
        'Push-up Bar',
        'Air Bike',
        'Chest Fly',
        'Hip Abductor',
        'Back Ext',
        'Cable Tower',
        'Bosu Ball',
        'Punch Bag',
        'Resistance Band',
        'Arm Bike',
        'Thigh Master'
    ]

    room_ids = list(range(1, 401))

    return [(i, random.choice(conditions), random.choice(equipment_names), random.choice(room_ids)) for i in
            range(1, n + 1)]


def generate_certified_for_data(n=400):  # מדריך מוסמך עבור סוג שיעור
    # IdCT
    # Id (trainer 400+)
    return [(i, i + 400) for i in range(1, n + 1)]


def generate_registers_for_data(n=400):  # מנוי נרשם לשיעור
    # Id
    # IdC
    class_ids = list(range(1, 401))
    return [(i, random.choice(class_ids)) for i in range(1, n + 1)]


def save_to_csv(filename, data, headers):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)


def generate_and_save_data():
    equipment_data = generate_equipment_data()
    certified_data = generate_certified_for_data()
    registers_data = generate_registers_for_data()

    save_to_csv("Equipment.csv", equipment_data, ["idE", "Condition", "NameE", "IdR"])
    save_to_csv("Certified_For.csv", certified_data, ["IdCT", "Id"])
    save_to_csv("Registers_For.csv", registers_data, ["Id", "IdC"])

    print("Generated and saved 400 random data entries for each table to CSV files successfully!")


if __name__ == "__main__":
    generate_and_save_data()
