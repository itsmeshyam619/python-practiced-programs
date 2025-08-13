import csv,operator,os


def create_file(file_name):
    with open(file_name,'a') as Fp:
        writer=csv.writer(Fp)
        col_names=[x.strip() for x in input(" Enter column names := ").split(',')]
        writer.writerow(col_names)
        
        ans='y'
        while ans=='y'or ans=='Y':
            data=[x.strip() for x in input(f"data for {col_names}:").split(',')]
            writer.writerow(data)
            ans=input("do you want to continue (y/n) := ")
            print("\n\t\tappended")

    Fp.close()

def read_file(file_name):
    with open(file_name,'r') as Fp:
        reader=csv.reader(Fp)
        next(reader)
        print(reader)
        sorted_array=sorted(reader)
        for r in sorted_array:
            print(r)
        print('\n')
        Fp.seek(0) # ***********
        print('*******************************************')
        print(*reader,sep='\n')
        print('*******************************************')
    Fp.close()

def main():

    # Get the path of the current script
    current_folder = os.path.dirname(__file__)

    file_name=input("Enter file name := ")
    # Construct the file path
    extension = ".csv"

    # Ensure the file name has the correct extension
    if not file_name.endswith(extension):
        file_name += extension

    file_path = os.path.join(current_folder, file_name)

    csv.dialect=csv.register_dialect('mydialect',delimiter=',',skipinitialspace=True,quoting=csv.QUOTE_ALL,lineterminator="\n")

    if os.path.exists(file_path):
        read_file(file_path)
    else:
        create_file(file_path)

main()