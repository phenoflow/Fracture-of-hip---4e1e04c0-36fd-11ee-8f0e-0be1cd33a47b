# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7K1D000","system":"readv2"},{"code":"7K1D600","system":"readv2"},{"code":"7K1D700","system":"readv2"},{"code":"7K1H600","system":"readv2"},{"code":"7K1H700","system":"readv2"},{"code":"7K1H800","system":"readv2"},{"code":"7K1J000","system":"readv2"},{"code":"7K1J500","system":"readv2"},{"code":"7K1J600","system":"readv2"},{"code":"7K1J700","system":"readv2"},{"code":"7K1J900","system":"readv2"},{"code":"7K1JB00","system":"readv2"},{"code":"7K1JC00","system":"readv2"},{"code":"7K1JD00","system":"readv2"},{"code":"7K1JE00","system":"readv2"},{"code":"7K1JF00","system":"readv2"},{"code":"7K1JG00","system":"readv2"},{"code":"S4E0.00","system":"readv2"},{"code":"S4E1.00","system":"readv2"},{"code":"S4E2.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fracture-of-hip-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fracture-of-hip-joint---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fracture-of-hip-joint---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fracture-of-hip-joint---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
