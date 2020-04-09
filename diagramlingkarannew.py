import matplotlib.pyplot as plt

def total_students(list_student):
    return sum(list_student)

def percent_program(list_students):
    result =[]

    for value in list_students:
        result.append((value/total_students(list_students))*100)

    return result

def do_piechart(list_percent, list_programs):
    fig1, ax1 = plt.subplots()
    ax1.pie(list_percent, explode=None, labels=list_programs,
            autopct='%1.1f%%', shadow=True, startangle=90)

    plt.show()
    plt.savefig('diagramlingkaran.png')

if __name__ =="__main__":

    list_programs = []
    list_students = []

    datasize = int(input("Jumlah makanan favorit: "))

    print("Masukkan daftar makanan favorit")
    for index in range(datasize):
        data_program = str(input("Makanan: "))
        list_programs.append(data_program)

    print("Masukkan jumlah siswa yang menyukai")
    for index in range(datasize):
        data_student = int(input("jumlah siswa: "))
        list_students.append(data_student)

    print("daftar makanan favorit {}".format(list_programs))
    print("jumlah siswa {}".format(list_students))
    print("total siswa {}".format(total_students(list_students)))

    list_percent = percent_program(list_students)
    print("percent program {}".format(list_percent))

    do_piechart(list_percent, list_programs)
