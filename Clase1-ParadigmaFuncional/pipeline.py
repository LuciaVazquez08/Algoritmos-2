import csv

def csv_line_reader(path):
    with open(path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            yield row

def csv_rows_generator(rows):
    for line in rows:
        yield line

def csv_dict_generator(rows_generator, headers):
    for fields in rows_generator:
        yield dict(zip(headers, fields))

def calculate_sum_of_sepal_width(species_generator, target_species):
    total_sum = 0
    for species in species_generator:
        if species['species'] == target_species:
            total_sum += float(species['sepal_width'])
    return total_sum

def calculate_average_of_sepal_width(species_generator, target_species):
    count = 0
    total_sum = 0
    for species in species_generator:
        if species['species'] == target_species:
            total_sum += float(species['sepal_width'])
            count += 1
    return total_sum / count if count > 0 else 0

if __name__ == "__main__":
    path = "C:\Users\Usuario\algo2"
    rows = csv_line_reader(path)
    headers = next(rows)
    rows_generator = csv_rows_generator(rows)
    species_generator = csv_dict_generator(rows_generator, headers)

    # Suma de los sepal_width de todas las especies Iris-setosa
    sum_of_setosa_sepal_width = calculate_sum_of_sepal_width(species_generator, 'Iris-setosa')
    print("Suma de los sepal_width de todas las especies Iris-setosa:", sum_of_setosa_sepal_width)

    # Promedio del sepal_width de las especies Iris-setosa
    rows = csv_line_reader(path)  # Reiniciamos el generador
    rows_generator = csv_rows_generator(rows)
    species_generator = csv_dict_generator(rows_generator, headers)
    average_of_setosa_sepal_width = calculate_average_of_sepal_width(species_generator, 'Iris-setosa')
    print("Promedio del sepal_width de las especies Iris-setosa:", average_of_setosa_sepal_width)
