def csv_line_reader(path):
    with open(path, newline='') as csvfile:
        for row in csvfile:
            yield row.strip().split(',')

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
    return round(total_sum,2)

def calculate_average_of_sepal_width(species_generator, target_species):
    count = 0
    total_sum = 0
    for species in species_generator:
        if species['species'] == target_species:
            total_sum += float(species['sepal_width'])
            count += 1
    return round(total_sum / count if count > 0 else 0,2)

if __name__ == "__main__":
    path = "C://Users//Usuario//algo2//IRIS.csv"
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
