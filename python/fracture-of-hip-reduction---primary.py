# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7K1D011","system":"readv2"},{"code":"7K1D012","system":"readv2"},{"code":"7K1D013","system":"readv2"},{"code":"7K1D014","system":"readv2"},{"code":"7K1D015","system":"readv2"},{"code":"7K1D016","system":"readv2"},{"code":"7K1D017","system":"readv2"},{"code":"7K1D018","system":"readv2"},{"code":"7K1D019","system":"readv2"},{"code":"7K1D01B","system":"readv2"},{"code":"7K1D01D","system":"readv2"},{"code":"7K1DE00","system":"readv2"},{"code":"7K1L400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fracture-of-hip-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fracture-of-hip-reduction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fracture-of-hip-reduction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fracture-of-hip-reduction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
