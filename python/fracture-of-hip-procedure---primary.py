# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"102104.0","system":"med"},{"code":"102313.0","system":"med"},{"code":"105352.0","system":"med"},{"code":"105803.0","system":"med"},{"code":"107358.0","system":"med"},{"code":"107932.0","system":"med"},{"code":"12544.0","system":"med"},{"code":"24493.0","system":"med"},{"code":"28464.0","system":"med"},{"code":"33624.0","system":"med"},{"code":"34764.0","system":"med"},{"code":"34846.0","system":"med"},{"code":"35004.0","system":"med"},{"code":"37998.0","system":"med"},{"code":"38856.0","system":"med"},{"code":"39322.0","system":"med"},{"code":"40999.0","system":"med"},{"code":"43403.0","system":"med"},{"code":"44594.0","system":"med"},{"code":"46258.0","system":"med"},{"code":"46959.0","system":"med"},{"code":"48973.0","system":"med"},{"code":"50450.0","system":"med"},{"code":"52395.0","system":"med"},{"code":"53670.0","system":"med"},{"code":"54819.0","system":"med"},{"code":"55386.0","system":"med"},{"code":"56568.0","system":"med"},{"code":"5742.0","system":"med"},{"code":"57514.0","system":"med"},{"code":"57884.0","system":"med"},{"code":"57889.0","system":"med"},{"code":"58817.0","system":"med"},{"code":"63189.0","system":"med"},{"code":"63554.0","system":"med"},{"code":"65536.0","system":"med"},{"code":"6660.0","system":"med"},{"code":"67028.0","system":"med"},{"code":"69857.0","system":"med"},{"code":"70018.0","system":"med"},{"code":"8719.0","system":"med"},{"code":"94714.0","system":"med"},{"code":"97337.0","system":"med"},{"code":"9792.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('fracture-of-hip-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["fracture-of-hip-procedure---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["fracture-of-hip-procedure---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["fracture-of-hip-procedure---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
